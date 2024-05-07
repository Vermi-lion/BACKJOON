# rjust함수를 이용해 오른쪽 정렬 방법
a = int(input())

for star in range(1, a + 1) :
    star = '*' * star
    print(star.rjust(a))


# 공백을 주는 방법
a = int(input())

for star in range(1, a + 1) :
    space = ' ' * (a - star)
    star = '*' * star
    print(space + star)