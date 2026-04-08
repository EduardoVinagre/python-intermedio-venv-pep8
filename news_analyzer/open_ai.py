import os
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def analyze_news_with_ia(articles: list[dict], query:str) -> str | None:
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    context = "\n".join([
        f"-{article['title']}: {article.get('description','')[:100]}..."
        for article in articles[:10] #Limitar para control de costos
    ])

    prompt = f"""
        Basándote en estas noticias:
        {context}

        Pregunta: {query}

        Responde de forma concisa en español.
    """

    try:
        response = client.responses.create(
            model="gpt-5.2",
            instructions="Eres un agente que lee contexto y responde de manera breve",
            input=prompt,
        )

        print(response.output_text)
    except openai.APIConnectionError as e:
        print("The server could not be reached")
        print(e.__cause__)  # an underlying Exception, likely raised within httpx.
    except openai.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
    except openai.APIStatusError as e:
        print("Another non-200-range status code was received")
        print(e.status_code)
        print(e.response)
