mem, a0, a1, count = 0, 0, 1, int(input("How many?:"))
if count < 0: count *= -1
print("0\n1")
while count >> 1:
    mem =  a0 + a1
    a0, a1, count = a1, mem, count - 1
    print(mem)
print("\n" + str(a1))