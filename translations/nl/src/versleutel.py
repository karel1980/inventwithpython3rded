# Caesar Versleuteling

MAX_SLEUTEL_GROOTTE = 26

def geefModus():
    while True:
        print('Wil je een bericht versleutelen of ontcijferen?')
        modus = input().lower()
        if modus in 'versleutel versleutelen v ontcijfer ontcijferen o'.split():
            return modus
        else:
            print('Voer ofwel "versleutelen" of "v" in, of "ontcijveren of "o".')

def geefBericht():
    print('Voer je bericht in:')
    return input()

def geefSleutel():
    sleutel = 0
    while True:
        print('Geef het sleutelgetal in (1-%s)' % (MAX_SLEUTEL_GROOTTE))
        sleutel = int(input())
        if (sleutel >= 1 and sleutel <= MAX_SLEUTEL_GROOTTE):
            return sleutel

def geefVertaaldBericht(modus, message, sleutel):
    if modus[0] == 'o':
        sleutel = -sleutel
    vertaald = ''

    for symbool in message:
        if symbool.isalpha():
            num = ord(symbool)
            num += sleutel

            if symbool.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbool.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            vertaald += chr(num)
        else:
            vertaald += symbool
    return vertaald

modus = geefModus()
message = geefBericht()
sleutel = geefSleutel()

print('Je vertaald bericht is:')
print(geefVertaaldBericht(modus, message, sleutel))
