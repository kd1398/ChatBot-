#Description : This is a chat bot program

#import the library
from nltk.chat.util import Chat, reflections

pairs = [['my name is (.*)', ['hi %1']],
         ['hi|hello|hey|holla|hola', ['hey there', 'hi there', 'hayyy']],
         ['(.*) is very much useful language', ['%1 is truely an efficient and helpful language.']],
         ['(.*)(location|city) ?', ['India']],
         ['(.*) created you ?', ['kinjal did using NLTK :)']],
         ['(.*)help', ['Sure I can help you :)']],
         ['(.*) your name ?', ['My name is J.A.R.V.I.S']]
         ]

#reflections is the dictionary

my_dummy_reflections = {
        'hello' : 'hey',
        'how are you' : 'i m fine, thank you :)'
    }

chat = Chat(pairs, my_dummy_reflections)
chat.converse()
