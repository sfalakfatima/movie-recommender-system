# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using **Python**, **Scikit-learn**, and **Streamlit**. This application recommends similar movies based on content similarity and displays movie posters using the **TMDB API** through an interactive web interface.

---

## 📌 Features

- 🎥 Recommend 5 similar movies
- 🖼️ Display movie posters using TMDB API
- ⚡ Fast recommendations with Cosine Similarity
- 🌐 Interactive Streamlit web application
- 🧠 Content-Based Recommendation System
- 📱 Clean and responsive user interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Requests
- TMDB API
- Pickle

---

## 📂 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── Movie_Recommendation_System.ipynb
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   ├── movies.pkl
│   ├── movies_dict.pkl
│   └── similarity.pkl
│
└── screenshots/
    ├── home.png
    └── recommendation.png
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender-system.git
```

### Move to project directory

```bash
cd movie-recommender-system
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Text Vectorization using CountVectorizer
5. Stemming using NLTK PorterStemmer
6. Cosine Similarity Calculation
7. Movie Recommendation Generation
8. Streamlit Deployment

---

## 📸 Screenshots

### Home Page

> Add `screenshots/home.png`

### Recommendation Page

> Add `screenshots/recommendation.png`

---

## 📈 Future Improvements

- ⭐ Movie Ratings
- 🎭 Genre Filters
- 🔍 Search Suggestions
- 🎬 Trailer Integration
- ❤️ Favorite Movies
- 🌙 Dark Mode
- ☁️ Cloud Deployment

---

## 📦 Dataset

- TMDB 5000 Movie Dataset
- TMDB 5000 Credits Dataset

---

## ⚠️ Note

The `similarity.pkl` file is large and may not be included in this repository due to GitHub's file size limit. You can regenerate it by running the notebook (`Movie_Recommendation_System.ipynb`).

---

## 👩‍💻 Author

**Falak Siddique**

B.Sc. Data Science Student

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.