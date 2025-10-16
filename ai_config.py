import google.generativeai as genai

# Configure once with your API key
genai.configure(api_key="AIzaSyBUw8WDMDk5dAnm3AqeBUEhDPbrZVE93ZE")

model = genai.GenerativeModel("gemini-2.5-flash")
