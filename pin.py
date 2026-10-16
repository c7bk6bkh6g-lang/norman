#Variant 1

'''
pin = input('Sisesta PIN-kood: ')

if pin  == '1234':
    print('Õige kood! Sisenesid meie süsteemi.')
else:
    print('Vale kood! Enesehävitusreziim aktiveeritud...')
'''

#Variant 2
print('Õige kood! Sisenesid meie süsteemi.' if input('Sisesta PIN-kood: ') == '1234' else 'Vale kood! Enesehävitusreziim aktiveeritud...')
