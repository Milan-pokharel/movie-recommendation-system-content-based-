1.Movie Recommendation System (Content-Based filtering)
-->This is a content-based movie recommendation system built using the TMDB 5000 Movies Dataset.The goal of the project is to recommend movies similar to a selected movie based on their content (overview, genres, keywords, cast, etc.).



2.Project Overview:
This system recommends movies using text similarity.
I used two techniques:

(a). Bag of Words (CountVectorizer)
-First approach
-Creates a word count matrix
-Works but gives less accurate results
-Sometimes recommends unrelated movies because it focuses only on word frequency

(b).TF-IDF Vectorizer
-Improved approach
-Gives more meaningful similarity scores
-Focuses on important words instead of common words
-Produces much better recommendations
-Our Final system uses TF-IDF



3.Dataset
I used the TMDB 5000 Movies Dataset. I Cleaned and preprocessed data,Extracted important features,Combined them into a single "tags" column,Converted tags into numerical vectors and finally Calculated similarity scores using cosine similarity



4.Recommendation Logic
-User selects a movie
-System finds its index in the movie matrix
-Computes similarity scores with all other movies
-Sorts movies based on similarity
-Returns top recommendations
-For each recommended movie, poster images are fetched using the TMDB API



5.Frontend (Streamlit)
-I built a simple interface using Streamlit:
-User chooses a movie from a dropdown
-Presses “Show Recommendation”
-App displays 5 recommended movies
-Each movie is shown with its poster image
-Posters are fetched through TMDB API using the movie ID
-This makes the output visually appealing and user-friendly.



6.Technologies Used
-Python
-Pandas
-NumPy
-NLTK (for text cleaning)
-Scikit-learn (CountVectorizer, TfidfVectorizer, cosine_similarity)
-Streamlit (web interface)
-TMDB API (movie posters)
-Pickle (saving the model and data)



7.Features
Content-based filtering
TF-IDF similarity
Clean preprocessing
TMDB poster display
Interactive Streamlit UI
Accurate and visually appealing recommendations



8.Future Improvements
-Add movie embeddings for more accurate similarity
-Include genres, cast weightage, director score
-Build a hybrid (content + collaborative) model
-Add search option for movies not in dataset