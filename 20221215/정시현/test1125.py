# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:42:55 2022

@author: Galaxy Book Ion
"""

'''
1. 화면에서 한개의 문자를 입력받아 대문자인 경우는 소문자로, 
   소문자인 경우는 대문자로 숫자인 경우는 20을 더한 값을 출력하기
[결과]
한개의 문자를 입력하세요 : 1
1 + 20 = 21
한개의 문자를 입력하세요 : a
a 문자의 대문자는 A
한개의 문자를 입력하세요 : A
A 문자의 소문자는 a
'''

while(True):
    x = input("한개의 문자를 입력하세요(종료) : ")
    if(x == "종료") :
        break
    if x.isdigit() :
        print(x+" + 20 =",(int(x)+20))
    elif x.isupper() :
        print(x+" 문자의 소문자는 : "+x.lower())
    elif x.islower() :
        print(x+" 문자의 대문자는 : "+x.upper())


'''
2 (1)+(1+2)+(1+2+3)+... (1+2+3+...10)=220 출력하기
[결과]
(1)+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)+(1+2+3+4+5+6+7)+(1+2+3+4+5+6+7+8)+(1+2+3+4+5+6+7+8+9)+(1+2+3+4+5+6+7+8+9+10)=220
'''

s = 0
for i in range(1,11):
    print("(", end="")
    for j in range(1,i+1):
        print(j, end="")
        s += j
        if(j != i):
            print("+", end="")    
        if(j == i):
            print("", end="")     
    if(i < 10):
        print(")+", end="")
    else:
        print(") =", s)

    
'''
3. 화면에서 자연수를 입력받아 각각의 자리수의 합을 구하기.
[결과]
자연수를 입력하세요 : 12345
자리수 합 : 15
'''

n = int(input("자연수를 입력하세요 : "))
s = sum(map(int, str(n)))
print("자리수 합 :",s)


'''
4. aa,bb 리스트를 생성하고,
aa 리스트는 0부터 짝수 100개를 저장하고
bb 리스트는 aa 배열의 역순으로 값을 저장하기.
aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기
[결과]
aa[ 0]= 0,aa[ 1]= 2,aa[ 2]= 4,aa[ 3]= 6,aa[ 4]= 8,aa[ 5]=10,aa[ 6]=12,aa[ 7]=14,aa[ 8]=16,aa[ 9]=18,
bb[99]= 0,bb[98]= 2,bb[97]= 4,bb[96]= 6,bb[95]= 8,bb[94]=10,bb[93]=12,bb[92]=14,bb[91]=16,bb[90]=18,
'''


aa = [x for x in range(200) if x%2==0]
bb = [x for x in reversed(range(200)) if x%2==0]
for i in range(10):
    print("aa[",i,"] = ",aa[i],",", end=" ")
for i in range(10):
    print("bb[",(99-i),"] = ",aa[(99-i)],",", end=" ")


'''
5. 다음 모레시계모양을 출력하기
[결과]
모래시계의 높이를 홀수로 입력하세요 : 5
*****     0    0  5  h=3    공백 i개   * h-2i
 ***      1    1  3
  *       2    2  1
 ***      3 1  1  3  h=3    공백 (h-i-1)      * 2*(i-h//2)+1
*****     4 2  0  5
'''

h = int(input("모래시계의 높이를 홀수로 입력하세요 : "))
h2 = h//2 + 1
h2
for i in range(h2):
    print(" "* i, end="")
    print("*"* (h-2*i))
for i in range(h2,h):
    print(" "*(h-i-1), end="")
    print("*"*(2*(i-h//2)+1))


'''
 6. 나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
 등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
 나라 입력시 "종료" 입력되면 프로그램 종료.
 종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
'''

country = {}
while(True):
    con = input("나라 이름을 입력하세요(종료) : ")
    if(con == '종료'):
        break
    if(con in country):
        print(country[con])
    else:
        cap = input("수도 이름을 입력하세요 : ")
        country[con] = cap

print("등록된 나라 정보 : ")
for c in country:
    print(c," : ",country[c])


"""
7. 화면에서 숫자를 입력받아 야구 게임하기
   시스템이 서로다른 임의의 숫자 4개를 저장
   화면에서 숫자4자리를 입력받아 스트라익, 볼을 출력
   정답 입력시 종료. 

상대방이 가진 카드, 내가 부르는 카드 비교
자리, 숫자 같으면 스트라이크
숫자만 같으면 볼

"""

import random

num = []
for i in range(4):
    num.append(random.randrange(0,10))
cnt = 0

while(True):
    mnum = list(map(int, input("숫자 네개를 입력하세요(띄어쓰기로 구분) : ").split()))
    o = 0
    s = 0
    b = 0
    cnt += 1

    for i in range(4):
        if(num[i] == mnum[i]):
            s += 1
        elif(mnum[i] in num):
            b += 1
        else:
            o += 1

    if(o == 4):
        print("아웃")
    else:
        print("%ds, %2db" % (s,b))

    if(s == 4):
        break;

print(str(cnt)+"번만에 승리")












