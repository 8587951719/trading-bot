from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Store orders in memory (for demo)
orders = []

@app.route('/')
def home():
    return """
    <h1>Trading Bot is Running!</h1>
    <p>Endpoints:</p>
    <ul>
        <li><b>GET /health</b> - Check status</li>
        <li><b>POST /webhook</b> - TradingView alerts</li>
        <li><b>GET /orders</b> - View orders</li>
    </ul>
    """

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "Trading Bot"})

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"Received webhook: {data}")
        
        # Validate required fields
        action = data.get('action', '').upper()
        symbol = data.get('symbol', 'GOLDM')
        quantity = data.get('quantity', 1)
        
        # Simulate order placement (for now)
        order_id = f"SIM_{len(orders) + 1}"
        order = {
            'id': order_id,
            'action': action,
            'symbol': symbol,
            'quantity': quantity,
            'status': 'simulated'
        }
        orders.append(order)
        
        return jsonify({
            "success": True,
            "order": order,
            "message": "Order simulated (not real)"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/orders')
def get_orders():
    return jsonify({
        "total": len(orders),
        "orders": orders
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
