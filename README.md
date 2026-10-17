# 🌦️ Weather App

A desktop weather application built using Python and PyQt5 that fetches current weather information using the OpenWeatherMap API.

## Features

- Search for weather by city name
- Display temperature in Celsius
- Show weather descriptions and emojis
- Handle API errors and connection issues
- Simple and clean graphical interface

## Requirements

- Python 3
- Git
- An OpenWeatherMap API key

## Installation and Setup

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/Samrudh-081808/Weather-API.git
```

Navigate into the project folder:

```bash
 cd '.\Weather API\'
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Obtain an API Key

Create an account on [OpenWeatherMap](https://home.openweathermap.org/api_keys) and obtain your API key.

### 4. Configure Environment Variables

Create a file named `.env` in the project folder.

Copy the contents of `.env.example` into `.env` and replace the placeholder with your API key:

```env
WEATHER_API_KEY=your_actual_api_key
```



### 5. Run the Application

Run the Python file:

```bash
python main.py
```

## Technologies Used

- Python
- PyQt5
- Requests
- OpenWeatherMap API
- python-dotenv

## License

This project is available for learning and personal use.
