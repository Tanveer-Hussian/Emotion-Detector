🎭 Emotion Predictor App
🧠 Overview

Emotion Predictor is a machine learning web app that identifies the emotion behind any sentence.
Using Natural Language Processing (NLP) techniques, MultiNomial NaivesBayes and Logistic Regression model, the app predicts emotions such as joy, sadness, anger, fear, love, and surprise.
It’s built with Python, Scikit-learn, and Streamlit, offering an interactive and user-friendly interface.

🚀 Features

🗣️ Predicts the emotion from any English sentence.

🔍 Uses TF-IDF vectorization for text representation.

⚖️ Handles imbalanced data effectively using SMOTE.

🧩 Trained with Logistic Regression for high interpretability and speed.

🌐 Deployed locally using Streamlit with a clean and responsive UI.

💾 Pre-trained model and vectorizer are loaded using Pickle files.

🧩 Tech Stack
Component	Technology
Programming Language	Python
ML Algorithm	Logistic Regression
NLP Technique	TF-IDF Vectorization
Data Balancing	SMOTE (Synthetic Minority Oversampling Technique)
Web Framework	Streamlit
Libraries Used	scikit-learn, pandas, numpy, seaborn, matplotlib
🧪 Model Workflow

Data Cleaning & Preprocessing – Tokenization, stopword removal, and lowercasing.

Feature Extraction – Converting text to numeric vectors using TF-IDF.

Handling Class Imbalance – Applied SMOTE to balance emotional categories.

Model Training – Trained Logistic Regression classifier on resampled data.

Evaluation – Checked performance using accuracy, precision, recall, and confusion matrix.

Deployment – Built an interactive Streamlit app for real-time predictions.

🖥️ How to Run Locally
1. Clone the repository
git clone https://github.com/your-username/Emotion-Predictor.git
cd Emotion-Predictor

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py

4. Use the app

Type a sentence like:

“I just got a new job today!”
and get output such as:
Predicted Emotion: joy


<br> **Screenshots:** <br>
<br>
<img width="812" height="693" alt="image" src="https://github.com/user-attachments/assets/de02ae97-d14b-4754-9f93-801ec08c1197"/> 
<br>
<img width="812" height="693" alt="image" src="https://github.com/user-attachments/assets/98973ded-396b-4f91-8b55-3868b4df0bec"/>
<br>
<img width="812" height="693" alt="image" src="https://github.com/user-attachments/assets/e7fa433d-6e50-4e82-957b-36230e03ae55"/>



