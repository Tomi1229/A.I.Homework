import openai # type: ignore

class AIService:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_interview_question(self, job_title: str, previous_answer: str) -> str:
        try:
            prompt = (
                f"Te egy állásinterjúztató vagy egy IT cégben. "
                f"A pozíció: {job_title}. Az előző válasz a jelölttől: \"{previous_answer}\". "
                f"Tegyél fel egy releváns következő kérdést, hogy jobban megismerd a jelöltet."
            )
            
            # Az új API szintaxis használata
            response = openai.completions.create(
                model="gpt-3.5-turbo",
                prompt=prompt,
                max_tokens=150,
                temperature=0.7,
            )
            
            return response['choices'][0]['text'].strip()  # Az új verzióban a válasz szöveg itt található
            
        except Exception as e:
            return f"Hiba történt az AI kérdésgenerálás során: {str(e)}"
