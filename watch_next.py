import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_md")

def get_similar_movie(description):
    movie_scores = defaultdict(float)
    with open("movies.txt", "r") as file:
        for line in file:
            info = line.strip().split(":")
            if len(info) != 2:  # skip invalid lines
                continue
            title, description = info
            doc = nlp(description)
            similarity = doc.similarity(nlp(description))
            movie_scores[title] = similarity

    # Sort movies by their similarity score in descending order
    sorted_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)

    # Return the title of the most similar movie
    if sorted_movies:
        return sorted_movies[0][0]
    else:
        return None

