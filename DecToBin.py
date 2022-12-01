def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')

def BinaryToDecimal(num):
    decimal, i = 0, 0
    while(num != 0):
        dec = num % 10
        decimal = decimal + dec * pow(2, i)
        num = num//10
        i += 1
    print(decimal)




DecimalToBinary(359)
print("\n")
BinaryToDecimal(101100111)