import requests
from bs4 import BeautifulSoup

class AccuWeather:
    """
    AccuWeather class provides functionality to extract weather information for a given place
    by scraping data from Google search results and AccuWeather website.

    Methods:
        Extract_Weather(Place: str): Extracts and prints weather forecast and current weather URLs
        from Google search results for the specified place. Fetches and processes weather data
        from the AccuWeather website.
    """
    def Extract_Weather(self, Place:str):
        """
        Extracts and prints weather forecast and current weather URLs from Google search results for the specified place.
        Fetches and processes weather data from the AccuWeather website.

        Args:
            Place (str): The name of the place for which to extract weather information.

        Returns:
            None
        """
        # URL to search weather for given place
        url = f"https://www.google.com/search?q=weather+in+{Place}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        try:
            weather_forecast_url = None
            # Create a session
            session = requests.Session()

            _ = session.get(url=url, headers=headers, timeout=None)
            soup = BeautifulSoup(_.content, "html.parser")

            # Finding all links
            links = soup.findAll("a")
            for link in links:
                if "www.accuweather.com" and "/weather-forecast/" in str(link).lower():
                    weather_forecast_url = link['href']
                    print(f"Weather Forecast Url: {weather_forecast_url}")
                if "www.accuweather.com" and "/current-weather/" in str(link).lower():
                    current_weather_url = link['href']
                    print(f"Current Weather Url: {current_weather_url}")
                else:pass

            # If AccuWeather URL is found, process it
            if weather_forecast_url is not None:
                print("Fetching Data From This URL:",weather_forecast_url, "\n")
                weather_url_response = requests.get(weather_forecast_url, headers=headers, timeout=None)

                if weather_url_response.status_code == 200:
                    weather_url_soup = BeautifulSoup(weather_url_response.content, 'html.parser')
                    
                    # Extracting the div with class 'today-forecast-card content-module'
                    div_content = weather_url_soup.find("div", class_="today-forecast-card content-module")
                    if div_content:
                        # Extract date
                        date = div_content.find("p", class_="sub").get_text(strip=True)
                        
                        # Extract the weather details
                        body_items = div_content.findAll("div", class_="body-item")
                        morning_weather = body_items[0].get_text(strip=True)
                        night_weather = body_items[1].get_text(strip=True)
                        
                        # Ensure spaces between conditions and temperatures
                        morning_weather = morning_weather.replace("Hi:", ", Highest Temperature will be").replace(";", "")
                        night_weather = night_weather.replace("Lo:", ", Lowest Temperature will be").replace("Tonight:", "Tonight")
                        
                        # Format the output
                        formatted_output = f"Today's weather on {date}, will be {morning_weather}. {night_weather}.\n"
                        
                        print(formatted_output)
                    else:
                        print("Div with class 'today-forecast-card content-module' not found.")
                    
                    # Find the weather card element
                    weather_card = weather_url_soup.find('a', class_='cur-con-weather-card')

                    # Extract the desired data
                    if weather_card:
                        # Current Weather Title
                        title = weather_card.find('h2', class_='cur-con-weather-card__title').text.strip()
                        
                        # Time
                        time = weather_card.find('p', class_='cur-con-weather-card__subtitle').text.strip()
                        
                        # Temperature
                        temperature = weather_card.find('div', class_='temp').text.strip()
                        
                        # RealFeel Temperature
                        real_feel = weather_card.find('div', class_='real-feel').text.strip().replace('RealFeel®', '').strip()
                        
                        # Weather Description
                        description = weather_card.find('span', class_='phrase').text.strip()
                        
                        # Wind
                        wind = weather_card.find_all('div', class_='spaced-content detail')[0].find('span', class_='value').text.strip()
                        
                        # Wind Gusts
                        wind_gusts = weather_card.find_all('div', class_='spaced-content detail')[1].find('span', class_='value').text.strip()
                        
                        # Air Quality
                        wind_speed = weather_card.find_all('div', class_='spaced-content detail')[2].find('span', class_='value').text.strip()

                        air_quality = weather_url_soup.find('span', class_='label', string='Air Quality').find_next('span', class_='value').text.strip()

                        print(f"The {title} at {time} indicates a temperature of {temperature} with a RealFeel temperature of {real_feel}. The conditions are described as {description}, and the wind is blowing from {wind} and occasional gusts of {wind_gusts}. Wind Speed is {wind_speed} and Air quality is {air_quality}.\n")

                    else:print("Weather card not found")

                    # Extract Looking Ahead Data
                    forecast_element = weather_url_soup.find('a', class_='local-forecast-summary')
                    if forecast_element:
                        # Extract the required pieces of data
                        p_text = forecast_element.find('p').text
                        print("Tomorrow's Weather Prediction:", p_text, "\n")
                    else:print("Cuurently I am not able to get weather forecast data for tomorrow.\n")

                    # Find the daily weather forecast section
                    daily_list = weather_url_soup.find('div', class_='daily-list content-module')

                    # Extract individual daily forecast items
                    forecast_items = daily_list.find_all('a', class_='daily-list-item')

                    # Iterate over each forecast item and extract the required data
                    for item in forecast_items:
                        day = item.find('p', class_='day').text
                        date = item.find('div', class_='date').find_all('p')[1].text
                        temp_hi = (item.find('span', class_='temp-hi').text).replace("°", " Degrees Celcius")
                        temp_lo = str(item.find('span', class_='temp-lo').text).replace("Lo", "Not expected temperature").replace("°", " Degrees Celcius")
                        day_phrase = str(item.find('div', class_='phrase').find_all('p')[0].text).replace("t-storm", "thunderstorm").replace(";", "")
                        night_phrase = str(item.find('span', class_='night').find_all('p')[0].text).replace("Night: ", "").replace("t-storm", "thunderstorm").replace(";", "") if item.find('span', class_='night') else "Nothing"
                        precip = item.find('div', class_='precip').text.strip()

                        print(f"On {day}, {date}, expect day with {day_phrase} and {night_phrase} night with a high of {temp_hi} and a low of {temp_lo}, along with a {precip} chance of precipitation.\n")
                    
                    # Extract the Sun & Moon data
                    sun_moon_section = weather_url_soup.find('div', class_='sunrise-sunset content-module')

                    # Sun details
                    sun_details = sun_moon_section.find_all('div', class_='sunrise-sunset__item')[0]
                    sun_duration = sun_details.find('span', class_='sunrise-sunset__phrase').text
                    sun_rise_time = sun_details.find_all('span', class_='sunrise-sunset__times-value')[0].text
                    sun_set_time = sun_details.find_all('span', class_='sunrise-sunset__times-value')[1].text

                    # Moon details
                    moon_details = sun_moon_section.find_all('div', class_='sunrise-sunset__item')[1]
                    moon_phase = moon_details.find('span', class_='sunrise-sunset__phrase').text
                    moon_rise_time = moon_details.find_all('span', class_='sunrise-sunset__times-value')[0].text
                    moon_set_time = moon_details.find_all('span', class_='sunrise-sunset__times-value')[1].text

                    print(f"On This Day, The Sun will be visible for {sun_duration}. It will rise at {sun_rise_time} and set at {sun_set_time}. The moon is currently in its {moon_phase} phase, and it will rise at {moon_rise_time} and set at {moon_set_time}.\n")

                    # Find the AIR QUALITY
                    air_quality_module = weather_url_soup.find('a', class_='air-quality-module-wrapper')
                    if air_quality_module:
                        # Extract the information you need
                        title = air_quality_module.find('h2').text.strip()
                        category = air_quality_module.find('span', class_='air-quality-module__row__category').text.strip()
                        statement = air_quality_module.find('p', class_='air-quality-module__statement').text.strip()
                        
                        print(f"The {title} is looking like {category}, and {statement}\n")
                    else:print("Air quality data not found.")

                    # Find the ALLERGY OUTLOOK
                    health_activities_title_div = weather_url_soup.find('div', class_='health-activities__title')

                    # Extract the href attribute of the a tag
                    a_href = f"https://www.accuweather.com{health_activities_title_div.find('a')['href']}"

                    try:
                        # Initialize the dictionary to hold the categories
                        classified_data = {
                            'Very High': [],
                            'High': [],
                            'Moderate': [],
                            'Low': [],
                            'Good': [],
                            'Poor': [],
                            'Fair': [],
                            'Great': [],
                            'Ideal': [],
                            'Extreme': []
                        }

                        ALLERGY_OUTLOOK_request = requests.get(a_href, headers=headers, timeout=None)
                        ALLERGY_OUTLOOK_soup = BeautifulSoup(ALLERGY_OUTLOOK_request.content, 'html.parser')

                        # Extract the data
                        index_cards = ALLERGY_OUTLOOK_soup.find_all('a', class_='index-list-card')
                        for card in index_cards:
                            index_name = card.find('div', class_='index-name').text
                            index_status_text = card.find('div', class_='index-status-text').text
                            # Classify the data into the appropriate category
                            if index_status_text in classified_data:
                                classified_data[index_status_text].append(index_name)
                            else:
                                classified_data[index_status_text] = [index_name]
                        for status, names in classified_data.items():
                            if names:  # Check if the list is not empty
                                names_str = ', '.join(names)
                                print(f"For {names_str}, Allergy Outlook & Health Activities Conditions are {status}.")
                        print('')
                    except Exception as e:print(e)

                    try:
                        # Find the <a> tag with the desired data-slug attribute
                        a_tag = weather_url_soup.find('a', {'data-slug': 'dust-dander'})

                        if a_tag:
                            # Extract the href attribute
                            dust_and_dander_href = f"https://www.accuweather.com{a_tag.get('href')}"
                            
                            dust_dander_request = requests.get(url=dust_and_dander_href, headers=headers, timeout=None)
                            dust_dander_soup = BeautifulSoup(dust_dander_request.content, 'html.parser')

                            # Find the div with the specified class
                            div = dust_dander_soup.find('div', class_='lifestyle-index-chart-container__description')

                            # Find the <p> tag within the div
                            p_tag = div.find('p', class_='index-description')

                            # Extract and print the text from the <p> tag
                            if p_tag:print(f"Dust & Dander Report Saying: {p_tag.get_text()}\n")
                            else:print('No matching <p> tag found.')
                        else:print("The desired <a> tag was not found.")
                    except Exception as error:print(error)

                else:print('Failed to retrieve the webpage.')

            else:print("AccuWeather URL not found, process it.")

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            try:
                print(F"Fetching Weather Data from This Url: {current_weather_url}\n")
                # Step 1: Fetch the HTML content from the website
                response = requests.get(url=current_weather_url, headers=headers)
                response.raise_for_status()  # Raise HTTPError for bad responses
                html_content = response.content

                # Step 2: Parse the HTML using BeautifulSoup
                soup = BeautifulSoup(html_content, 'html.parser')

                # Step 3: Extract the required weather data
                current_weather_card = soup.find('div', class_='current-weather-card')
                if current_weather_card is None:
                    raise ValueError("Could not find the current-weather-card element on the page.")

                # Extracting the current temperature
                temperature_element = current_weather_card.find('div', class_='display-temp')
                temperature = temperature_element.get_text(strip=True) if temperature_element else "N/A"

                # Extracting the weather phrase
                phrase_element = current_weather_card.find('div', class_='phrase')
                weather_phrase = phrase_element.get_text(strip=True) if phrase_element else "N/A"

                # Extracting additional weather details
                details = current_weather_card.find_all('div', class_='detail-item spaced-content')
                weather_details = {}
                for detail in details:
                    key = detail.find('div').get_text(strip=True)
                    value = detail.find_all('div')[1].get_text(strip=True)
                    weather_details[key] = value

                # Creating sentences for each detail
                weather_report = (
                    f"The current temperature is {temperature} with {weather_phrase}. "
                    f"The RealFeel temperature is {weather_details.get('RealFeel®', 'N/A')}. "
                    f"Wind is blowing at {weather_details.get('Wind', 'N/A')} with gusts up to {weather_details.get('Wind Gusts', 'N/A')}. "
                    f"Humidity is at {weather_details.get('Humidity', 'N/A')} and indoor humidity is {weather_details.get('Indoor Humidity', 'N/A')}. "
                    f"The dew point is {weather_details.get('Dew Point', 'N/A')}. "
                    f"Pressure is {weather_details.get('Pressure', 'N/A')}. "
                    f"Cloud cover is {weather_details.get('Cloud Cover', 'N/A')} and visibility is {weather_details.get('Visibility', 'N/A')}. "
                    f"The cloud ceiling is {weather_details.get('Cloud Ceiling', 'N/A')}."
                )

                # Printing the weather report
                print(weather_report)

            except requests.exceptions.RequestException as e:
                print(f"Error fetching the weather data: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

            # Clear cookies
            session.cookies.clear_expired_cookies()
            session.cookies.clear_session_cookies()
            session.cookies.clear()

            # Close the session
            session.close()

        except Exception as  E:print(E)

if __name__=="__main__":
    Place="Delhi"
    weather = AccuWeather()
    weather.Extract_Weather(Place=Place)