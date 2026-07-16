# 🎬 Movie Recommendation System

<p align="center">
  <img src="https://img.shields.io/github/stars/sfalakfatima/movie-recommender-system?style=for-the-badge&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/sfalakfatima/movie-recommender-system?style=for-the-badge&color=blue" alt="GitHub Forks">
  <img src="https://img.shields.io/github/license/sfalakfatima/movie-recommender-system?style=for-the-badge&color=green" alt="License">
</p>

<p align="center">
  A high-performance, Machine Learning-powered Content-Based Movie Recommendation System. Built using <b>Python</b>, <b>Scikit-Learn</b>, and deployed with an interactive <b>Streamlit</b> web application that fetches live movie posters via the <b>TMDB API</b>.
</p>

---

## 📌 Table of Contents
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Screenshots](#-screenshots)
- [Project Structure](#-project-structure)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Installation & Usage](#-installation--usage)
- [Dataset Details](#-dataset-details)
- [Future Enhancements](#-future-enhancements)

---

## 📌 Features

*   **⚡ Smart Content Filtering:** Recommends 5 highly relevant movies based on genres, keywords, cast, and crew analysis.
*   **🖼️ Dynamic Poster Fetching:** Integrates live data extraction from the **TMDB API** to show visually appealing movie posters.
*   **🧠 Text Vectorization:** Implements Bag-of-Words via `CountVectorizer` and text normalization with NLTK's `PorterStemmer`.
*   **🌐 Modern UI:** Responsive, minimalist, and clean web layout using Streamlit.

---

## 🛠️ Tech Stack

| Category | Technologies & Libraries |
| :--- | :--- |
| **Language** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) |
| **Data & ML** | ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=flat&logo=scikit-learn&logoColor=white) ![NLTK](https://img.shields.io/badge/NLTK-268B63?style=flat) |
| **Frontend/Web** | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) ![Requests](https://img.shields.io/badge/Requests-000000?style=flat) |
| **API & Storage**| TMDB API, Pickle (Serialization) |

---

## 🖼️ Screenshots

Yahan application ka visual interface aur working flow dekh sakte hain:

## 📸 Screenshots

### 🏠 Home Interface
![Home Page](home.png)

### 🎬 Recommendations Output
![Recommendation Page](recommendations.png)

### 🍿 Extra Recommendations View
![Recommendation Page 2](recommendation2.png)
---

## 📂 Project Structure

```text
movie-recommender-system/
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
├── model/
│   ├── movies.pkl
│   ├── movies_dict.pkl
│   └── similarity.pkl (Generated locally)
├── home.png
├── recommendations.png
├── recommendation2.png
├── .gitignore
├── Movie_Recommendation_System.ipynb
├── README.md
├── app.py
└── requirements.txt
