"""
projekt_1.py: projekt č.1 - Engeto Online Python Akademie
author: Martin Rechtorik
email: martin.rechtorik@nacr.cz
discord: Maarty#1226
"""

from task_template import TEXTS as text

users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123',
}
welcome = "Welcome in our text analyzing tool"
separator = "="
print(welcome)
print(len(welcome) * separator)


def login():
    """Checks if username and password are on the list and match"""
    username = input('Fill in your username: ')
    logout = 'Unregistered user, terminating the program..'
    if username not in users:
        print(logout)
        print(len(logout) * separator)
        quit(login)
    else:
        userpass = input('Fill in your password: ')
        if users.get(username) == userpass:
            check_in = 'Thanks for authorization '
            print(check_in + username)
            print((len(username) + len(check_in)) * separator)
            pass

        else:
            wr_pass = 'Sorry, wrong password, terminating the program..'
            print(wr_pass)
            print(len(wr_pass) * separator)
            quit(wr_pass)

def text_selection():
    """Menu for text selection based od correct number"""
    basic_info = 'Three available texts can be analyzed and they are numbered from 1 to 3.'
    print(basic_info)
    print(len(basic_info) * "=")
    text_offer = 'Choose the number of the text to be analyzed:'
    textNumber = input(text_offer)
    if textNumber.isnumeric():
        intNumber = int(textNumber) - 1
        if intNumber in range(0, 3):
            selectedText = text[intNumber]
            numberWords = 0
            numberFirstUp = 0
            numberAllUp = 0
            numberAllLow = 0
            numberNumbers = 0
            sumNumbers = 0

            selectedText = selectedText.strip()
            selectedText = selectedText.replace('\n', ' ')
            words = selectedText.split(' ')

            numberWords = len(words)

            statistics = dict()
            maxNumber = 0;

            for word in words:
                word = word.strip('.,')
                lenghtWord = len(word)

                if lenghtWord in statistics:
                    statistics[lenghtWord] += 1
                else:
                    statistics[lenghtWord] = 1

                if statistics[lenghtWord] > maxNumber:
                    maxNumber = statistics[lenghtWord]

                if word.isupper():
                    numberAllUp += 1
                if word[0].isupper():
                    numberFirstUp += 1
                if word.isnumeric():
                    numberNumbers += 1
                    sumNumbers += int(word)
                if word.islower():
                    numberAllLow += 1
            title = 'Text num. ' + textNumber + 'was analyzed.'
            titleLenght = (len(text_offer + ' ' + textNumber))
            print((len(text_offer) + 1) * "-")
            print(title.center(titleLenght))
            print('The total number of words in the text:', numberWords)
            print('Number of words with the first capital letter:', numberFirstUp)
            print('Number of capitalized words:', numberAllUp)
            print('Number of words written in lowercase letters:', numberAllLow)
            print('Total number of numbers in the text :', numberNumbers)
            print('In total:', sumNumbers)

            print((len(text_offer) + 1) * "-")

            title = 'Words statistics in text numb. ' + textNumber

            print(title.center(titleLenght))

            title1 = 'Numb of characters'
            title2 = 'Numb of words'
            title1Lenght = len(title1)
            title2Lenght = len(title2)

            if maxNumber > title2Lenght:
                title2Lenght = maxNumber

            partialText = (title1Lenght + 5 + title2Lenght + 5) * '-'
            print(partialText.center(titleLenght))

            partialText = '| ' + title1 + ' | ' + title2.center(title2Lenght + 3) + ' |'
            print(partialText.center(titleLenght))

            partialText = (title1Lenght + 5 + title2Lenght + 5) * '-'
            print(partialText.center(titleLenght))

            for key, value in sorted(statistics.items()):
                valueString = value * '*' + ' ' + str(value)
                partialText = ('| ' + str(key).rjust(title1Lenght) + ' | ' + valueString.ljust(title2Lenght + 3) + ' |')
                print(partialText.center(titleLenght))

            partialText = ((title1Lenght + 5 + title2Lenght + 5) * '-')
            print(partialText.center(titleLenght))

        else:
            print('Such text ' + textNumber + ' is not available.')
    else:
        print('You haven´t put in a number.')


login()

text_selection()
