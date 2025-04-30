# 🏆 OscarOrNot: Predicting Oscar-Worthy Films with Neural Networks

**OscarNet** is a machine learning project designed to predict whether a film will win the **Best Picture Oscar** based on a rich set of features including box office performance, critical reception, genre, timing of release, and industry prestige indicators.

## 📌 Project Objective

Leverage a neural network to classify movies as potential **Oscar winners** or not, using engineered features derived from metadata, release strategies, and historical trends in Academy Awards.

## 🔍 Features Used

| Feature Name                  | Use in Model | Derived/Raw         | Notes |
|------------------------------|--------------|----------------------|-------|
| **imdb_id**                  | ❌           | Raw                  | Used only for web scraping; not included in training |
| **movie_id**                 | ❌           | Raw                  | Unique identifier — no predictive value |
| **name**                     | ✅           | Raw                  | May influence recognition/popularity; consider embeddings, word count, sentiment, or semantic features |
| **release_date**            | ❌           | Raw                  | Used to derive other features like release_month, weeks_before_oscar |
| **release_year**            | ✅           | Derived from release_date | Temporal trend or eligibility tracking |
| **release_month**           | ✅           | Derived from release_date | Captures strategic Oscar eligibility windows |
| **release_day**             | ✅           | Derived from release_date | May help with fine-grained release timing analysis |
| **oscar_date_that_year**     | ❌           | Raw                  | Used only to compute weeks_before_oscar |
| **weeks_before_oscar**       | ✅           | Derived              | Captures strategic release timing — Oscars favor Q4 releases |
| **opening_weekend_usd**      | ✅           | Raw                  | Strong early hype signal — log-transform recommended |
| **opening_week_usd**         | ❌           | Raw                  | Redundant with weekend revenue; optional |
| **total_box_office_usd**     | ✅           | Raw                  | Indicator of overall commercial success — normalize |
| **production_budget_usd**    | ✅           | Raw                  | Normalize; enables ROI-related calculations |
| **production_companies**     | ✅           | Derived (one-hot)    | May carry prestige or influence; encode accordingly |
| **production_countries**     | ✅           | Derived (one-hot)    | National origin may bias perception (e.g., foreign films less likely in Best Picture) |
| **language**                 | ✅           | Raw / Derived        | Replace `language_en`; multi-hot if multilingual — English dominance noted |
| **main_genre_encoded**       | ✅           | Derived (one-hot)    | Oscars favor drama and certain genres more |
| **side_genres_multi_encoded**| ✅           | Derived (multi-hot)  | Multi-genre blends like comedy-drama often favored |
| **runtime_minutes**          | ✅           | Raw                  | Normalize; longer films favored historically |
| **is_franchise**             | ✅           | Raw                  | Franchise/MCU sequels rarely win Best Picture |
| **based_on_existing_ip**     | ✅           | Raw                  | Adaptations (books, biographies) often help — encode as binary |
| **director_oscar_wins**      | ✅           | Raw                  | Count — strong prestige signal |
| **director_oscar_noms**      | ✅           | Raw                  | Count — reflects industry reputation |
| **actors_oscar_wins_total**  | ✅           | Raw                  | Sum of top-billed actors' wins |
| **actors_oscar_noms_total**  | ✅           | Raw                  | Sum — indicator of acting quality |
| **writer_oscar_wins**        | ✅           | Raw                  | Strong proxy for screenplay quality |
| **writer_oscar_noms**        | ✅           | Raw                  | Even nominations reflect script quality |
| **rt_score_pct**             | ✅           | Raw                  | Normalize (0–100); essential critic reception indicator |
| **imdb_rating_10**           | ✅           | Raw                  | Normalize (0–10); useful but noisier than RT |
| **mdb_rating_10**            | ✅           | Raw                  | If separate from IMDb, normalize and include |
| **imdb_votes**               | ✅           | Raw                  | Helps gauge popularity and user base trust |
| **google_trends_buzz**       | ⚠ Maybe      | Derived              | Risky: sensitive to viral, meme, or controversial noise. Needs normalization and manual quality control |

> All monetary values are normalized (log-transformed) to reduce skew. Categorical fields are one-hot or multi-hot encoded where appropriate.

## 🧠 Model

A fully connected feedforward **neural network** is trained using TensorFlow/Keras, with layers optimized for classification tasks (binary output: Oscar Win / No Win).

- **Loss Function**: Binary Crossentropy  
- **Optimizer**: Adam  
- **Evaluation Metrics**: Accuracy, Precision, Recall, AUC  

## 📁 Folder Structure

to do

## License

This project (code and documentation) is licensed under the MIT License.  
See [LICENSE](./LICENSE) for more details.

### Dataset License

The dataset used in this project — [TMDB Movies Daily Updates](https://www.kaggle.com/datasets/alanvourch/tmdb-movies-daily-updates) by Alan Vourch — is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Please note that while the code in this repository is MIT-licensed, the dataset is subject to its own license and terms of use.

---
