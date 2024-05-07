a = int(input())

for star in range(1, a + 1) :
    star = '*' * star
    print(star.rjust(a))