📰 Fake News Detection System
➜ ➜ ➜ Introduction

With the rapid growth of digital media, the spread of fake news has become a serious concern. Misleading information can influence public opinion, create panic, and distort reality. This project presents a machine learning-based Fake News Detection System built using Python.

The system analyzes news content, processes textual data, and classifies it as REAL ✅ or FAKE ❌ using trained models. It uses Natural Language Processing (NLP) techniques and compares multiple algorithms to select the best-performing model.

The goal is to provide a simple, automated, and effective solution to identify unreliable news and promote trustworthy information.

📌 Real-World Problem

Fake news impacts society in multiple ways:

Spread of misinformation
Public confusion and panic
Political manipulation
Loss of trust in media
⚠️ Major Issue

Delay in identifying fake news can lead to widespread misinformation.
A reliable automated system can help detect and prevent this.

🎯 Objectives
Detect whether a news article is real or fake
Apply text preprocessing and cleaning techniques
Use TF-IDF vectorization for feature extraction
Train and compare multiple ML models
Provide real-time prediction for user input
Save and reload trained models for reuse
🛠️ Technologies Used
Python 🐍
Pandas & NumPy
Scikit-learn
Matplotlib
Regex & String Processing
Pickle (Model Saving)
⚙️ How It Works
Load dataset (news.csv)
Clean and preprocess text
Combine title + content
Convert text into numerical features using TF-IDF
Train models:
Logistic Regression
Naive Bayes
Evaluate performance
Select best model
Predict user input in real-time
📊 Features
✔ Text Cleaning & Preprocessing
✔ Data Visualization
✔ Feature Engineering (Text Length)
✔ Model Comparison
✔ Real-Time User Input Prediction
✔ Model Saving & Reloading
🧠 Machine Learning Models
🔹 Logistic Regression
High accuracy
Works well for classification
🔹 Naive Bayes
Fast and efficient
Suitable for text data

👉 The system automatically selects the best-performing model.

📈 Output Example
News: Government launches new scheme for students  
Prediction: REAL ✅
💻 How to Run
1. Clone the Repository
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
2. Install Dependencies
pip install pandas numpy scikit-learn matplotlib
3. Run the Script
python main.py
🧪 User Input

You can test your own news:

Enter news: New technology revolutionizes education  
Result: REAL ✅

Type exit to stop the program.

💾 Model Saving
Model saved as: model.pkl
Vectorizer saved as: vectorizer.pkl

These can be reused without retraining.

📂 Project Structure
📁 fake-news-detection
 ├── news.csv
 ├── main.py
 ├── model.pkl
 ├── vectorizer.pkl
 └── README.md
🚀 Future Improvements
Use real labeled datasets
Add deep learning models (LSTM, BERT)
Build a web interface (Flask/Streamlit)
Deploy as an API
✅ Conclusion

This project demonstrates how machine learning can be used to combat fake news effectively. While currently using dummy labels, it provides a strong foundation for building real-world applications.
