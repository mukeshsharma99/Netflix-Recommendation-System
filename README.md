# 🎬 Netflix Recommendation System

A Machine Learning project that recommends Netflix movies and TV shows based on content similarity.

Instead of recommending content based on user ratings, this project uses a **Content-Based Recommendation System**. It analyzes information such as genres, descriptions, directors, and cast members to find titles that are similar to the one selected by the user.

The project is built using Python, Scikit-Learn, and Streamlit.

---

## 📌 About the Project

Netflix offers thousands of movies and TV shows, making it difficult for users to decide what to watch next. The goal of this project is to help users discover similar content quickly and easily.

When a user selects a movie or TV show, the recommendation engine finds other titles with similar content and displays the top recommendations.

---

## 🚀 Features

- Content-based recommendation system
- Recommend similar movies and TV shows
- Interactive web application built with Streamlit
- TF-IDF vectorization for text processing
- Cosine similarity for finding related content
- Clean and modular project structure
- Easy to understand and extend

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- TF-IDF Vectorizer
- Cosine Similarity
- Pickle

---

## 📊 Dataset

The project uses the Netflix Titles dataset, which contains information about movies and TV shows available on Netflix.

### Features Used

- Title
- Genre
- Description
- Director
- Cast
- Release Year
- Rating

---

## ⚙️ How It Works

### 1. Data Preprocessing
- Handle missing values
- Clean textual data
- Prepare the dataset for analysis

### 2. Feature Engineering
Important features such as genres, descriptions, directors, and cast members are combined into a single text feature.

### 3. TF-IDF Vectorization
The combined text is converted into numerical vectors using TF-IDF Vectorizer.

### 4. Similarity Calculation
Cosine similarity is used to measure how similar two titles are.

### 5. Recommendation Generation
When a user selects a title, the system returns the most similar movies or TV shows.

---

## 📂 Project Structure

```text
Netflix-Recommendation-System/
│
├── data/
│   └── netflix_titles.csv
│
├── notebooks/
│   └── EDA.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── vectorizer.py
│   ├── recommender.py
│   └── utils.py
│
├── models/
│   ├── similarity.pkl
│   └── tfidf.pkl
│
├── app/
│   ├── app.py
│   ├── recommendation.py
│   └── poster_fetcher.py
│
├── model.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔧 Installation

Clone the repository:

```bash
git clone https://github.com/mukeshsharma99/Netflix-Recommendation-System.git
```

Move into the project directory:

```bash
cd Netflix-Recommendation-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🏗️ Build the Recommendation Model

Generate the similarity matrix and save the trained files:

```bash
python model.py
```

This will create:

```text
models/
├── similarity.pkl
└── tfidf.pkl
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app/app.py
```

Once the application starts, open the URL provided by Streamlit in your browser.

---

## 📈 Future Improvements

- Movie poster integration using TMDB API
- Advanced filtering options
- Personalized recommendations
- Trending and popular content section
- Deployment on Streamlit Cloud or AWS

---

## 🎯 What I Learned

Through this project, I gained hands-on experience with:

- Data preprocessing
- Feature engineering
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- Recommendation Systems
- Streamlit application development
- Project structuring and deployment

---

## 👨‍💻 Author

**Mukesh Kumar**

Aspiring Machine Learning Engineer passionate about building practical AI and Machine Learning applications.

GitHub: https://github.com/mukeshsharma99

If you found this project interesting, feel free to ⭐ the repository.