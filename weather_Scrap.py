import requests
from bs4 import BeautifulSoup

def fech_data():
    url_telAviv = "https://weather.com/weather/today/l/7c511642f70a5b458d73fdb9a585169db2060b1adbdaa5b230a1819d3fe47cbb"
    url_Afula = "https://weather.com/weather/today/l/e02fe1129123296eba3b6ede23c1ec50a969b5c69044ae54f2d0009c79bf096f"

    user_input = int(input('''
Afula - 1
Tel Aviv - 2
Enter which city to show : '''))
# Fetch the page
    if user_input == 1:
        response = requests.get(url_Afula)
        city = 'Afula'
        return response,city
    elif user_input == 2:
        response = requests.get(url_telAviv)
        city = 'Tel Aviv'
        return response,city

def parse_data():

    response, city = fech_data()
# Ensure the request was successful
    if response.status_code == 200:
    # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the temperature
        temp_element = soup.find('span', {'data-testid': 'TemperatureValue'})
        temperature = temp_element.text.strip() if temp_element else 'N/A'

        # Extract the Humidity
        humidity_element = soup.find('span', {'data-testid': 'PercentageValue'})
        humidity = humidity_element.text.strip() if humidity_element else 'N/A'
        
        return temperature, humidity, city
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
    
def main():
    temperature, humidity, city = parse_data()

    if city is None:  # Проверяем, есть ли корректные данные
        print("Program terminated due to invalid input.")
        return

    # Отображаем результат
    print(f"{city} Weather:")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
main()