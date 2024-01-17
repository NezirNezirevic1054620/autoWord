from pprint import pprint

from PyInquirer import prompt
from examples import custom_style_2

from classes.cv_generator import CVGenerator
from classes.essay_generator import EssayGenerator

questions = [
    {
        'type': 'list',
        'name': 'word',
        'message': 'What type of Word document would you like to generate?',
        'choices': [
            'CV',
            'Essay'
        ]
    }
]

answers = prompt(questions, style=custom_style_2)

if questions[0]["choices"][1]:
    questions2 = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'What is the name of your essay?',
        },
        {
            'type': 'input',
            'name': 'paragraph',
            'message': 'Write your paragraph',
        }
    ]

    answers2 = prompt(questions2, style=custom_style_2)
    essay = EssayGenerator(title=list(answers2.values())[0], paragraph=list(answers2.values())[1])
    essay.generate_essay()

elif questions[0]["choices"][0]:
    questions3 = [
        {
            'type': 'input',
            'name': 'title',
            'message': 'What is the name of your CV',
        },
        {
            'type': 'input',
            'name': 'introduction',
            'message': 'Write your introduction',
        }
    ]

    answers3 = prompt(questions3, style=custom_style_2)
    cv = CVGenerator(title=list(answers3.values())[0], paragraph=list(answers3.values())[1])
