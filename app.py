from google import genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = "AIzaSyBOQSNwzLjowiZvl7rb5qhAR6vYzNSxwDI"
client = genai.Client(api_key=GOOGLE_API_KEY)
MODEL_ID = "gemini-2.5-flash"

@app.route('/ask-ai', methods=['POST'])
def ask_ai():
    try:
        data = request.json
        user_msg = data.get("message")
        lang = data.get("lang", "English") # Default to English
        
        income = data.get("income", "0")
        expenses = data.get("expenses", "0")
        emi = data.get("emi", "0")
        savings = data.get("savings", "0")

        # Dynamic System Instruction based on Language
        system_instruction = (
            f"You are FinSight AI, a financial expert. "
            f"IMPORTANT: You must respond ONLY in {lang}. "
            "Provide advice in a clear, bulleted list. "
            "Use bold text for important numbers. Keep it very concise."
        )

        prompt = (
            f"Context: Income {income}, Expenses {expenses}, EMI {emi}, Savings {savings}. "
            f"User says: {user_msg}"
        )

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config={'system_instruction': system_instruction}
        )
        
        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Error processing request."}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
