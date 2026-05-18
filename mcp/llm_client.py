import requests


class LLMClient:

    API_URL = (
        "https://api.longcat.chat/openai/v1/chat/completions"
    )

    API_KEY = (
        "ak_2GD5Wb7kU09m2n54Tp6kj4wi64T7v"
    )

    @staticmethod
    def generate(prompt):

        headers = {

            "Authorization":
                f"Bearer {LLMClient.API_KEY}",

            "Content-Type":
                "application/json"
        }

        payload = {

            "model": "LongCat-Flash-Chat",

            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }
            ],

            "max_tokens": 30,

            "temperature": 0.2
        }

        try:

            response = requests.post(

                LLMClient.API_URL,

                headers=headers,  #Authentication + content type.

                json=payload,

                timeout=3   
            )

            data = response.json()        #Converts LongCat API response into Python dictionary.

            ai_response = (
                data["choices"][0]
                ["message"]["content"]
            )

            print("\n")
            print("=" * 60)
            print("LONGCAT AI RESPONSE")
            print("=" * 60)

            print(ai_response)

            print("=" * 60)
            print("\n")

            return ai_response.strip()

        except Exception:

            # FAST fallback
            return "//button"