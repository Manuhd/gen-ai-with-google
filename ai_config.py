import google.generativeai as genai

# Configure once with your API key
genai.configure(api_key="API KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

