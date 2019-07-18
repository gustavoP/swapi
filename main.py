from __future__ import print_function, unicode_literals

import pandas as pd
from PeopleAPI import PeopleAPI

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import sw

#menu style
style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: 'bold',
})

print("Hello son! \nYou have to be the strongest of all. \nFor that I have collected some data to help you.")


### Firts menu ####
questions = [
    {
        'type': 'list',
        'message': 'What do you want to know?',
        'name': 'data',
        'choices': [
            #Separator('Hello!!'),
            {
                'name': 'Who are the top pilots'
            },
            {
                'name': 'I want to know the fastest pilots'
            },
            {
                'name': 'Show me which pilots I have to overcome'
            }
        ],
        'validate': lambda answer: 'You must choose at least one.' \
            if len(answer) == 0 else True
    }
]
answers = prompt(questions, style=style)


print("Oh, good choice. Wait here...")

top = pd.DataFrame(PeopleAPI().get_people_festest_vehicle())
top = top.rename(columns={ 'person' : 'pilot'})
top.speed = top.speed.astype(float)
top = top.sort_values(by='speed', ascending = False).reset_index(drop=True)

print(top)

#### Second menu ####
questions = [
    {
        'type': 'list',
        'message': 'What do you want to do now?',
        'name': 'after',
        'choices': [
            #Separator('Hello!!'),
            {
                'name': 'Nothing.'
            },
            {
                'name': 'chill out and watch a movie!'
            }
        ],
        'validate': lambda answer: 'You must choose at least one.' \
            if len(answer) == 0 else True
    }
]
answers = prompt(questions, style=style)

if answers['after']=='chill out and watch a movie!':
    sw.start_movie()
    print("Come to the dark side")
    exit()
else:
    print("Come to the dark side")
    exit()
