import random
getal1 = random.randint(1, 10)
getal2 = random.randint(1, 10)
print('Hoeveel is ' + str(getal1) + ' + ' + str(getal2) + '?')
answer = input()
if answer == getal1 + getal2:
    print('Correct!')
else:
    print('Helaas! Het antwoord is ' + str(getal1 + getal2))
