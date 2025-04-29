# 🏆 OscarNet: Predicting Oscar-Worthy Films with Neural Networks

**OscarNet** is a machine learning project designed to predict whether a film will win the **Best Picture Oscar** based on a rich set of features including box office performance, critical reception, genre, timing of release, and industry prestige indicators.

## 📌 Project Objective

Leverage a neural network to classify movies as potential **Oscar winners** or not, using engineered features derived from metadata, release strategies, and historical trends in Academy Awards.

## 🔍 Features Used

The model uses a wide range of features including:

- 🎬 `name` — Title of the movie (embedded or NLP-processed)
- 📅 `weeks_before_oscar` — Strategic release timing
- 💰 `opening_weekend_usd`, `total_box_office_usd`, `production_budget_usd`
- 🌍 `language_en` — Whether the movie is in English
- 🎭 `main_genre_encoded`, `side_genres_multi_encoded`
- ⏱️ `runtime_minutes`
- 🗓️ `release_month`
- 🎞️ `is_franchise`, `based_on_existing_ip`
- 🎬 `director_oscar_wins`, `director_oscar_noms`
- 🎭 `actors_oscar_wins_total`, `actors_oscar_noms_total`
- ✍️ `writer_oscar_wins`, `writer_oscar_noms`
- 🍅 `rt_score_pct`, `imdb_rating_10`
- 🔍 `google_trends_buzz` *(optional, under evaluation)*

> All monetary values are normalized (log-transformed) to reduce skew. Categorical fields are one-hot or multi-hot encoded where appropriate.

## 🧠 Model

A fully connected feedforward **neural network** is trained using TensorFlow/Keras, with layers optimized for classification tasks (binary output: Oscar Win / No Win).

- **Loss Function**: Binary Crossentropy  
- **Optimizer**: Adam  
- **Evaluation Metrics**: Accuracy, Precision, Recall, AUC  

## 📁 Folder Structure

to do
