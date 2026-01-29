# 📩 Spam Email Detection System

## 📌 Project Overview

The Spam Detection System is a machine learning–based application that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques. The system provides real-time predictions through a simple and interactive Streamlit web interface.

---

## ✨ Key Features

* **Real-time Message Classification**
  Instantly detects whether a given message is spam or legitimate.

* **NLP-Based Text Processing**
  Uses TF-IDF vectorization to convert text into numerical features.

* **Machine Learning Model**
  Implements a stacking classifier with a tuned final estimator for improved accuracy and reduced false positives.

* **Interactive Streamlit UI**
  Clean and user-friendly interface for easy message input and result visualization.

* **Input Validation**
  Handles empty or invalid inputs gracefully.

* **Reusable Trained Model**
  Loads pre-trained model and vectorizer using pickle for fast execution.

---

## 🛠️ Technologies Used

* Python
* Scikit-learn
* NLP (TF-IDF Vectorizer)
* Streamlit
* Pickle

---

## 📂 Project Structure

```
spam-detection/
│
├── app.py
├── spam_classifier_model.sav
├── feature_extraction_model.sav
├── spamdetection.ipynb
├── dataset.csv
└── README.md
```

---

## ▶️ How to Run the Application

1. Install required dependencies:

   ```bash
   pip install streamlit scikit-learn
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Enter a message in the text box and click **Check Spam** to see the result.

---

## 📈 Future Enhancements

* Display prediction confidence score
* Explain why a message was classified as spam
* Support batch message classification

---

## 👩‍💻 Author

**Hasini**
