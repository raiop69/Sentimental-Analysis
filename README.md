# Sentiment Analysis and Emotion Detection using NLP

## About the Project

This is my first Natural Language Processing (NLP) project, developed after completing my NLP using Machine Learning course. The project uses machine learning techniques to analyze text and predict the emotion expressed in a sentence.

I worked with a text and emotion dataset, performed text preprocessing and vectorization, and trained multiple machine learning models. After evaluating their performance, Logistic Regression achieved **86% accuracy**, making it my selected model for the final application.

I also developed a user-friendly web interface using Streamlit, allowing users to enter a sentence and receive an emotion prediction.

## Features

- Predict emotions from user-input text.
- Text preprocessing and feature extraction.
- Text vectorization for machine learning.
- Training and comparison of multiple ML models.
- Model evaluation using accuracy and other metrics.
- Interactive web interface built with Streamlit.
- Best-performing model achieved 86% accuracy.

## Technologies Used

- **Python** — Programming language
- **Pandas and NumPy** — Data processing
- **Scikit-learn** — Machine learning and model evaluation
- **Natural Language Processing (NLP)** — Text processing
- **TF-IDF / Text Vectorization** — Converting text into numerical features, if used in your implementation
- **Naive Bayes** — Classification model
- **Logistic Regression** — Selected classification model
- **Streamlit** — Web application interface
- **Joblib** — Saving and loading the trained model

## Machine Learning Models

I trained and compared multiple classification models, including:

1. Naive Bayes
2. Logistic Regression

Logistic Regression achieved **86% accuracy** on my evaluation data, so I selected it for the final application.

## Project Structure

```text
Sentiment-Analysis/
│
├── app.py                 # Streamlit application
├── model_training.py      # Model training script (if included)
├── model.pkl              # Saved trained model (example filename)
├── vectorizer.pkl         # Saved text vectorizer (example filename)
├── requirements.txt       # Project dependencies
├── dataset.csv            # Dataset (if included)
└── README.md              # Project documentation
```

*Note: Update the filenames above to match your actual repository. Only include files that exist in your project.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Sentiment-Analysis
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file yet, you can install the main dependencies using:

```bash
pip install streamlit pandas numpy scikit-learn joblib
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser. Enter a sentence in the input field to get an emotion prediction.

## Model Performance

| Metric | Result |
|---|---|
| Selected Model | Logistic Regression |
| Accuracy | 86% |
| Task | Text Emotion Classification |

*Accuracy is based on my evaluation results. Actual performance may vary depending on the dataset and input text.*

## Learning Outcomes

Through this project, I gained practical experience in:

- Text preprocessing and cleaning.
- Converting text into numerical features.
- Training and comparing machine learning models.
- Evaluating classification performance.
- Saving and loading trained models.
- Integrating a machine learning model into a Streamlit application.

## Future Improvements

- Experiment with additional machine learning models.
- Improve performance through hyperparameter tuning.
- Test different text vectorization techniques.
- Improve the frontend design and user experience.
- Explore advanced NLP approaches for better emotion classification.

## Acknowledgements

This project was developed as part of my learning journey in Natural Language Processing and Machine Learning. It represents my first practical NLP project and an important step toward building more advanced AI applications.

## Author

**Rai Amanullah**

- GitHub: https://github.com/raiop69/
- LinkedIn: https://linkedin.com/in/raiamanullah/

---

If you find this project interesting, feel free to explore the repository!
