# 💧 Water Intake Predictor

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

An intelligent **Machine Learning-powered REST API** that predicts your daily water intake requirements based on personalized factors like temperature, weight, and exercise intensity.

---

## 🎯 Features

✨ **ML-Powered Predictions** - Advanced machine learning model for accurate water intake recommendations  
🌡️ **Temperature-Aware** - Adjusts predictions based on ambient temperature  
⚖️ **Weight Consideration** - Personalizes recommendations to your body weight  
🏃 **Exercise Tracking** - Factors in physical activity duration for precise calculations  
⚡ **Fast REST API** - Built with FastAPI for high performance and easy integration  
📊 **Real-time Predictions** - Get instant recommendations with minimal latency  

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Amrutha2804/water-intake-predictor.git
cd water-intake-predictor
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

---

## 📖 API Documentation

### Endpoints

#### **POST** `/predict`
Predict daily water intake requirements

**Request Body:**
```json
{
  "temperature": 29,
  "weight_kg": 72,
  "exercise_minutes": 40
}
```

**Parameters:**
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `temperature` | float | Ambient temperature in Celsius | 25-35 |
| `weight_kg` | float | Body weight in kilograms | 50-120 |
| `exercise_minutes` | int | Duration of exercise in minutes | 0-180 |

**Response:**
```json
{
  "predicted_water_intake_liters": 3.5,
  "recommendation": "Drink approximately 3.5 liters of water daily",
  "confidence": 0.92
}
```

---

## 💻 Usage Examples

### Using cURL
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 28,
    "weight_kg": 70,
    "exercise_minutes": 45
  }'
```

### Using Python
```python
import requests

url = "http://localhost:8000/predict"
payload = {
    "temperature": 28,
    "weight_kg": 70,
    "exercise_minutes": 45
}

response = requests.post(url, json=payload)
print(response.json())
```

### Using JavaScript/Node.js
```javascript
fetch('http://localhost:8000/predict', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    temperature: 28,
    weight_kg: 70,
    exercise_minutes: 45
  })
})
.then(response => response.json())
.then(data => console.log(data))
```

---

## 🏗️ Project Structure

```
water-intake-predictor/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── models/              # ML model files
│   └── utils/               # Utility functions
├── requirements.txt         # Project dependencies
├── README.md               # Project documentation
└── .gitignore             # Git ignore rules
```

---

## 🔬 ML Model Details

The prediction model is trained on various datasets considering:
- **Temperature Impact** - Higher temperatures increase water requirements
- **Body Weight** - Heavier individuals typically need more water
- **Exercise Duration** - Physical activity increases fluid loss
- **Environmental Factors** - Humidity and activity intensity are considered

The model achieves high accuracy in predicting personalized water intake recommendations.

---

## 📋 Requirements

```
fastapi==0.95.0
uvicorn==0.21.0
pydantic==1.10.0
scikit-learn==1.2.0
numpy==1.23.0
pandas==1.5.0
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 👨‍💻 Author

**Amrutha2804**  
GitHub: [@Amrutha2804](https://github.com/Amrutha2804)

---

## 📧 Support

For issues, questions, or suggestions, please open an [GitHub Issue](https://github.com/Amrutha2804/water-intake-predictor/issues).

---

## ⭐ Show Your Support

If you found this project helpful, please consider giving it a star! ⭐

---

**Stay hydrated!**
