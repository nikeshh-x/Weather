Weather App
A simple Django web application to display current weather information for any city using the OpenWeatherMap API.

Features
Search weather by city name
Displays temperature, weather condition, and icon
Responsive UI with custom CSS

Project Structure
weatherproject - Django project settings and URLs
weatherapp/ - Main app with views, URLs, and templates
style.css - Custom styles
index.html - Main page template


Setup Instructions
1. Clone the repository : git clone https://github.com/nikeshh-x/Weather.git
  cd Weather
2. Install dependencies : pip install django requests
3. Run Migrations : python manage.py migrate
4. Start the development server : python manage.py runserver
5. Access the app : Open your browser and go to http://127.0.0.1:8000/

Configuration
The app uses OpenWeatherMap API. You can change the API key in views.py.
Default city is Kathmandu.
License
This project is licensed under the MIT License.
