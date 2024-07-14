# Import the Streamlit library
import streamlit as st

# Define the main function
def main():
  # Set the title of the app
  st.title("Welcome to !")

  # Display a welcome message
  st.write("Hello, welcome to my Streamlit app!")

  # Create a button
  if st.button('Say Hello'):
    # Display a message when the button is clicked
    st.write("Hello, Streamlit!")

# Run the main function
if __name__ == '__main__':
  main()

  '''
  elif "weather" in query:

      # Google Open weather website
      # to get API of Open weather
      api_key = "75394ec72bfd20458b76d9632aceb3eb"
      base_url = "http://api.openweathermap.org/data/2.5/weather?"
      say(" City name ")
      print("City name : ")
      city_name = takeCommand()
      complete_url = base_url + "appid =" + api_key + "&q =" + city_name
      response = requests.get(complete_url)
      x = response.json()

      if x["code"] != "404":
          y = x["main"]
          current_temperature = y["temp"]
          current_pressure = y["pressure"]
          current_humidiy = y["humidity"]
          z = x["weather"]
          weather_description = z[0]["description"]
          print(" Temperature (in kelvin unit) = " + str(
              current_temperature) + "\n atmospheric pressure (in hPa unit) =" + str(
              current_pressure) + "\n humidity (in percentage) = " + str(
              current_humidiy) + "\n description = " + str(weather_description))

      else:
          say(" City Not Found ")
  '''
  '''
  elif 'search' in query or 'play' in query:

      query = query.replace("search", "")
      query = query.replace("play", "")
      webbrowser.open(query)
  '''