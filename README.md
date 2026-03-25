📌 Fake News Detection Project – CSE0001

Name: Mohit Yadav
Registration Number: [Your Reg No.]
Branch: [Your Branch]
Year: 1st Year
Course Code: CSE0001
Course Title: Digital Literacy

📖 Project Overview

This project was developed as part of the Digital Literacy course with the objective of applying machine learning techniques to solve a real-world problem. The system focuses on identifying fake news by analyzing textual data using Natural Language Processing (NLP) and classification algorithms.

In today’s fast-paced digital environment, misinformation spreads quickly, making it difficult to distinguish between real and fake content. This project explores how machine learning can automate this process and assist users in verifying news authenticity.

The project demonstrates a complete pipeline including data preprocessing, feature extraction, model training, evaluation, and prediction. It also allows users to input custom news and get real-time results.

🧩 Task Summary

This project includes the following key tasks:

Data loading and exploration
Text cleaning and preprocessing
Feature extraction using TF-IDF
Model training (Logistic Regression & Naive Bayes)
Model evaluation and comparison
Real-time prediction system
Model saving and loading
⚙️ Environment Setup & Installation

Follow these steps to set up and run the project (even if you are a beginner):

Step 1: Install Python

Download and install Python 3.x from the official website.

Verify installation:

python --version
Step 2: Create Project Folder
mkdir fake-news-project
cd fake-news-project
Step 3: Create Virtual Environment (Recommended)
python -m venv venv

Activate it:

Windows:
venv\Scripts\activate
Mac/Linux:
source venv/bin/activate
Step 4: Install Required Libraries
pip install pandas numpy matplotlib scikit-learn
Step 5: Add Dataset

Place your dataset file:

news.csv

Required columns:

title
text
Step 6: Add Source Code

Save your Python file as:

main.py
▶️ How to Run the Project
Step 1: Navigate to folder
cd fake-news-project
Step 2: Run program
python main.py
Step 3: Output

You will see:

Dataset details
Model accuracy
Confusion matrix
Classification report
Step 4: Sample Prediction
News: Government launches new scheme
Prediction: REAL ✅
Step 5: User Input
Enter news: Your news here
Step 6: Exit
Type: exit
📂 Repository Structure
fake-news-project/
│── README.md
│── news.csv
│── model.pkl
│── vectorizer.pkl
└── main.py
🧠 Concepts Used
Machine Learning
Natural Language Processing (NLP)
TF-IDF Vectorization
Logistic Regression
Naive Bayes
Data Preprocessing
🚀 Features
Automatic text cleaning
TF-IDF feature extraction
Multiple model training
Accuracy comparison
Real-time predictions
Model saving and loading
🧪 Testing & Results
Models tested on split dataset
Accuracy compared between algorithms
Logistic Regression vs Naive Bayes
Prediction function validated
🔮 Future Enhancements
Use real labeled dataset
Implement deep learning (LSTM, BERT)
Build web interface (Flask/Streamlit)
Integrate live news APIs
Improve NLP techniques
🌍 Real-World Applications
Fake news detection platforms
Social media monitoring
Fact-checking systems
News verification tools
🎓 Learning Outcomes

Through this project, students learn:

End-to-end ML pipeline
Text preprocessing techniques
Model evaluation methods
Real-world AI application
✅ Conclusion

The Fake News Detection System highlights how machine learning can be used to combat misinformation. It provides a complete, beginner-friendly implementation of text classification and serves as a strong foundation for advanced AI and NLP projects.
