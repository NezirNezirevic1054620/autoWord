from pprint import pprint

from PyInquirer import prompt
from examples import custom_style_2

from classes.cv_generator import CVGenerator
from classes.essay_generator import EssayGenerator

welcome_prompt = [
    {
        "type": "confirm",
        "message": "Welcome to auto word generator! Would you like to proceed?",
        "name": "continue",
        "default": True,
    }
]

welcome_prompt_answers = prompt(welcome_prompt, style=custom_style_2)

if list(welcome_prompt_answers.values())[0] is True:
    questions = [
        {
            "type": "list",
            "name": "word",
            "message": "What type of Word document would you like to generate?",
            "choices": ["Essay", "CV"],
        }
    ]

    answers = prompt(questions, style=custom_style_2)

    if questions[0]["choices"][0]:
        questions2 = [
            {
                "type": "input",
                "name": "title",
                "message": "What is the name of your essay?",
            },
            {
                "type": "input",
                "name": "paragraph",
                "message": "Write your paragraph",
            },
            {
                "type": "confirm",
                "message": "Do you want to continue?",
                "name": "continue",
                "default": True,
            },
        ]

        answers2 = prompt(questions2, style=custom_style_2)

        if list(answers2.values())[2] is True:
            essay = EssayGenerator(
                title=list(answers2.values())[0], paragraph=list(answers2.values())[1]
            )
            essay.generate_essay()

    elif questions[0]["choices"][1]:
        questions3 = [
            {
                "type": "input",
                "name": "title",
                "message": "What is the name of your CV",
            },
            {
                "type": "input",
                "name": "introduction",
                "message": "Write your introduction",
            },
            {
                "type": "confirm",
                "message": "Do you want to continue?",
                "name": "continue",
                "default": True,
            },
        ]

        answers3 = prompt(questions3, style=custom_style_2)
        if list(answers3.values())[2] is True:
            cv = CVGenerator(title=list(answers3.values())[0], paragraph=list(answers3.values())[1])
            cv.generate_cv()
