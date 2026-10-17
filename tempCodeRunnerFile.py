import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QLineEdit, QVBoxLayout)
from PyQt5.QtCore import Qt


class WeatherAPP(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter a City",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.desc_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 600)
        
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")
        self.setObjectName("WeatherAPP")

        self.setStyleSheet(
            """QLabel, QPushButton{
                        font-family : Arial;
            }
            
            QLabel#city_label{
                        font-size : 42px;
                        font-weight : bold;
                        color : #19324D;
            }
            
            QLineEdit#city_input{
                        font-size : 24px;
                        padding: 10px;
                        border: 2px solid #D5E6F7;
                        border-radius: 10px;
                        background-color: white;
                        color: #19324D;
            }

            QLineEdit#city_input::placeholder {
                        color: #8AA2BA;
                        font-style: italic;
            }
            
            QPushButton{
                        font-size : 22px;
                        padding: 10px;
                        border: none;
                        border-radius: 10px;
                        background-color: #2878D0;
                        color: white ;
                        font-weight: bold;
            }

            QPushButton:hover {
                        background-color: #1E65B0;
            }

            QPushButton:pressed {
                        background-color: #174F8A;
            }
            
            QLabel#temp_label{
                        font-size : 72px;
                        color: #19324D;
                        }
            QLabel#emoji_label{
                        font-size : 90px;
                        font-family : Segoe UI Emoji;
                        }
                        
            QLabel#desc_label{
                        font-size : 32px;
                        color: #19324D; 
                        }
                        
            QWidget#WeatherAPP {
                        background-color: #EAF4FF;
                        }"""
        )

        self.get_weather_button.clicked.connect(self.getWeather)

    def getWeather(self):
        api_key = "bfd38049b59d707c835d3f9ee11eeba0"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status() # for try block
            data = response.json()
            print(data)

            
            if data["cod"] == 200:
                self.display_weather_data(data)

        except requests.exceptions.HTTPError:
               match response.status_code:
                    case 400:
                        self.display_error("Bad request:\nPlease check your input")
                    case 401:
                        self.display_error("Unauthorized:\nInvalid API key")
                    case 403:
                        self.display_error("Forbidden:\nAccess is denied")
                    case 404:
                        self.display_error("Not found:\nCity not found")
                    case 500:
                        self.display_error("Internal Server Error:\nPlease try again later")
                    case 502:
                        self.display_error("Bad Gateway:\nInvalid response from the server")
                    case 503:
                        self.display_error("Service Unavailable:\nServer is down")
                    case 504:
                        self.display_error("Gateway Timeout:\nNo response from the server")
                    case _:
                        self.display_error(f"Unexpected status code: {response.status_code}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")


    def display_error(self, msg):
        self.temp_label.setText(msg)
        self.temp_label.setStyleSheet("font-size: 18px;")
        self.emoji_label.setText("🤕")
        self.emoji_label.setStyleSheet("font-size: 30px;")

    def display_weather_data(self, data):
        temp_k = data["main"]["temp"]
        temp_c = temp_k - 273.15

        self.temp_label.setText(f"{temp_c:.0f}°C")
        self.temp_label.setStyleSheet("font-size: 80px;")

        weather_emoji_desc = data["weather"][0]['description']
        self.desc_label.setText(f"{weather_emoji_desc}".capitalize())
        weather_id = data["weather"][0]["id"]

        self.emoji_label.setText(self.display_emoji(weather_id))
        self.emoji_label.setStyleSheet("font-size: 100px;")

    @staticmethod
    def display_emoji(weather_id):
        if 200 <= weather_id <= 299:
            return "⛈️"
        elif 300 <= weather_id <= 399:
            return "🌧️"
        elif 500 <= weather_id <= 599:
            return "💧"
        elif 600 <= weather_id <= 699:
            return "❄️"
        elif 701 <= weather_id <= 781:
            return "🌫️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return "✨"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weatherapp = WeatherAPP()
    weatherapp.show()
    sys.exit(app.exec_())

