"""
ILAH Token Distribution API - Blueprint/Specification

NOTE: This is a reference implementation and API specification.
In a production environment, this would be deployed as a separate service
with proper database persistence, secret management, and blockchain integration.

For development/demo purposes on Replit, this file serves as documentation
of the API contract that OnTime mobile app developers would integrate with.

To use in production:
1. Deploy this as a separate microservice (not on Replit's port 5000)
2. Set ILAH_API_SECRET environment variable
3. Implement database persistence (replace in-memory dicts)
4. Add Solana blockchain integration for actual token transfers
5. Implement proper claim processing workflow
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import secrets
import time
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)

API_SECRET = os.getenv('ILAH_API_SECRET')
if not API_SECRET:
    raise ValueError("ILAH_API_SECRET environment variable must be set for production use")

class ILAHClaimManager:
    def __init__(self):
        self.pending_claims = {}
        self.processed_claims = {}
    
    def verify_ontime_request(self, api_key, signature, timestamp):
        """Verify the request is from legitimate OnTime app"""
        if abs(time.time() - float(timestamp)) > 300:
            return False, "Request timestamp too old (> 5 minutes)"
        
        expected_signature = hashlib.sha256(
            f"{api_key}{timestamp}{API_SECRET}".encode()
        ).hexdigest()
        
        if signature != expected_signature:
            return False, "Invalid signature"
        
        return True, "Verified"
    
    def calculate_user_earnings(self, user_id, activity_data):
        """Calculate ILAH earnings based on user activity"""
        base_daily = 5
        weekly_bonus = 50
        monthly_bonus = 250
        data_quality_bonus = 100
        
        days_active = activity_data.get('days_active', 0)
        weeks_active = activity_data.get('weeks_active', 0)
        data_quality_score = activity_data.get('data_quality_score', 0)
        
        total_ilah = 0
        total_ilah += days_active * base_daily
        total_ilah += weeks_active * weekly_bonus
        
        if days_active >= 30:
            total_ilah += monthly_bonus
        
        total_ilah += data_quality_score * data_quality_bonus
        
        referrals = activity_data.get('referrals', 0)
        total_ilah += referrals * 200
        
        return round(total_ilah, 2)
    
    def submit_claim(self, user_id, wallet_address, earned_ilah):
        """Submit a claim for processing"""
        claim_id = secrets.token_hex(16)
        
        self.pending_claims[claim_id] = {
            'user_id': user_id,
            'wallet_address': wallet_address,
            'amount_ilah': earned_ilah,
            'status': 'pending',
            'created_at': datetime.now().isoformat(),
            'estimated_completion': (datetime.now() + timedelta(hours=24)).isoformat()
        }
        
        return claim_id

claim_manager = ILAHClaimManager()

@app.route('/')
def index():
    """API health check"""
    return jsonify({
        'service': 'ILAH Token API',
        'status': 'operational',
        'version': '1.0',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/v1/verify-user', methods=['POST'])
def verify_user():
    """
    Verify OnTime user and calculate earned ILAH
    
    Expected payload:
    {
        "api_key": "ontime_api_key",
        "signature": "sha256_signature",
        "timestamp": "unix_timestamp",
        "user_id": "ontime_user_id",
        "activity_data": {
            "days_active": 30,
            "weeks_active": 4,
            "data_quality_score": 0.85,
            "referrals": 2
        }
    }
    """
    try:
        data = request.json
        
        api_key = data.get('api_key')
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        user_id = data.get('user_id')
        activity_data = data.get('activity_data', {})
        
        if not all([api_key, signature, timestamp, user_id]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400
        
        verified, message = claim_manager.verify_ontime_request(api_key, signature, timestamp)
        
        if not verified:
            return jsonify({
                'success': False,
                'error': message
            }), 401
        
        earned_ilah = claim_manager.calculate_user_earnings(user_id, activity_data)
        
        return jsonify({
            'success': True,
            'user_id': user_id,
            'earned_ilah': earned_ilah,
            'usd_value': round(earned_ilah * 0.42, 2),
            'verified': True,
            'message': 'User verified successfully'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/v1/claim', methods=['POST'])
def submit_claim():
    """
    Submit ILAH claim request
    
    Expected payload:
    {
        "api_key": "ontime_api_key",
        "signature": "sha256_signature",
        "timestamp": "unix_timestamp",
        "user_id": "ontime_user_id",
        "wallet_address": "solana_wallet_address",
        "activity_data": {
            "days_active": 30,
            "weeks_active": 4,
            "data_quality_score": 0.85,
            "referrals": 2
        }
    }
    """
    try:
        data = request.json
        
        api_key = data.get('api_key')
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        user_id = data.get('user_id')
        wallet_address = data.get('wallet_address')
        activity_data = data.get('activity_data', {})
        
        if not all([api_key, signature, timestamp, user_id, wallet_address]):
            return jsonify({
                'success': False,
                'error': 'Missing required fields'
            }), 400
        
        if not wallet_address or len(wallet_address) < 32:
            return jsonify({
                'success': False,
                'error': 'Invalid Solana wallet address'
            }), 400
        
        verified, message = claim_manager.verify_ontime_request(api_key, signature, timestamp)
        
        if not verified:
            return jsonify({
                'success': False,
                'error': message
            }), 401
        
        earned_ilah = claim_manager.calculate_user_earnings(user_id, activity_data)
        
        if earned_ilah < 100:
            return jsonify({
                'success': False,
                'error': 'Minimum claim threshold is 100 ILAH',
                'earned_ilah': earned_ilah,
                'threshold': 100,
                'message': 'Keep earning! Your balance will carry over to next week.'
            }), 400
        
        claim_id = claim_manager.submit_claim(user_id, wallet_address, earned_ilah)
        
        return jsonify({
            'success': True,
            'claim_id': claim_id,
            'user_id': user_id,
            'wallet_address': wallet_address,
            'amount_ilah': earned_ilah,
            'usd_value': round(earned_ilah * 0.42, 2),
            'status': 'pending',
            'estimated_completion': claim_manager.pending_claims[claim_id]['estimated_completion'],
            'message': 'Claim submitted successfully. Tokens will be transferred within 24 hours.'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/v1/claim-status/<claim_id>', methods=['GET'])
def check_claim_status(claim_id):
    """Check the status of a claim"""
    try:
        if claim_id in claim_manager.pending_claims:
            claim = claim_manager.pending_claims[claim_id]
            return jsonify({
                'success': True,
                'claim_id': claim_id,
                'status': claim['status'],
                'amount_ilah': claim['amount_ilah'],
                'wallet_address': claim['wallet_address'],
                'created_at': claim['created_at'],
                'estimated_completion': claim['estimated_completion']
            })
        elif claim_id in claim_manager.processed_claims:
            claim = claim_manager.processed_claims[claim_id]
            return jsonify({
                'success': True,
                'claim_id': claim_id,
                'status': 'completed',
                'amount_ilah': claim['amount_ilah'],
                'wallet_address': claim['wallet_address'],
                'completed_at': claim['completed_at'],
                'transaction_hash': claim.get('tx_hash', 'N/A')
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Claim not found'
            }), 404
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/v1/token-price', methods=['GET'])
def get_token_price():
    """Get current ILAH token price"""
    return jsonify({
        'success': True,
        'symbol': 'ILAH',
        'price_usd': 0.42,
        'change_24h': 10.5,
        'volume_24h': 127500,
        'market_cap': 2847000,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'ILAH API',
        'version': '1.0',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/v1/docs', methods=['GET'])
def api_documentation():
    """API documentation"""
    return jsonify({
        'api_name': 'ILAH Token Distribution API',
        'version': '1.0',
        'description': 'API for OnTime Family App to verify users and distribute ILAH tokens',
        'base_url': request.host_url + 'api/v1',
        'endpoints': {
            'verify_user': {
                'method': 'POST',
                'path': '/verify-user',
                'description': 'Verify OnTime user and calculate earned ILAH',
                'auth': 'API key + signature required'
            },
            'submit_claim': {
                'method': 'POST',
                'path': '/claim',
                'description': 'Submit ILAH claim request',
                'auth': 'API key + signature required'
            },
            'check_status': {
                'method': 'GET',
                'path': '/claim-status/<claim_id>',
                'description': 'Check claim processing status',
                'auth': 'None'
            },
            'token_price': {
                'method': 'GET',
                'path': '/token-price',
                'description': 'Get current ILAH token price',
                'auth': 'None'
            },
            'health': {
                'method': 'GET',
                'path': '/health',
                'description': 'API health check',
                'auth': 'None'
            }
        },
        'authentication': {
            'type': 'signature-based',
            'description': 'Requests must include api_key, timestamp, and sha256 signature',
            'signature_formula': 'SHA256(api_key + timestamp + secret)'
        },
        'rate_limits': {
            'verify_user': '100 requests/minute',
            'submit_claim': '10 requests/minute',
            'check_status': '1000 requests/minute'
        }
    })

if __name__ == '__main__':
    port = int(os.getenv('API_PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True)
