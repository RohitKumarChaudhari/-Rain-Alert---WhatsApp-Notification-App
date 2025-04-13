# ☔ Rain Alert - WhatsApp Notification App

This is a simple API-based Python program that checks weather data using the **OpenWeatherMap API** and sends a **rain alert message via WhatsApp** using the **Twilio API**.

---

## 🚀 Features
- Uses OpenWeatherMap API to fetch hourly weather forecast
- Sends a WhatsApp message alert if rain is predicted
- Built with Python and easy to configure
- Can be scheduled to run daily

---

## 🛠 Technologies Used
- Python
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp/api)
- `requests` module

---


---

## 🔐 Environment Variables / Secrets

You need to set the following environment variables (locally or using GitHub Secrets):

| Variable Name      | Description                      |
|--------------------|----------------------------------|
| `OWM_API_KEY`       | Your OpenWeatherMap API key     |
| `TWILIO_SID`        | Twilio Account SID              |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token               |
| `FROM_WHATSAPP`     | Twilio WhatsApp-enabled number  |
| `TO_WHATSAPP`       | Your personal WhatsApp number   |
| `LAT`               | Latitude of location            |
| `LON`               | Longitude of location           |

---

## 📦 Installation & Setup
```bash
git clone https://github.com/your-username/rain_alert.git
cd rain_alert
pip install -r requirements.txt
```
✅ Usage  
Run the script:
```bash
python main.py
```
If there's rain in the forecast, you'll get a message like:
"🌧️ Heads up! It might rain today. Take an umbrella ☔"  

📚 API Sources  
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp/api)

📌 Notes
-  Make sure your Twilio number is approved for WhatsApp messaging.
-  You must verify your WhatsApp number on Twilio (in trial mode).

🧾 License
This project is open-source and free to use under the MIT License.  

📬 Made with 💙 by Rohit
    
