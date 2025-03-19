from typing import Literal
 
# Import the Braintrust SDK for creating/managing projects and tools
import braintrust
# Import Pydantic for data validation and schema generation
from pydantic import BaseModel, RootModel, Field
import os
import requests
import logging
from typing import Dict, List, Optional, Union

"""
This script is used to create tools in Braintrust.
Currently implemented tools:
- Calculator: A simple calculator that can add, subtract, multiply, and divide numbers
- Current Weather: Get current weather data for a specified city
use this command to push the tools to Braintrust:
braintrust push tools.py
"""

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('weather_tool')
 
# Get or create a Braintrust project named "workflow-glowing"
# Note: To use an existing project instead of creating a new one,
# replace this with: project = braintrust.projects.get(name="workflow-glowing")
project = braintrust.projects.create(name="workflow-glowing")
 
 
# Define the input schema for our calculator tool using Pydantic
# This creates a JSON schema that will be used to validate inputs and
# guide the model on how to format its tool calls
class CalculatorInput(BaseModel):
    # The operation to perform (must be one of these four options)
    op: Literal["add", "subtract", "multiply", "divide"]
    # The first number (can be any float value)
    a: float
    # The second number (can be any float value)
    b: float
 
 
# Define the output schema for our calculator tool
# RootModel[float] means the entire output is just a single float value
# instead of a complex object with multiple fields
class CalculatorOutput(RootModel[float]):
    # No additional fields needed, so we use 'pass'
    # The calculator will return a simple float value
    pass
 
 
# The actual function that performs the calculation
# This is what gets executed when an LLM calls the tool
def calculator(op, a, b):
    # Use Python's match statement to handle different operations
    match op:
        case "add":
            return a + b
        case "subtract":
            return a - b
        case "multiply":
            return a * b
        case "divide":
            return a / b
 
 
# Register the calculator function as a tool in Braintrust
# This makes it available for LLMs to call when this tool is attached to a prompt
project.tools.create(
    # The function that will be executed when the tool is called
    handler=calculator,
    # A user-friendly name for the tool (shown in the UI)
    name="Calculator method",
    # A unique identifier for the tool (must be unique within the project)
    slug="calculator",
    # A description of what the tool does (used by the LLM to understand when to call it)
    description="A simple calculator that can add, subtract, multiply, and divide.",
    # The input schema - defines what parameters the LLM must provide
    parameters=CalculatorInput,  # You can also provide raw JSON schema here if you prefer
    # The output schema - defines what the tool will return
    returns=CalculatorOutput,
)

"""
Here is a another tool to call the weather API to call the current weather in a city.

Reference link to API documentation:
https://openweathermap.org/current
"""

# Define input schema for the weather API tool
class WeatherInput(BaseModel):
    city: str = Field(..., description="The name of the city to get weather data for")
    country_code: str = Field(..., description="Two-letter country code (ISO 3166)")
    units: Optional[Literal["standard", "metric", "imperial"]] = Field(
        "metric", 
        description="Units of measurement. standard: Kelvin, metric: Celsius, imperial: Fahrenheit"
    )
    lang: Optional[str] = Field(
        "en", 
        description="Language for weather descriptions (e.g., en, fr, es)"
    )

# Define the structure for weather data response
class WeatherData(BaseModel):
    # ... is an ellipsis, it means that the field is required. The `description` parameter adds a documentation to what this field is for.
    temperature: float = Field(..., description="Current temperature")
    feels_like: float = Field(..., description="Feels like temperature")
    description: str = Field(..., description="Weather condition description")
    humidity: int = Field(..., description="Humidity percentage")
    wind_speed: float = Field(..., description="Wind speed")
    country: str = Field(..., description="Country code")
    city_name: str = Field(..., description="City name")
    weather_main: str = Field(..., description="Main weather category")
    pressure: int = Field(..., description="Atmospheric pressure in hPa")
    units: str = Field(..., description="Units used for measurements")

# Function to fetch current weather data
def get_current_weather(city, country_code, units="metric", lang="en"):
    # Get API key from environment variable
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    if not api_key:
        logger.error("API key not found in environment variables")
        return {"error": "API key not found in environment variables"}
    
    logger.info(f"Weather data requested with params: city={city}, country_code={country_code}, units={units}")
    
    # Build the API URL and params
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Construct the location query parameter
    location_query = f"{city},{country_code}"
    logger.info(f"Using city name: {location_query}")
    
    params = {
        "q": location_query,
        "appid": api_key,
        "units": units,
        "lang": lang
    }
    
    try:
        # Make the API request
        logger.info(f"Making API request to: {base_url} with params: {params}")
        response = requests.get(base_url, params=params)
        
        # Check if request was successful
        if response.status_code == 200:
            # Process response
            data = response.json()
            logger.info(f"Got successful response from API with data for: {data.get('name', 'unknown location')}")
            
            # Format the response
            weather_data = {
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "description": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "country": data["sys"]["country"],
                "city_name": data["name"],
                "weather_main": data["weather"][0]["main"],
                "pressure": data["main"]["pressure"],
                "units": units
            }
            
            logger.info(f"Returning formatted weather data for {weather_data['city_name']}")
            return weather_data
        else:
            logger.error(f"API error: {response.status_code} - {response.text}")
            return {"error": f"API error: {response.status_code}", "message": response.text}
    
    except Exception as e:
        logger.exception(f"Exception occurred while fetching weather data: {str(e)}")
        return {"error": f"Exception occurred: {str(e)}"}

# Register the weather tool in Braintrust
project.tools.create(
    handler=get_current_weather,
    name="Current Weather",
    slug="current-weather",
    description="Retrieve current weather data for a specified city. Provides temperature, feels like, humidity, wind speed, and weather description. Requires both city name and country code (ISO 3166, e.g., 'us', 'gb', 'fr').",
    parameters=WeatherInput,
    returns=WeatherData,
)

# Test code - Only runs when script is executed directly
if __name__ == "__main__":
    # Test each operation to verify that the calculator works
    test_cases = [
        {"op": "add", "a": 5, "b": 3},
        {"op": "subtract", "a": 10, "b": 4},
        {"op": "multiply", "a": 6, "b": 7},
        {"op": "divide", "a": 20, "b": 5}
    ]
    
    print("Testing calculator function:")
    print("---------------------------")
    
    for case in test_cases:
        result = calculator(**case)
        print(f"{case['op']}({case['a']}, {case['b']}) = {result}")
    
    print("\nAll tests completed!")
    print("Note: This only tests the function locally.")
    print("To test the deployed tool in Braintrust, push it with 'braintrust push tools.py'")
    print("Then access it through the Braintrust UI in your project 'workflow-glowing'")

    # Test the weather API function if API key is available
    if os.environ.get("OPENWEATHER_API_KEY"):
        print("\nTesting weather API function:")
        print("---------------------------")
        
        # Test with city and country code
        print("\nTest 1: Using city and country code (France)")
        weather = get_current_weather(city="Paris", country_code="fr")
        print(f"Current weather in {weather.get('city_name', 'Paris')}, {weather.get('country', 'FR')}:")
        print(f"Temperature: {weather.get('temperature')}°C")
        print(f"Description: {weather.get('description')}")
        
        # Test with another city and country code
        print("\nTest 2: Using city and country code (UK)")
        weather = get_current_weather(city="London", country_code="gb")
        print(f"Current weather in {weather.get('city_name', 'London')}, {weather.get('country', 'GB')}:")
        print(f"Temperature: {weather.get('temperature')}°C")
        print(f"Description: {weather.get('description')}")
    else:
        print("\nSkipping weather API test - OPENWEATHER_API_KEY not found in environment")

