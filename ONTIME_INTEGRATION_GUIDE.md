# OnTime Family App ↔ Crypto Platform Integration Guide

**Version:** 1.0  
**Last Updated:** October 29, 2025  
**For:** OnTime Mobile App Developers

> **📘 NOTE:** This document is a comprehensive API specification and integration blueprint for production deployment. The accompanying `api_server.py` file serves as a reference implementation demonstrating the API contract, authentication flow, and data structures that OnTime mobile app developers would integrate with.
> 
> **For Production Use:** Deploy the API as a separate microservice with:
> - Database persistence (PostgreSQL/MongoDB)
> - Solana blockchain integration for real token transfers
> - Proper secret management (HashiCorp Vault, AWS Secrets Manager)
> - Rate limiting and DDoS protection
> - Monitoring and logging (DataDog, Sentry)
> 
> The current demo implementation uses in-memory storage for demonstration purposes only.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Authentication](#authentication)
3. [API Endpoints](#api-endpoints)
4. [Integration Flow](#integration-flow)
5. [Code Examples](#code-examples)
6. [Testing](#testing)
7. [Security Best Practices](#security-best-practices)
8. [Support](#support)

---

## 🌟 Overview

This guide explains how to integrate the OnTime Family Planning App with the AI Crypto Empire Builder platform to enable ILAH token claiming for your users.

### Integration Benefits

- **Users earn ILAH tokens** through daily app usage
- **Automated claiming** via QR codes or manual wallet entry
- **Real-time earning tracking** with activity-based rewards
- **Secure verification** with signature-based authentication
- **Transparent revenue sharing** (60% to families, 30% operations, 10% AI)

### Architecture Diagram

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│  OnTime Mobile  │◄───────►│  ILAH API Server │◄───────►│  Solana Network │
│      App        │  HTTPS  │   (REST API)     │  Web3   │   (Blockchain)  │
└─────────────────┘         └──────────────────┘         └─────────────────┘
        │                            │
        │                            │
        ▼                            ▼
┌─────────────────┐         ┌──────────────────┐
│  User Activity  │         │  Token           │
│  Tracking       │         │  Distribution    │
└─────────────────┘         └──────────────────┘
```

---

## 🔐 Authentication

All API requests require signature-based authentication to ensure security and prevent unauthorized access.

### Authentication Flow

1. **API Key**: Each OnTime app installation receives a unique API key
2. **Timestamp**: Unix timestamp of the request (within 5 minutes)
3. **Signature**: SHA256 hash of `api_key + timestamp + secret_key`

### Generating Signatures

```python
import hashlib
import time

def generate_signature(api_key, secret_key):
    timestamp = str(int(time.time()))
    payload = f"{api_key}{timestamp}{secret_key}"
    signature = hashlib.sha256(payload.encode()).hexdigest()
    
    return {
        'api_key': api_key,
        'timestamp': timestamp,
        'signature': signature
    }
```

```javascript
// JavaScript/React Native
const crypto = require('crypto');

function generateSignature(apiKey, secretKey) {
    const timestamp = Math.floor(Date.now() / 1000).toString();
    const payload = `${apiKey}${timestamp}${secretKey}`;
    const signature = crypto.createHash('sha256').update(payload).digest('hex');
    
    return {
        apiKey,
        timestamp,
        signature
    };
}
```

---

## 🔌 API Endpoints

### Base URL

```
Production: https://ilah-api.ontimefamily.app/api/v1
Development: http://localhost:5001/api/v1
```

---

### 1. Verify User Earnings

**Endpoint:** `POST /verify-user`

Calculate how much ILAH a user has earned based on their activity.

#### Request

```json
{
    "api_key": "your_api_key_here",
    "signature": "sha256_signature",
    "timestamp": "1698585600",
    "user_id": "ontime_user_12345",
    "activity_data": {
        "days_active": 30,
        "weeks_active": 4,
        "data_quality_score": 0.85,
        "referrals": 2
    }
}
```

#### Response (Success)

```json
{
    "success": true,
    "user_id": "ontime_user_12345",
    "earned_ilah": 647.5,
    "usd_value": 272.00,
    "verified": true,
    "message": "User verified successfully"
}
```

#### Response (Error)

```json
{
    "success": false,
    "error": "Invalid signature"
}
```

---

### 2. Submit Claim Request

**Endpoint:** `POST /claim`

Submit a claim to transfer ILAH tokens to user's wallet.

#### Request

```json
{
    "api_key": "your_api_key_here",
    "signature": "sha256_signature",
    "timestamp": "1698585600",
    "user_id": "ontime_user_12345",
    "wallet_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
    "activity_data": {
        "days_active": 30,
        "weeks_active": 4,
        "data_quality_score": 0.85,
        "referrals": 2
    }
}
```

#### Response (Success)

```json
{
    "success": true,
    "claim_id": "clm_a1b2c3d4e5f6g7h8",
    "user_id": "ontime_user_12345",
    "wallet_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
    "amount_ilah": 647.5,
    "usd_value": 272.00,
    "status": "pending",
    "estimated_completion": "2025-10-30T14:30:00Z",
    "message": "Claim submitted successfully. Tokens will be transferred within 24 hours."
}
```

#### Response (Below Threshold)

```json
{
    "success": false,
    "error": "Minimum claim threshold is 100 ILAH",
    "earned_ilah": 87.5,
    "threshold": 100,
    "message": "Keep earning! Your balance will carry over to next week."
}
```

---

### 3. Check Claim Status

**Endpoint:** `GET /claim-status/{claim_id}`

Check the processing status of a submitted claim.

#### Request

```
GET /claim-status/clm_a1b2c3d4e5f6g7h8
```

#### Response (Pending)

```json
{
    "success": true,
    "claim_id": "clm_a1b2c3d4e5f6g7h8",
    "status": "pending",
    "amount_ilah": 647.5,
    "wallet_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
    "created_at": "2025-10-29T14:30:00Z",
    "estimated_completion": "2025-10-30T14:30:00Z"
}
```

#### Response (Completed)

```json
{
    "success": true,
    "claim_id": "clm_a1b2c3d4e5f6g7h8",
    "status": "completed",
    "amount_ilah": 647.5,
    "wallet_address": "7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
    "completed_at": "2025-10-29T18:45:00Z",
    "transaction_hash": "5J7kMw8N2pQrS3tU4vWxYz6A1bC8dE9fG0hI2jK3lM4nO5pQ"
}
```

---

### 4. Get Token Price

**Endpoint:** `GET /token-price`

Get current ILAH token price and market data.

#### Request

```
GET /token-price
```

#### Response

```json
{
    "success": true,
    "symbol": "ILAH",
    "price_usd": 0.42,
    "change_24h": 10.5,
    "volume_24h": 127500,
    "market_cap": 2847000,
    "timestamp": "2025-10-29T14:30:00Z"
}
```

---

### 5. API Health Check

**Endpoint:** `GET /health`

Check if the API is operational.

#### Request

```
GET /health
```

#### Response

```json
{
    "status": "healthy",
    "service": "ILAH API",
    "version": "1.0",
    "timestamp": "2025-10-29T14:30:00Z"
}
```

---

## 🔄 Integration Flow

### Step-by-Step User Journey

```
1. User completes activities in OnTime app
   ↓
2. OnTime tracks: days_active, weeks_active, quality_score, referrals
   ↓
3. User navigates to "Wallet" → "Claim ILAH"
   ↓
4. OnTime calls POST /verify-user to check earnings
   ↓
5. Display earned ILAH amount to user
   ↓
6. User enters Solana wallet address or scans QR code
   ↓
7. OnTime calls POST /claim with wallet address
   ↓
8. Display claim confirmation with claim_id
   ↓
9. Poll GET /claim-status/{claim_id} every 5 minutes
   ↓
10. Notify user when status = "completed"
    ↓
11. Show transaction_hash and success message
```

### Activity Data Calculation

```python
def calculate_user_earnings(activity_data):
    """
    Calculate ILAH earnings based on user activity
    """
    # Base earnings
    base_daily = 5  # ILAH per active day
    weekly_bonus = 50  # ILAH per active week
    monthly_bonus = 250  # ILAH if active 30+ days
    data_quality_bonus = 100  # ILAH per quality point
    
    # Extract activity data
    days_active = activity_data.get('days_active', 0)
    weeks_active = activity_data.get('weeks_active', 0)
    data_quality_score = activity_data.get('data_quality_score', 0)  # 0.0 - 1.0
    referrals = activity_data.get('referrals', 0)
    
    # Calculate total
    total_ilah = 0
    total_ilah += days_active * base_daily
    total_ilah += weeks_active * weekly_bonus
    
    if days_active >= 30:
        total_ilah += monthly_bonus
    
    total_ilah += data_quality_score * data_quality_bonus
    total_ilah += referrals * 200  # 200 ILAH per referral
    
    return round(total_ilah, 2)

# Example calculation
activity = {
    'days_active': 30,
    'weeks_active': 4,
    'data_quality_score': 0.85,
    'referrals': 2
}

earned = calculate_user_earnings(activity)
# Result: 30*5 + 4*50 + 250 + 0.85*100 + 2*200 = 150 + 200 + 250 + 85 + 400 = 1,085 ILAH
```

---

## 💻 Code Examples

### React Native / JavaScript

```javascript
// OnTime App - ILAH Integration Module

import axios from 'axios';
import { generateSignature } from './auth';

const API_BASE_URL = 'https://ilah-api.ontimefamily.app/api/v1';
const API_KEY = 'your_api_key';
const SECRET_KEY = 'your_secret_key';

class ILAHService {
    // Verify user earnings
    async verifyUserEarnings(userId, activityData) {
        try {
            const auth = generateSignature(API_KEY, SECRET_KEY);
            
            const response = await axios.post(`${API_BASE_URL}/verify-user`, {
                ...auth,
                user_id: userId,
                activity_data: activityData
            });
            
            if (response.data.success) {
                return {
                    success: true,
                    earnedILAH: response.data.earned_ilah,
                    usdValue: response.data.usd_value
                };
            }
        } catch (error) {
            console.error('Error verifying earnings:', error);
            return { success: false, error: error.message };
        }
    }
    
    // Submit claim
    async submitClaim(userId, walletAddress, activityData) {
        try {
            const auth = generateSignature(API_KEY, SECRET_KEY);
            
            const response = await axios.post(`${API_BASE_URL}/claim`, {
                ...auth,
                user_id: userId,
                wallet_address: walletAddress,
                activity_data: activityData
            });
            
            if (response.data.success) {
                return {
                    success: true,
                    claimId: response.data.claim_id,
                    amountILAH: response.data.amount_ilah,
                    status: response.data.status,
                    estimatedCompletion: response.data.estimated_completion
                };
            }
        } catch (error) {
            console.error('Error submitting claim:', error);
            return { success: false, error: error.response.data.error };
        }
    }
    
    // Check claim status
    async checkClaimStatus(claimId) {
        try {
            const response = await axios.get(`${API_BASE_URL}/claim-status/${claimId}`);
            
            if (response.data.success) {
                return {
                    success: true,
                    status: response.data.status,
                    transactionHash: response.data.transaction_hash
                };
            }
        } catch (error) {
            console.error('Error checking claim status:', error);
            return { success: false, error: error.message };
        }
    }
    
    // Get current token price
    async getTokenPrice() {
        try {
            const response = await axios.get(`${API_BASE_URL}/token-price`);
            
            if (response.data.success) {
                return {
                    success: true,
                    priceUSD: response.data.price_usd,
                    change24h: response.data.change_24h
                };
            }
        } catch (error) {
            console.error('Error getting token price:', error);
            return { success: false, error: error.message };
        }
    }
}

export default new ILAHService();
```

### Python / Flask Backend

```python
# OnTime Backend - ILAH Integration

import requests
import hashlib
import time

API_BASE_URL = 'https://ilah-api.ontimefamily.app/api/v1'
API_KEY = 'your_api_key'
SECRET_KEY = 'your_secret_key'

class ILAHClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.api_key = API_KEY
        self.secret_key = SECRET_KEY
    
    def generate_auth(self):
        """Generate authentication credentials"""
        timestamp = str(int(time.time()))
        payload = f"{self.api_key}{timestamp}{self.secret_key}"
        signature = hashlib.sha256(payload.encode()).hexdigest()
        
        return {
            'api_key': self.api_key,
            'timestamp': timestamp,
            'signature': signature
        }
    
    def verify_user_earnings(self, user_id, activity_data):
        """Verify user earnings"""
        auth = self.generate_auth()
        payload = {
            **auth,
            'user_id': user_id,
            'activity_data': activity_data
        }
        
        response = requests.post(f"{self.base_url}/verify-user", json=payload)
        return response.json()
    
    def submit_claim(self, user_id, wallet_address, activity_data):
        """Submit ILAH claim"""
        auth = self.generate_auth()
        payload = {
            **auth,
            'user_id': user_id,
            'wallet_address': wallet_address,
            'activity_data': activity_data
        }
        
        response = requests.post(f"{self.base_url}/claim", json=payload)
        return response.json()
    
    def check_claim_status(self, claim_id):
        """Check claim status"""
        response = requests.get(f"{self.base_url}/claim-status/{claim_id}")
        return response.json()

# Usage example
client = ILAHClient()

# Verify earnings
activity = {
    'days_active': 30,
    'weeks_active': 4,
    'data_quality_score': 0.85,
    'referrals': 2
}

result = client.verify_user_earnings('user_12345', activity)
print(f"User earned: {result['earned_ilah']} ILAH (${result['usd_value']})")

# Submit claim
claim = client.submit_claim(
    user_id='user_12345',
    wallet_address='7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU',
    activity_data=activity
)
print(f"Claim ID: {claim['claim_id']}, Status: {claim['status']}")
```

---

## 🧪 Testing

### Test Credentials

```
API Key: test_api_key_12345
Secret Key: test_secret_key_67890
```

### Test Users

```json
{
    "test_user_1": {
        "user_id": "test_user_001",
        "activity_data": {
            "days_active": 30,
            "weeks_active": 4,
            "data_quality_score": 0.85,
            "referrals": 2
        },
        "expected_ilah": 1085.0
    },
    "test_user_2": {
        "user_id": "test_user_002",
        "activity_data": {
            "days_active": 15,
            "weeks_active": 2,
            "data_quality_score": 0.60,
            "referrals": 0
        },
        "expected_ilah": 235.0
    }
}
```

### Testing Checklist

- [ ] Verify signature generation works correctly
- [ ] Test user verification endpoint
- [ ] Test claim submission with valid wallet
- [ ] Test claim submission with invalid wallet (should fail)
- [ ] Test claim below 100 ILAH threshold (should fail gracefully)
- [ ] Test claim status polling
- [ ] Test error handling for invalid signatures
- [ ] Test error handling for expired timestamps (>5 minutes old)
- [ ] Test rate limiting behavior
- [ ] Test concurrent claims from same user

---

## 🔒 Security Best Practices

### 1. Store Secrets Securely

```javascript
// ✅ GOOD - Use environment variables
const API_KEY = process.env.ILAH_API_KEY;
const SECRET_KEY = process.env.ILAH_SECRET_KEY;

// ❌ BAD - Hardcoded secrets
const API_KEY = 'my_api_key_12345';
```

### 2. Validate Wallet Addresses

```javascript
function isValidSolanaAddress(address) {
    // Solana addresses are 32-44 characters, base58 encoded
    const solanaRegex = /^[1-9A-HJ-NP-Za-km-z]{32,44}$/;
    return solanaRegex.test(address);
}
```

### 3. Implement Rate Limiting

```javascript
// Limit claim requests to 1 per user per hour
const lastClaimTime = await getLastClaimTime(userId);
const ONE_HOUR = 60 * 60 * 1000;

if (Date.now() - lastClaimTime < ONE_HOUR) {
    throw new Error('Please wait 1 hour between claims');
}
```

### 4. Sanitize User Input

```python
def sanitize_user_id(user_id):
    """Remove dangerous characters from user_id"""
    import re
    return re.sub(r'[^a-zA-Z0-9_-]', '', user_id)
```

### 5. Handle Errors Gracefully

```javascript
try {
    const result = await ilahService.submitClaim(userId, wallet, activity);
    if (result.success) {
        showSuccessMessage(result);
    } else {
        showErrorMessage(result.error);
    }
} catch (error) {
    // Log error for debugging
    console.error('Claim error:', error);
    
    // Show user-friendly message
    showErrorMessage('Unable to submit claim. Please try again later.');
    
    // Report to error tracking service
    reportError(error);
}
```

---

## 📞 Support

### Technical Support

- **Email**: dev-support@ontimefamily.app
- **Slack**: #ilah-integration
- **Documentation**: https://docs.ontimefamily.app/ilah

### API Status

- **Status Page**: https://status.ilah-api.ontimefamily.app
- **Uptime**: 99.9% SLA
- **Support Hours**: 24/7

### Rate Limits

| Endpoint | Limit |
|----------|-------|
| POST /verify-user | 100 requests/minute |
| POST /claim | 10 requests/minute |
| GET /claim-status | 1000 requests/minute |
| GET /token-price | Unlimited |
| GET /health | Unlimited |

### Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Missing or invalid parameters |
| 401 | Unauthorized - Invalid signature or expired timestamp |
| 404 | Not Found - Claim ID not found |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - Contact support |

---

## 📚 Additional Resources

- [ILAH Token Whitepaper](https://docs.ontimefamily.app/ilah-whitepaper.pdf)
- [Solana Wallet Integration Guide](https://docs.solana.com/wallet-guide)
- [Privacy & Security Documentation](https://docs.ontimefamily.app/privacy)
- [Revenue Sharing Model](https://docs.ontimefamily.app/revenue-model)

---

**Last Updated:** October 29, 2025  
**Version:** 1.0  
**Maintainer:** AI Crypto Empire Builder Team
