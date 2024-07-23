
# AccuWeather Scraper

The AccuWeather Scraper is a Python script that fetches and displays weather data for a specified location. It uses web scraping techniques to extract weather information from AccuWeather and other related sources. The script leverages the requests library to make HTTP requests and the BeautifulSoup library to parse HTML content.
## Authors

- [@sujalrajpoot](https://github.com/sujalrajpoot)


## Features

- Fetches current weather data for a specified location.
- Extracts detailed weather forecasts, including daily and weekly forecasts.
- Retrieves sun and moon data, including sunrise and sunset times.
- Displays air quality information and allergy outlook.
- Provides dust and dander reports.
## Usage/Examples

```python
To run the script, simply execute the Python file using your preferred Python interpreter. For example:

if __name__=="__main__":
    Place="Delhi"
    weather = AccuWeather()
    weather.Extract_Weather(Place=Place)
```
```
Output:
Weather Forecast Url: https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396
Current Weather Url: https://www.accuweather.com/en/in/delhi/202396/current-weather/202396
Fetching Data From This URL: https://www.accuweather.com/en/in/delhi/202396/weather-forecast/202396 

Today's weather on Tue, Jul 23, will be Occasional morning rain and a thunderstorm otherwise, mostly cloudy and humid, Highest Temperature will be 35°. Tonight Cloudy and humid; a thunderstorm in spots this evening followed by occasional rain and a thunderstorm late, Lowest Temperature will be 28°.

The Current Weather at 7:32 AM indicates a temperature of 29°C with a RealFeel temperature of 36°. The conditions are described as Mostly cloudy, and the wind is blowing from 35° and occasional gusts of ESE 8 km/h. Wind Speed is 20 km/h and Air quality is Poor.

Cuurently I am not able to get weather forecast data for tomorrow.

On Today, 7/23, expect day with Some rain and a thunderstorm and Some rain and a thunderstorm late night with a high of 35 Degrees Celcius and a low of 28 Degrees Celcius, along with a 60% chance of precipitation.

On Wed, 7/24, expect day with Humid with a thunderstorm in spots and Some rain and a thunderstorm late night with a high of 34 Degrees Celcius and a low of 28 Degrees Celcius, along with a 40% chance of precipitation.

On Thu, 7/25, expect day with Humid with a thunderstorm in spots and Humid a stray thunderstorm late night with a high of 36 Degrees Celcius and a low of 29 Degrees Celcius, along with a 40% chance 
of precipitation.

On Fri, 7/26, expect day with An afternoon thunderstorm or two and Humid with a stray thunderstorm night with a high of 36 Degrees Celcius and a low of 29 Degrees Celcius, along with a 87% chance of precipitation.

On Sat, 7/27, expect day with Rain and a thunderstorm and Humid a thunderstorm or two late night with a high of 34 Degrees Celcius and a low of 28 Degrees Celcius, along with a 90% chance of precipitation.

On Sun, 7/28, expect day with A couple of thunderstorms humid and Humid with a thunderstorm in spots night with a high of 33 Degrees Celcius and a low of 28 Degrees Celcius, along with a 72% chance 
of precipitation.

On Mon, 7/29, expect day with A thunderstorm in spots and Some rain and a thunderstorm late night with a high of 34 Degrees Celcius and a low of 29 Degrees Celcius, along with a 40% chance of precipitation.

On Tue, 7/30, expect day with Partly sunny, a stray thunderstorm and A stray thunderstorm early cloudy night with a high of 34 Degrees Celcius and a low of 28 Degrees Celcius, along with a 43% chance of precipitation.

On Wed, 7/31, expect day with Cloudy with a thunderstorm or two and A thunderstorm early overcast night with a high of 34 Degrees Celcius and a low of 27 Degrees Celcius, along with a 64% chance of 
precipitation.

On Thu, 8/1, expect day with Cloudy, a couple of thunderstorms and A couple of thunderstorms night with a high of 35 Degrees Celcius and a low of 28 Degrees Celcius, along with a 63% chance of precipitation.

On This Day, The Sun will be visible for 13 hrs 40 mins. It will rise at 5:38 AM and set at 7:18 PM. The moon is currently in its Waning Gibbous phase, and it will rise at 9:04 PM and set at 8:31 AM.

The Air Quality is looking like Poor, and The air has reached a high level of pollution and is unhealthy for sensitive groups. Reduce time spent outside if you are feeling symptoms such as difficulty breathing or throat irritation.

For Arthritis, Indoor Pests, Allergy Outlook & Health Activities Conditions are Very High.
For Sinus Pressure, Asthma, Allergy Outlook & Health Activities Conditions are High.
For Flu, Migraine, Allergy Outlook & Health Activities Conditions are Moderate.
For Common Cold, Allergy Outlook & Health Activities Conditions are Low.
For Beach & Pool, Allergy Outlook & Health Activities Conditions are Good.
For Running, Golf, Biking & Cycling, Stargazing, Hiking, Lawn Mowing, Allergy Outlook & Health Activities Conditions are Poor.
For Fishing, Driving, Outdoor Entertaining, Allergy Outlook & Health Activities Conditions are Fair.
For Air Travel, Composting, Allergy Outlook & Health Activities Conditions are Ideal.
For Mosquitos, Outdoor Pests, Dust & Dander, Allergy Outlook & Health Activities Conditions are Extreme.

Dust & Dander Report Saying: Dust from inside your home and the outdoors can contain pet hair and dander, mold spores, and dust mites, which can all trigger allergy symptoms. As a result, you may suffer from a runny nose, watery eyes, and sneezing.

Fetching Weather Data from This Url: https://www.accuweather.com/en/in/delhi/202396/current-weather/202396

The current temperature is 29°C with Mostly cloudy. The RealFeel temperature is 36°. Wind is blowing at ESE 8 km/h with gusts up to 20 km/h. Humidity is at 96% and indoor humidity is 95% (Dangerously Humid). The dew point is 28° C. Pressure is ↑ 1000 mb. Cloud cover is 79% and visibility is 6 km. The cloud ceiling is 9100 m.
```


## Running Tests

To run tests, run the following command

```python
python AccuWeather.py
```


## License

[MIT](https://choosealicense.com/licenses/mit/)


## Installation


```bash
Clone the repository:
git clone https://github.com/sujalrajpoot/AccuWeather.gi

Install the required packages: 
pip install requests beautifulsoup4
```
    
## 🚀 About Me
I'm a skilled Python programmer and experienced web developer. With a strong background in programming and a passion for creating interactive and engaging web experiences, I specialize in crafting dynamic websites and applications. I'm dedicated to transforming ideas into functional and user-friendly digital solutions. Explore my portfolio to see my work in action.
# Hi, I'm Sujal Rajpoot! 👋


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sujalrajpoot.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sujal-rajpoot-469888305/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sujalrajpoot70)


# Disclaimer
This project is for educational and personal use only. The script scrapes data from AccuWeather and other related sources without explicit permission from these websites. Usage of this script must comply with the terms and conditions and policies of AccuWeather and other websites being scraped.
