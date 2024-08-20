# 📱 SMS Spam Classifier

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.10%2B-brightgreen.svg)
![NLTK](https://img.shields.io/badge/NLTK-3.8.1-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

An SMS Spam Classifier application built using Python, NLTK, and Streamlit. This project classifies SMS messages as "Spam" or "Ham" (not spam) using Natural Language Processing techniques. It provides a clean and interactive web interface to demonstrate the model's predictions.

## 🚀 Features

- **Real-Time Classification**: Input any SMS message to see instant classification as Spam or Ham.
- **Interactive Web Interface**: Built with Streamlit, offering a user-friendly and interactive experience.
- **Data Preprocessing**: Utilizes NLTK for text tokenization, stopwords removal, and text transformation.
- **Deployable**: Easily deployable on platforms like Heroku.

## 📸 Screenshots

### Home Page
![Home Page](link-to-screenshot)

### Classification Result
![Classification Result](link-to-screenshot)

## 🛠️ Technologies Used

- **Python**: Core programming language used for backend logic.
- **NLTK**: Natural Language Toolkit for preprocessing text data.
- **Streamlit**: Framework to build an interactive web application.
- **Heroku**: For deploying the application to the web.

## 💡 How It Works

1. **Data Preprocessing**: The input SMS message is tokenized, and stopwords are removed using NLTK.
2. **Feature Extraction**: The processed text is transformed into features using text vectorization techniques.
3. **Classification**: A pre-trained model classifies the SMS message as Spam or Ham.
4. **Result Display**: The classification result is displayed on the web interface in real-time.

## 📂 Project Structure

```
SMS-Spam-Classifier/
│
├── app.py                   # Main application code
├── nltk_data/               # Pre-downloaded NLTK data (stopwords, Punkt)
├── requirements.txt         # Python dependencies
├── Procfile                 # Heroku process file
└── README.md                # Project documentation (this file)
```

## ⚙️ Setup Instructions

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MUDITJAINN/SMS-Spam-Classifier.git
   cd SMS-Spam-Classifier
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK Data** (if not included):
   ```python
   import nltk
   nltk.download('stopwords', download_dir='./nltk_data')
   nltk.download('punkt', download_dir='./nltk_data')
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Deploy on Heroku** (Optional):
   ```bash
   git push heroku main
   ```

## 📈 Performance

The model is trained on a public SMS Spam dataset and evaluated using standard metrics like accuracy, precision, recall, and F1-score. The classifier performs efficiently in real-time scenarios, making it ideal for SMS filtering applications.

## 🌟 Why This Project?

This project showcases my expertise in Natural Language Processing (NLP) and web deployment, demonstrating my ability to build and deploy machine learning applications. It reflects my hands-on experience with Python, NLTK, and cloud platforms like Heroku.

## 🤝 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/MUDITJAINN/SMS-Spam-Classifier/issues).

## 📝 License

This open-source project is available under the [MIT License](LICENSE).
