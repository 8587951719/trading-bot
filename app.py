from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Trading Bot is Running!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print(f"📨 Received: {data}")
    
    # Just return success for now
    return jsonify({
        "status": "success",
        "message": "Signal received",
        "data": data
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
