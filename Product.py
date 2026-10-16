name = input('Sisesta toote nimi: ').lower()

product = ''
price = 0.0

if name.lower() == 'maasikas':
    product = name
    price = 5
elif name.lower() == 'vaarikas':
    product = name
    price = 5.2

print(product.capitalize() + ' maksab ' + str(price) + ' eurot.' if product != '' else 'Toode ei ole saadaval.')
