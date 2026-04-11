from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🧠 EXPLANATION ENGINE
@app.route('/explain', methods=['POST'])
def explain():
    data = request.json

    amount = float(data.get('amount', 0))
    interest = float(data.get('interest', 0))
    time = float(data.get('time', 0))

    # Simple interest calculation
    total = amount + (amount * interest * time / 100)

    explanation = f"You borrowed ₹{amount} at {interest}% for {time} months. Total repayment is ₹{round(total,2)}."

    # ⚠️ RISK ANALYZER
    risks = []
    if interest > 15:
        risks.append("High interest rate")
    if time > 60:
        risks.append("Long-term loan risk")
    if total > amount * 2:
        risks.append("You are paying double the amount")

    return jsonify({
        "explanation": explanation,
        "total": total,
        "risks": risks
    })


# 🧠 UNDERSTANDING VERIFICATION
@app.route('/verify', methods=['POST'])
def verify():
    data = request.json

    user_answer = float(data.get('answer', 0))
    actual = float(data.get('actual', 0))

    if abs(user_answer - actual) < 5:
        return jsonify({"status": "✅ Correct Understanding"})
    else:
        return jsonify({"status": "❌ Incorrect, please review"})


# 🔐 CONSENT MANAGER
@app.route('/consent', methods=['POST'])
def consent():
    data = request.json

    # In real app → store in DB
    return jsonify({
        "message": "✅ Consent Recorded Successfully"
    })


# 📊 BUDGET ANALYZER (FOR CHART DATA)
@app.route('/budget', methods=['POST'])
def budget():
    data = request.json

    income = float(data.get('income', 0))
    expenses = float(data.get('expenses', 0))

    savings = income - expenses

    return jsonify({
        "income": income,
        "expenses": expenses,
        "savings": savings
    })


# 🌍 MULTILINGUAL SUPPORT (BASIC)
@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text', '')
    lang = data.get('lang', 'en')

    translations = {
        "hi": "यह एक सरल व्याख्या है",
        "mr": "हे एक सोपे स्पष्टीकरण आहे"
    }

    return jsonify({
        "translated": translations.get(lang, text)
    })


if __name__ == '__main__':
    app.run(debug=True)
