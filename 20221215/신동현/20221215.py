# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 14:56:51 2022
@author: KITCOOP
test1125.py
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

ch = input("한개의 문자를 입력하세요 : ")
if ch.isdigit() :  
   print("%c + 20 = %d" % (ch,int(ch) + 20))
elif ch.isupper() : 
   print("%c 문자의 소문자는  %c" % (ch,ch.lower()))
elif ch.islower() :  
   print("%c 문자의 대문자는  %c" % (ch,ch.upper()))



'''
2 (1)+(1+2)+(1+2+3)+... (1+2+3+...10)=220 출력하기
[결과]
(1)+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)+(1+2+3+4+5+6+7)+(1+2+3+4+5+6+7+8)+(1+2+3+4+5+6+7+8+9)+(1+2+3+4+5+6+7+8+9+10)=220
'''
hap= 0
for i in range(1,11):
    print("(",end="")
    for j in range(1,i+1):
        print(j,end = "")
        if(j!=i) :#이거 이해가 안감 왜 !=지?
            print("+",end="")
        hap += j
    print((")=" if i == 10 else ")+"),end="") #줄 위치에 따라 다르게 나옴
print(hap)

#명신김님꺼 보고 따라함 ㅠ
'''
3. 화면에서 자연수를 입력받아 각각의 자리수의 합을 구하기.
[결과]
자연수를 입력하세요 : 12345
자리수 합 : 15
'''
print('자연수를 입력하세요')
num = int(input())
sum=0
tmp = num

while (tmp>0) : #()<을 빼먹음
    sum += tmp%10
    tmp //= 10
print('자리수 합:',sum)

'''
4. aa,bb 리스트를 생성하고,
aa 리스트는 0부터 짝수 100개를 저장하고
bb 리스트는 aa 배열의 역순으로 값을 저장하기.
aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기
[결과]
aa[ 0]= 0,aa[ 1]= 2,aa[ 2]= 4,aa[ 3]= 6,aa[ 4]= 8,aa[ 5]=10,aa[ 6]=12,aa[ 7]=14,aa[ 8]=16,aa[ 9]=18,
bb[99]= 0,bb[98]= 2,bb[97]= 4,bb[96]= 6,bb[95]= 8,bb[94]=10,bb[93]=12,bb[92]=14,bb[91]=16,bb[90]=18,
'''
aa=[x*2 for x in range(0,100)]
print(aa)
bb=[x*2 for x in range(0,100)]
bb.reverse()
print(bb)
len(aa)
len(bb)
for i in range(0,11):
    print("aa[",i,"]=",aa[i],",")
for i in range(0,11):
    print("bb[",100-i,"]=",bb[i],",") #가로 출력을 어떻게 해야할지 모르겠음...
'''
5. 다음 모레시계모양을 출력하기
[결과]
모래시계의 높이를 홀수로 입력하세요 : 5
*****   0 / 5 / 0 h=1 공백(0)= h-1
 ***    1 / 3 / 1 h=2 공백(1)= h-1
  *     2 / 1 / 2 h=3 공백(2)= h-1  
 ***    1 / 3 / 1 h=4 공백(1)= h-3
*****   0 / 5 / 0 h=5 공백(0)= h-5
'''
print('모래시계의 높이를 홀수로 입력하세요 : ')
h = int(input())
for i in range(h) : 
    if h // 2> i :
        print(" "*i, end="")
        print("*"*(h-1*i-1))
    else:
        print(" "*(h - i -1),end="")
        print("*"*((2*i)-h//2-1))
#자세히 안보면 티 안남 일단 성공 ㅎ

'''
 6. 나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
 등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
 나라 입력시 "종료" 입력되면 프로그램 종료.
 종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
'''
country = {}
while True : 
    indata = input(str(list(country.keys()))+ " 나라명 검색:")
    if indata in country : 
        print("<%s> 나라의 수도는 <%s>입니다." %(indata,country.get(indata)))
    elif indata == "종료" :
        break
    else : 
        print("등록된 나라가 아닙니다.")
    yn = input("수도를 등록하시겠습니까?(y/n)")
    if yn == 'y' :
        f = input("수도이름을 입력하세요 :")
        country[indata]= f
        
print("등록된 나라:")
for i in country.keys() :
    print("%s => %s" % (i,country[i]))
        
#하나도 모르겠어서 선생님꺼 따라 씀....

"""
7. 화면에서 숫자를 입력받아 야구 게임하기
   시스템이 서로다른 임의의 숫자 4개를 저장
   화면에서 숫자4자리를 입력받아 스트라익, 볼을 출력
   정답 입력시 종료. 
"""

print("숫자야구 게임에 오신 여러분 환영합니다.")

import random #파이썬 랜덤 모듈
correct_number = ["0", "0", "0", "0"] #파이썬에서 input() 함수의 사용자 입력은 문자열이므로 "0" 문자열로 배열
correct_number[0] = str(random.randrange(1, 10, 1))
correct_number[1] = correct_number[0]
correct_number[2] = correct_number[0]
correct_number[3] = correct_number[0]

# 랜덤 숫자가 같다면 계속 반복
while(correct_number[0] == correct_number[1]):
    correct_number[1] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[2] or correct_number[1] == correct_number[2]):
    correct_number[2] = str(random.randrange(1, 10, 1))
while(correct_number[0] == correct_number[3] or correct_number[1] == correct_number[3] or correct_number[2] == correct_number[3]):
    correct_number[3] = str(random.randrange(1, 10, 1))

print(correct_number)

try_number = 0
strike_number = 0
ball_number = 0

print("숫자야구를 시작합니다.")
print("--------------------------")
while (strike_number < 4):

    number = str(input("숫자 4자리를 입력하세요: "))

    strike_number = 0
    ball_number = 0

    for i in range(0, 4): # i 값의 범위 0~3
        for j in range(0, 4):
            if(number[i] == str(correct_number[j]) and i == j):
                strike_number += 1
            elif(number[i] == str(correct_number[j]) and i != j):
                ball_number += 1
    print("결과: [",strike_number,"]스트라이크 [",ball_number,"]볼")
    try_number += 1

print("--------------------------")
print("축하합니다! 정답입니다!")
print("[",try_number,"]번 만에 맞췄습니다")
