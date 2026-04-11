# FinSight 💸
### Multilingual Financial Wellness & Loan Intelligence Platform

FinSight is a hackathon project designed to help users understand and improve their financial health using AI-powered insights, multilingual assistance, EMI tracking, and instant PDF loan document summarization.

---

## 🚀 Problem Statement
Many users struggle with:
- managing multiple loans
- understanding EMI burden
- tracking expenses and savings
- reading lengthy financial documents
- accessing financial literacy in regional languages

FinSight solves this by providing an **AI-driven financial dashboard** with instant insights and document intelligence.

---

## ✨ Features
- **AI Financial Assistant** using Google Gemini API
- **Secure Sign Up / Sign In Authentication**
- **SQLite Database Integration**
- **Multilingual Support**
  - English
  - Hindi
  - Marathi
- **Income & Expense Tracking**
- **Loan EMI Calculator**
- **Net Savings Dashboard**
- **Wealth Distribution Charts**
- **Instant PDF Summarizer**
- **AI Financial Insights**
- **Interactive AI Chat Support**

---

## 📄 PDF Summarization Tech Used
### PDF.js — PDF text extraction
This is the main library used to **read and scan the uploaded PDF file directly in the browser**.

The uploaded PDF is scanned locally and the first 3 pages are extracted for quick summarization.

This ensures:
- instant speed
- no backend load
- zero API cost
- fast hackathon demo performance

---

## 🛠 Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Chart.js
- PDF.js

### Backend
- Python
- Flask
- Flask-CORS
- SQLite3

### AI / LLM
- Google Gemini 1.5 Flash API

### Security
- Werkzeug password hashing

---

## 🧠 Architecture

```text
Frontend (HTML/CSS/JS)
        ↓
    Flask Backend
        ↓
 Gemini API + SQLite DB
        ↓
 PDF.js + Chart.js
```

---

## 🔐 Authentication
Authentication is implemented using:
- **Sign Up**
- **Sign In**
- **hashed password storage**
- **SQLite database**

Passwords are securely stored using:
```python
generate_password_hash()
```

---

## 📊 Core Functionalities
### 1. Financial Dashboard
- monthly income
- other income
- rent
- food expenses
- loan EMIs
- savings percentage

---

### 2. Loan Calculator
Users can add multiple loans with:
- principal
- interest
- tenure

Automatic EMI calculation is performed.

---

### 3. AI Insights
FinSight AI provides:
- savings advice
- EMI management suggestions
- debt analysis
- financial health summary

---

### 4. PDF Loan Summarizer
Users can upload:
- loan agreements
- sanction letters
- bank documents
- repayment PDFs

The app extracts important sentences instantly.

---

## ⚙️ Setup Instructions

### Backend
```bash
pip install flask flask-cors google-generativeai werkzeug
python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

---

### Frontend
Simply open:

```text
index.html
```

in browser

OR run using Live Server in Visual Studio Code :contentReference[oaicite:2]{index=2}

---

## 🌍 Future Scope
- credit score integration
- loan risk prediction
- fraud detection
- personalized budgeting
- investment suggestions
- bank statement analysis

---

## 👨‍💻 Team / Hackathon Project
Built for hackathon demonstration with focus on:
- speed
- usability
- financial intelligence
- multilingual accessibility
