"""
Test openAI API
"""

import os
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

with open("token_file.txt", "r", encoding="utf-8") as file:
    TOKEN = file.read()
os.environ["OPENAI_API_KEY"] = TOKEN
PROMT = "Ты гонзо журналист и общаешься только в этом стиле"  # тут мы как раз дообучаем модель
USER_MASSAGE = "Расскажи прогноз погоды в Москве на завтра"  # это то что спрашивает у модлеи пользователь


def get_massage_from_gpt(promt: str, user_massage: str) -> ChatCompletionMessage:
    """
    doc string
    """
    print(os.environ.get("OPENAI_API_KEY"))
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": promt},
            {"role": "user", "content": user_massage},
        ],
    )

    return completion.choices[0].message


massage = get_massage_from_gpt(PROMT, USER_MASSAGE)
print(massage)
