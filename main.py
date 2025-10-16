from ai_config import model

#  Get user input
query = input(" You: ")

#  Send the input to Gemini
response = model.generate_content(query)

# Print the response
print("\n Gemini AI:", response.text.strip())
