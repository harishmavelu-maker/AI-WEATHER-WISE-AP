import streamlit as st
import requests
from datetime import datetime

# -------------------------------
# AI WEATHER WISE AP
# -------------------------------

st.set_page_config(
    page_title="AI Weather Wise AP",
    page_icon="🌦️",
    layout="centered"
)

# Title
st.title("🌦️ AI WEATHER WISE AP")
st.write("AI-powered weather information and daily weather assistant.")

st.divider()

# API key
api_key = st.sidebar.text_input(
    "Enter OpenWeather API Key",
    type="password"
)

# City input
city = st.text_input(
    "Enter City Name",
    placeholder="Example: Chennai"
)

# Weather search
if st.button("🔍 Get Weather"):

    if not api_key:
        st.warning("Please enter your OpenWeather API key in the sidebar.")

    elif not city:
        st.warning("Please enter a city name.")

    else:

        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={api_key}&units=metric"
        )

        try:
            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()

                temperature = data["main"]["temp"]
                feels_like = data["main"]["feels_like"]
                humidity = data["main"]["humidity"]
                pressure = data["main"]["pressure"]

                weather = data["weather"][0]["description"]
                wind_speed = data["wind"]["speed"]

                country = data["sys"]["country"]

                # Weather heading
                st.success(
                    f"Weather information for {city.title()}, {country}"
                )

                # Weather information
                col1, col2 = st.columns(2)

                with col1:
                    st.metric(
                        "🌡️ Temperature",
                        f"{temperature} °C"
                    )

                    st.metric(
                        "💧 Humidity",
                        f"{humidity}%"
                    )

                    st.metric(
                        "🌬️ Wind Speed",
                        f"{wind_speed} m/s"
                    )

                with col2:
                    st.metric(
                        "🌡️ Feels Like",
                        f"{feels_like} °C"
                    )

                    st.metric(
                        "Pressure",
                        f"{pressure} hPa"
                    )

                    st.write(
                        f"**☁️ Condition:** {weather.title()}"
                    )

                st.divider()

                # AI-style weather explanation
                st.subheader("🤖 AI Weather Explanation")

                if temperature >= 35:
                    suggestion = (
                        "It is very hot today. Stay hydrated "
                        "and avoid unnecessary outdoor activities."
                    )

                elif temperature >= 25:
                    suggestion = (
                        "The weather is warm. Carry water "
                        "and plan outdoor activities accordingly."
                    )

                elif temperature >= 18:
                    suggestion = (
                        "The temperature is comfortable. "
                        "It is suitable for most outdoor activities."
                    )

                else:
                    suggestion = (
                        "The weather is cool. Consider carrying "
                        "a light jacket when going outside."
                    )

                st.info(suggestion)

                # Humidity suggestion
                if humidity > 80:
                    st.warning(
                        "High humidity detected. You may feel warmer "
                        "than the actual temperature."
                    )

                # Wind suggestion
                if wind_speed > 10:
                    st.warning(
                        "Strong winds detected. Take care when "
                        "travelling outdoors."
                    )

                # Search time
                current_time = datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )

                st.caption(
                    f"Weather checked at: {current_time}"
                )

            else:
                st.error(
                    "City not found or API key is invalid."
                )

        except requests.exceptions.RequestException:
            st.error(
                "Unable to connect to the weather service."
            )


# Sidebar
st.sidebar.divider()
st.sidebar.subheader("About")

st.sidebar.write(
    "AI Weather Wise AP provides weather information "
    "and simple AI-based recommendations."
)

st.sidebar.write(
    "Developed using Python and Streamlit."
)
