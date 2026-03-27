# importing libraries  
import pandas as pd
import numpy as np
import re
import string
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

print("\nLoading dataset...\n")

# reading the given data set which i store it in news.csv file 

try:
    data = pd.read_csv("news.csv")
    print("Dataset loaded successfully!\n")
# handelling error     
except:
    print("Error: news.csv not found!")
    exit()


print("First 5 rows:\n", data.head())
print("\nColumns:", data.columns)
print("\nShape:", data.shape)


print("\nMissing values:\n", data.isnull().sum())


data = data.dropna()


print("\nCombining title + text...\n")
data["content"] = data["title"] + " " + data["text"]


def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r'https?://\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

print("\nCleaning text...\n")
data["content"] = data["content"].apply(clean_text)

# my dta is unlabeled so i labeled it (dummy)
print("\nCreating dummy labels...\n")

# using random function for labeling 
np.random.seed(42)
data["label"] = np.random.randint(0, 2, size=len(data))

print("Label distribution:\n", data["label"].value_counts())

# star visulazing the given data 
print("\nPlotting label distribution...\n")

plt.figure()
data["label"].value_counts().plot(kind="bar")
plt.title("Fake vs Real (Dummy Labels)")
plt.xlabel("Label (0=Fake, 1=Real)")
plt.ylabel("Count")
plt.show()

#  TEXT LENGTH FEATURE 
print("\nAdding text length feature...\n")
 # data visulaization 
data["length"] = data["content"].apply(len)

plt.figure()
data["length"].hist(bins=50)
plt.title("Text Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.show()

# splitting the data set 
print("\nSplitting dataset...\n")

X = data["content"]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", len(X_train))
print("Test size:", len(X_test))

# vectraization 
print("\nApplying TF-IDF...\n")

vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

print("Vectorization complete!")

#  LOGISTIC REGRESSION 
print("\nTraining Logistic Regression...\n")

lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_vec, y_train)

lr_pred = lr_model.predict(X_test_vec)

print("\n=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, lr_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, lr_pred))
print("Report:\n", classification_report(y_test, lr_pred))

#  NAIVE BAYES 
print("\nTraining Naive Bayes...\n")

nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)

nb_pred = nb_model.predict(X_test_vec)

print("\n=== Naive Bayes ===")
print("Accuracy:", accuracy_score(y_test, nb_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, nb_pred))
print("Report:\n", classification_report(y_test, nb_pred))

# MODEL COMPARISON 
print("\nComparing models...\n")

lr_acc = accuracy_score(y_test, lr_pred)
nb_acc = accuracy_score(y_test, nb_pred)

print("Logistic Regression:", lr_acc)
print("Naive Bayes:", nb_acc)

best_model = lr_model if lr_acc > nb_acc else nb_model

#  PREDICTION FUNCTION
def predict_news(news):
    news = clean_text(news)
    vec = vectorizer.transform([news])
    pred = best_model.predict(vec)

    if pred[0] == 0:
        return "FAKE ❌"
    else:
        return "REAL ✅"

# SAMPLE TEST 
print("\nSample prediction:\n")

sample = "Government launches new scheme for students"
print("News:", sample)
print("Prediction:", predict_news(sample))

#  USER INPUT LOOP 
print("\nEnter your own news (type 'exit' to quit)\n")

while True:
    user_input = input("Enter news: ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    result = predict_news(user_input)
    print("Result:", result)
    print("-" * 50)

#  SAVE MODEL 
print("\nSaving model...\n")

pickle.dump(best_model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model saved successfully!")

#  LOAD MODEL (DEMO) 
print("\nReloading model for verification...\n")

loaded_model = pickle.load(open("model.pkl", "rb"))
loaded_vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

test = "Breaking news about economy growth"
vec = loaded_vectorizer.transform([test])
pred = loaded_model.predict(vec)

print("Loaded model prediction:", "REAL" if pred[0] == 1 else "FAKE")

#  END 
print("\nProject Completed Successfully!\n")