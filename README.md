🌦️ Weather API — FastAPI Project
This project is a simple and fast Weather API built using FastAPI.
It retrieves real-time weather information for any city using the OpenWeatherMap API.
The API returns temperature, weather condition, and description in a clean JSON format.



🚀 Features
Get current weather by city name
Temperature in Celsius
Weather conditions (Clear, Clouds, Rain, etc.)
Detailed weather description
Very fast performance with FastAPI + Uvicorn
Safe API key handling via .env file


weather-api/
│── main.py
│── requirements.txt
│── .env
│── .gitignore


🛠 Installation
 Clone the repository
git clone https://github.com/amdoff/weather-api.git
cd weather-api

Create and activate virtual environment
macOS / Linux
python3 -m venv venv
source venv/bin/activate

Windows
python -m venv venv
venv\Scripts\activate

Install dependencies
pip install -r requirements.txt


🔑 Environment Variables
Create a .env file in the project directory and add your OpenWeather API key:
WEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
Get your API key here: https://openweathermap.org/api



▶️ Run the Server
uvicorn main:app --reload
http://127.0.0.1:8000


📡 API Usage
GET /weather?city=Tashkent


Example Response:
{
  "city": "Tashkent",
  "temperature": 14.5,
  "weather": "Clear",
  "description": "clear sky"
}


🧪 API Documentation
FastAPI provides built-in docs:
Swagger UI

Swagger UI
http://127.0.0.1:8000/docs

Redoc
http://127.0.0.1:8000/redoc


📝 Technologies Used
FastAPI
Python 3
Requests
Uvicorn
python-dotenv
OpenWeatherMap API

📄 License
MIT License — free to use and modify.

