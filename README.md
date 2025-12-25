---
title: Fake News Detector
emoji: 📰
colorFrom: blue
colorTo: yellow
sdk: docker
app_file: app.py
pinned: false
tags:
  - flask
  - fake-news
  - nlp
  - machine-learning
---


# CWNatLatFLASK

This project runs a Flask web app for fake news detection using pre-trained models (Naive Bayes, Random Forest, SVM) and TF-IDF vectors.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CWNLP-FLASK.git
cd CWNLP-FLASK


# Create a Virtual Environment

python -m venv .venv
# Activate it:
# For macOS / Linux
source .venv/bin/activate 
# For CMD
venv\Scripts\activate.bat
# For PowerShell
.\venv\Scripts\Activate.ps1


# Install Requirements

pip install -r requirements.txt
pip freeze > requirements.txt

# If requirements.txt is missing, install manually:

pip install flask pandas numpy scikit-learn vaderSentiment joblib


# Run the App

http://127.0.0.1:5000/
