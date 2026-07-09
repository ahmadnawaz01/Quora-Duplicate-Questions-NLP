# 👯‍♂️ Quora Duplicate Question Pairs Detector

An end-to-end Natural Language Processing (NLP) and Machine Learning application that determines whether two questions share the same semantic intent. This project bypasses basic text vectorization by implementing advanced feature engineering (token analysis, length metrics, and fuzzy string matching) to train a highly accurate classifier.

🚀 **Live Demo:** [View the Streamlit Web App](https://quora-duplicate-questions-nlp.streamlit.app/)

---

## 📌 Project Overview

Identifying duplicate questions is a core problem for platforms like Quora, StackOverflow, and e-commerce search engines to reduce redundant content and improve user experience. 

While standard NLP pipelines rely strictly on TF-IDF or simple embeddings, this project extracts **domain-specific text features** that capture word order, string distance, and semantic overlap. These features serve as the backbone for a classification model built to pass the "human intern test."

### Key Features Implemented:
* **Token Features:** Overlap ratio, common token counts, first/last word matching, and stopword-aware token tracking.
* **Length Features:** Absolute character length difference, word count difference, and longest common substring ratios.
* **Fuzzy String Matching:** Leverages advanced heuristics inspired by the `FuzzyWuzzy` library:
  * **Simple Ratio:** Base edit-distance similarity.
  * **Partial Ratio:** Handling structural variations and substrings.
  * **Token Sort Ratio:** Alphabetically sorting tokens to bypass word-order changes (e.g., "A vs B" vs "B vs A").
  * **Token Set Ratio:** Isolatating core intersections from filler/noise words.

---

## 🛠️ Tech Stack & Libraries

* **Core Language:** Python 3.x
* **Machine Learning:** Scikit-Learn
* **Natural Language Processing:** NLTK (Natural Language Toolkit)
* **Web Interface:** Streamlit (deployed via Streamlit Community Cloud)
* **Serialization:** Pickle

---
