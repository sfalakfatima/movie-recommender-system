import streamlit as st
import pandas as pd
import pickle
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="CineMatch",
    page_icon="🎬",
    layout="wide"
)

# ---------------- Custom CSS ---------------- #

st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #ff4b4b, #ff9068);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .subtitle {
        text-align: center;
        color: #9a9a9a;
        font-size: 1.05rem;
        margin-bottom: 1.8rem;
    }
    .movie-card {
        background-color: rgba(255,255,255,0.03);
        border-radius: 14px;
        padding: 10px;
        text-align: center;
        transition: transform 0.25s ease, box-shadow 0.25s ease;
        border: 1px solid rgba(255,255,255,0.08);
    }
    .movie-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.35);
        border-color: #ff4b4b;
    }
    .movie-card img {
        border-radius: 10px;
        width: 100%;
    }
    .movie-title {
        margin-top: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        min-height: 45px;
    }
    .rating-badge {
        display: inline-block;
        margin-top: 6px;
        padding: 3px 12px;
        border-radius: 20px;
        background: rgba(255, 193, 7, 0.15);
        color: #ffc107;
        font-weight: 700;
        font-size: 0.85rem;
    }
    div[data-testid="stSelectbox"] label {
        font-size: 1.1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎬 CineMatch</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Select a movie and get 5 similar recommendations with posters &amp; ratings</div>',
            unsafe_allow_html=True)

API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
PLACEHOLDER_POSTER = "https://via.placeholder.com/300x450?text=No+Poster"

# ---------------- Session with Retry ---------------- #

session = requests.Session()

retry = Retry(
    total=3,
    backoff_factor=0.5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

adapter = HTTPAdapter(max_retries=retry, pool_connections=20, pool_maxsize=20)

session.mount("https://", adapter)
session.mount("http://", adapter)


# ---------------- Load Data ---------------- #

@st.cache_data
def load_movies():
    movies_dict = pickle.load(open("models/movies_dict.pkl", "rb"))
    return pd.DataFrame(movies_dict)


@st.cache_resource
def load_similarity():
    return pickle.load(open("models/similarity.pkl", "rb"))


movies = load_movies()
similarity = load_similarity()


# ---------------- Fetch Poster ---------------- #

@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    """Returns (poster_url, rating) for a movie_id in a single API call."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": API_KEY, "language": "en-US"}

    try:
        response = session.get(
            url,
            params=params,
            timeout=6,
            headers={"User-Agent": "Mozilla/5.0"}
        )
        response.raise_for_status()
        data = response.json()

        poster = data.get("poster_path")
        poster_url = f"https://image.tmdb.org/t/p/w500{poster}" if poster else None

        rating = data.get("vote_average")
        rating = round(rating, 1) if rating else None

        return poster_url, rating

    except Exception as e:
        print(e)
        return None, None


def fetch_details_parallel(movie_ids):
    """Fetch poster + rating for multiple movies at once -> much faster."""
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_movie_details, movie_ids))
    return results


# ---------------- Recommendation ---------------- #

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    indices = [i[0] for i in movie_list]
    names = [movies.iloc[i].title for i in indices]
    movie_ids = [movies.iloc[i].movie_id for i in indices]

    # parallel fetch instead of sequential loop
    details = fetch_details_parallel(movie_ids)
    posters = [d[0] for d in details]
    ratings = [d[1] for d in details]

    return names, posters, ratings


# ---------------- UI ---------------- #

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies["title"].values
)

col_btn = st.columns([1, 2, 1])[1]
with col_btn:
    recommend_clicked = st.button("✨ Recommend Movies", use_container_width=True)

if recommend_clicked:
    with st.spinner("Finding similar movies..."):
        names, posters, ratings = recommend(selected_movie)

    st.markdown("<br>", unsafe_allow_html=True)
    cols = st.columns(5, gap="medium")

    for i in range(5):
        with cols[i]:
            poster_url = posters[i] if posters[i] else PLACEHOLDER_POSTER
            rating_html = (
                f'<div class="rating-badge">⭐ {ratings[i]}</div>'
                if ratings[i] else
                '<div class="rating-badge">⭐ N/A</div>'
            )
            st.markdown(
                f"""
                <div class="movie-card">
                    <img src="{poster_url}" />
                    <div class="movie-title">{names[i]}</div>
                    {rating_html}
                </div>
                """,
                unsafe_allow_html=True
            )