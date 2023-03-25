from morsecodedict import morse_to_alphabet, alphabet_to_morse


translation = ''

user_choice = input('Choose one of the options: 1. Translate sentence into Morse Code'
                    ' 2. Translate Morse Code into sentence ')
user_sentence = input('enter sentence that you want to convert to morse or unconvert: ')

if user_choice == '1':
    for letter in user_sentence.upper().replace(' ', ''):
            translation += alphabet_to_morse[letter]
            translation += ' '

    print(translation)

else:
    for morse in user_sentence.split():
        translation += morse_to_alphabet[morse]
    print(translation)


