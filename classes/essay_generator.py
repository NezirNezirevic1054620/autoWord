from docx import Document
import os
from openai import OpenAI
from dotenv import load_dotenv


class EssayGenerator:

    def __init__(self, title):
        self.title = title

    @staticmethod
    def __get_document():
        document = Document()

        return document

    def generate_essay(self, message1):
        document = self.__get_document()
        load_dotenv()
        openai_api_key = os.getenv("OPENAI_API_KEY")

        client = OpenAI(
            api_key=openai_api_key,
        )

        message = f"Generate a essay about {message1} min 500 words"

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You are a very skilled essay maker, your english grammar is perfect, you have a huge vocabulary, and you can make a structured essay with a introduction, and a conclusion"},
                {"role": "user", "content": message}
            ]
        )

        document.add_paragraph(completion.choices[0].message.content)
        document.save(f"docs/{self.title}.docx")
