def analizer_amount(amount):
    return f'We are the bank and you are {'ACCEPTED' if amount >= 100 else 'DENIED'}'


analysis = analizer_amount(150)
print(analysis)