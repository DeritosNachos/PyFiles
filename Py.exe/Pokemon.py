from random import randint
from time import sleep

p1health = 100
p2health = 100


#messages

print('''
How to play
Moves:
Quick Attack--Q-- High Probability Low Damage
Heavy Attack--H-- Low Probability High Damage
Heal----------X-- Medium Probability
''')
while p1health > 0 and p2health > 0: #play the game while both players have life
    numbergen1 = randint(1,100)
    numbergen2 = randint(1,100)   #generates values of 1-100
    
    move1 = -randint(18,25)
    move2 = -randint(25,45)
    move3 = randint(18,65)    #heal
    
    decision1 = input('Choose a move: ').upper()
    if decision1 not in 'QHX':
        print('''I don't understand''')
    else:
        if decision1 == 'Q' and numbergen1 >= 30:
            p2health += move1
            print('player chooses quick attack and was successful')
            print('quick attack does', move1, 'damage')
        elif decision1 == 'H' and numbergen1 >= 70:
            p2health += move2
            print('player chooses heavy attack and was successful')
            print('heavy attack does', move2, 'damage')
        elif decision1 == 'X' and numbergen1 >= 50:
            p1health += move3
            print('player chooses heal and was successful')
            print('heal does', move3, 'health')
        else:
            print('player move unsuccessful')
    botmove = randint(1,3)
    if botmove == 1 and numbergen2 >= 30:
        p1health += move1
        print('bot chooses quick attack and was successful')
        print('quick attack does', move1, 'damage')
    elif botmove == 2 and numbergen2 >= 70:
        p1health += move2
        print('bot chooses heavy attack and was successful')
        print('heavy attack does', move2, 'damage')
    elif botmove == 3 and numbergen2 >= 50:
        p2health += move3
        print('bot chooses heal and was successful')
        print('heal does', move3, 'health')
    else:
        print('bot move unsuccessful')
    if p2health > 0 and p1health > 0:
        print('bot health =', p2health)
        print('player health =', p1health)
        
print('Game Over')    
if p1health > 0:
    print('you win!')
else:
    print('you lose')

sleep(5)

