
def reg_symb(x):
    if x <= 90 and x >= 65:
        return True
    if x <= 122 and x>= 97:
        return False
    else:
        return None

symbol = 'A'
check_reg_symb = lambda symbol : f'{symbol}: {reg_symb(ord(symbol))}'
print(check_reg_symb(symbol))

sentence = 'OQIFEnownelvjw;soeiwoie 082459203'

for value in sentence:
    symbol = value
    symbol_num = reg_symb(ord(symbol))
    print(check_reg_symb(symbol))

