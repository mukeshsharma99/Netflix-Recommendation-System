import sys
import os
import pandas as pd

# Add project root to Python path
project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.utils import load_pickle

# Load dataset
df = pd.read_csv(
    os.path.join(project_root, "data", "netflix_titles.csv")
)

# Load similarity matrix
similarity = load_pickle(
    os.path.join(project_root, "models", "similarity.pkl")
)


def recommend(movie_name):
    try:
        movie_index = df[df["title"] == movie_name].index[0]

        distances = similarity[movie_index]

        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommendations = []

        for movie in movie_list:
            recommendations.append(
                df.iloc[movie[0]]["title"]
            )

        return recommendations

    except IndexError:
        return ["Movie not found in dataset."]