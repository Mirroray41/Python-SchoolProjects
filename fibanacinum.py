mem, a0, a1 = 0, 0, 1
count = int(input("How many?:")) 
if count < 0: count *= -1
print("0\n1")
while count >> 1:
    count-=1
    mem = a0 + a1
    a0, a1 = a1, mem
    print(mem)
print("\n" + str(a1))