import random
from time import sleep
from utils.hangman_art import logo, stages
from utils.hangman_words import word_list
from utils.helper import cls

word = random.choice(word_list)
moves = 6
word_display = []
wrong_guesses = []
word_lengh = len(word)
picture = stages[moves]

for num in range(word_lengh):
    word_display.append('_')

end_of_game = False

print(logo)

while not end_of_game:
    print(picture)
    print(f'{word_display}    wrong ones: {wrong_guesses}\n')
    guess = input('Chose a letter to find the word: ').lower()
    cls()
    
    while guess in word_display or guess in wrong_guesses:
        print(f'You alredy tried "{guess}", guess another one!')
        print(picture)
        print(f'{word_display}    wrong ones: {wrong_guesses}\n')
        guess = input('Chose a letter to find the word: ').lower()
        cls()
    
    for position in range(word_lengh):
        letter = word[position]
        if guess == letter:
            word_display[position] = guess
    if guess in word_display:
        print(f'Good job ! "{guess}" is correct !')
    else: 
        wrong_guesses.append(guess)
        moves -= 1
        print(f'Wrong move! "{guess}" not part of the word. {moves} moves left!')
            
    picture = stages[moves]
    if moves == 0:
        end_of_game = True
        print('You are out of moves, you lost !')
        print(f'the word was : {word}')
        print(f'Thanks for playing:\n{logo}')
        sleep(1)     
    else:
        if '_' not in word_display:
            end_of_game = True
            print('Congratulations, you won!')
            print(f'Thanks for playing:\n{logo}')
            sleep(1)
            

    

