from PyInquirer import prompt, Separator
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
    generator_choice = [
        {
            "type": "list",
            "name": "word",
            "message": "What type of Word document would you like to generate?",
            "choices": ["Essay", "CV"],
        }
    ]

    answers = prompt(generator_choice, style=custom_style_2)

    if generator_choice[0]["choices"][0]:
        essay_questions = [
            {
                "type": "input",
                "name": "title",
                "message": "What is the name of your Essay?",
            },
        ]

        essay_answers = prompt(essay_questions, style=custom_style_2)
        essay_answer = list(essay_answers.values())[0]
        essay = EssayGenerator(title=essay_answer)
        essay.generate_essay(message1=essay_answer)

    elif generator_choice[0]["choices"][1]:
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
            cv_generator = CVGenerator(
                title=list(answers3.values())[0], paragraph=list(answers3.values())[1]
            )
            cv_generator.generate_cv()
