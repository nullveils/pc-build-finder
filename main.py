from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from data import get_build_recommendation, get_all_games, get_game_info, CURRENCY_SYMBOLS, CURRENCY_NAMES, EXCHANGE_RATES
import traceback

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Basic error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/currencies', methods=['GET'])
def currencies():
    """Return available currencies and exchange rates"""
    try:
        currencies_data = {
            "currencies": [
                {"code": "EUR", "name": CURRENCY_NAMES["EUR"], "symbol": CURRENCY_SYMBOLS["EUR"]},
                {"code": "USD", "name": CURRENCY_NAMES["USD"], "symbol": CURRENCY_SYMBOLS["USD"]},
                {"code": "CAD", "name": CURRENCY_NAMES["CAD"], "symbol": CURRENCY_SYMBOLS["CAD"]},
            ],
            "exchange_rates": EXCHANGE_RATES,
            "default": "EUR"
        }
        return jsonify(currencies_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/games', methods=['GET'])
def games_list():
    """Return list of all available games"""
    try:
        games = get_all_games()
        return jsonify({"games": games, "total": len(games)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/game-info/<game_name>', methods=['GET'])
def game_info(game_name):
    """Get info about a specific game"""
    try:
        info = get_game_info(game_name)
        if not info:
            return jsonify({"error": f"Game '{game_name}' not found"}), 404
        return jsonify(info)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/recommend', methods=['POST', 'OPTIONS'])
def recommend():
    """Generate PC build recommendation with currency support"""
    try:
        # Handle CORS preflight
        if request.method == 'OPTIONS':
            return '', 204
        
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        budget = float(data.get('budget', 0))
        games = data.get('games', '').lower().split(',')
        currency = data.get('currency', 'EUR').upper()
        
        # Validate currency
        if currency not in EXCHANGE_RATES:
            return jsonify({'error': f'Invalid currency. Use: {", ".join(EXCHANGE_RATES.keys())}'}), 400
        
        games = [g.strip() for g in games if g.strip()]
        
        # Validation
        min_budget_eur = 300
        max_budget_eur = 50000
        min_budget = min_budget_eur * EXCHANGE_RATES[currency]
        max_budget = max_budget_eur * EXCHANGE_RATES[currency]
        
        if budget < min_budget:
            return jsonify({
                'error': f'Budget too low. Minimum {CURRENCY_SYMBOLS[currency]}{min_budget:.2f}'
            }), 400
        if budget > max_budget:
            return jsonify({
                'error': f'Budget too high. Maximum {CURRENCY_SYMBOLS[currency]}{max_budget:.2f}'
            }), 400
        if not games:
            return jsonify({'error': 'Please enter at least one game'}), 400
        
        # Generate build
        build = get_build_recommendation(budget, games, currency)
        return jsonify(build)
    
    except ValueError as e:
        return jsonify({'error': f'Invalid budget. Please enter a valid number: {str(e)}'}), 400
    except Exception as e:
        print(f"Error in /api/recommend: {str(e)}")
        print(traceback.format_exc())
        return jsonify({'error': f'Error generating build: {str(e)}'}), 500

@app.route('/api/build-tiers', methods=['GET'])
def build_tiers():
    """Return info about build tiers"""
    currency = request.args.get('currency', 'EUR').upper()
    
    if currency not in EXCHANGE_RATES:
        currency = 'EUR'
    
    rate = EXCHANGE_RATES[currency]
    symbol = CURRENCY_SYMBOLS[currency]
    
    tiers = {
        "low": {
            "budget_range": f"{symbol}{300*rate:.0f} - {symbol}{700*rate:.0f}",
            "use_case": "Esports games, casual play, light work",
            "performance": "60+ FPS at 1080p low-medium settings"
        },
        "medium": {
            "budget_range": f"{symbol}{700*rate:.0f} - {symbol}{1500*rate:.0f}",
            "use_case": "AAA games, streaming, content creation",
            "performance": "60-100+ FPS at 1440p high settings"
        },
        "high": {
            "budget_range": f"{symbol}{1500*rate:.0f}+",
            "use_case": "Demanding AAA games, 4K gaming, professional work",
            "performance": "60+ FPS at 4K or 120+ FPS at 1440p ultra settings"
        }
    }
    return jsonify(tiers)

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint for deployment"""
    return jsonify({"status": "ok", "version": "1.0.0"})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)