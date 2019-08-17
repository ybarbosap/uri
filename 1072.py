n = int(input())

entre = 0
fora = 0

for e in range(n):
    v = int(input())

    if v < 10000:

        if v >= 10 and v <= 20:
            entre += 1
        else:
            fora += 1

print("{} in".format(entre))
print("{} out".format(fora))