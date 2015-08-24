import random
print('Ik ga 1000 muntjes opwerpen. Raad eens hoeveel het kop zal zijn. (Druk op enter om te beginnen)')
input()
worpen = 0
kop = 0
while worpen < 1000:
    if random.randint(0, 1) == 1:
        kop = kop + 1
    worpen = worpen + 1

    if worpen == 900:
        print('900 worpen en het was al ' + str(kop) + ' keer kop.')
    if worpen == 100:
        print('Na 100 worpen was het al ' + str(kop) + ' keer kop.')
    if worpen == 500:
        print('We zijn halverwege, en het was al ' + str(kop) + ' keer kop.')

print()
print('Van 1000 worpen wwas het ' + str(kop) + ' keer kop!')
print('Zat je in de buurt?')
