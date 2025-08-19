import requests

API_KEY = "1f374b415b6b59fed64a665edb76e13f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        # Build request URL
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            print(f"\n🌍 Weather in {city_name}")
            print(f"🌡 Temperature: {temperature}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁️ Condition: {description}")

        elif response.status_code == 401:
            print("❌ Invalid API Key.")
        elif response.status_code == 404:
            print("❌ City not found.")
        else:
            print("⚠️ Error:", response.status_code)

    except requests.exceptions.ConnectionError:
        print("❌ No Internet connection!")


# --- Main Program ---
while True:
    city = input("\nEnter city name (or 'exit' to quit): ")
    if city.lower() == "exit":
        print("👋 Goodbye!")
        break
    get_weather(city)
