import openai

class AIService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_response(self, prompt: str):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Válassz a támogatott modellek közül, pl. gpt-3.5-turbo
                messages=[
                    {"role": "system", "content": "Te egy állásinterjúztató vagy."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return f"Error during AI response generation: {str(e)}"
