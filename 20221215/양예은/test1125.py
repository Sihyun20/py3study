# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:09:40 2022

@author: 예은
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
a = input("한개의 문자를 입력하세요 :")
if a.isdigit():
    print("%c + 20 = %d" % (a,int(a)+20))
elif a.isupper():
    print("%c 문자의 대문자는 %c" % (a,a.lower()))
elif a.islower():
    print("%c 문자의 대문자는 %c" % (a,a.upper()))


'''
2 (1)+(1+2)+(1+2+3)+... (1+2+3+...10)=220 출력하기
[결과]
(1)+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)+(1+2+3+4+5+6+7)+(1+2+3+4+5+6+7+8)+(1+2+3+4+5+6+7+8+9)+(1+2+3+4+5+6+7+8+9+10)=220
'''
sum=0
for i in range (1,11) : # 1~10
    print("(",end="")
    for j in range (1,i+1) : 
        print(j, end="")
        if(j!=i) : 
            print("+",end="")
        sum += j
    print((")=" if i==10 else ")+"),end="")
print(sum)

'''
3. 화면에서 자연수를 입력받아 각각의 자리수의 합을 구하기.
[결과]
자연수를 입력하세요 : 12345
자리수 합 : 15
'''
num = int(input("자연수를 입력하세요 : "))
hap = 0
a = num
while(a > 0):
    hap += a % 10
    a //= 1
print(num,"자리수의 합 :",hap)

'''
4. aa,bb 리스트를 생성하고,
aa 리스트는 0부터 짝수 100개를 저장하고
bb 리스트는 aa 배열의 역순으로 값을 저장하기.
aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기
[결과]
aa[ 0]= 0,aa[ 1]= 2,aa[ 2]= 4,aa[ 3]= 6,aa[ 4]= 8,aa[ 5]=10,aa[ 6]=12,aa[ 7]=14,aa[ 8]=16,aa[ 9]=18,
bb[99]= 0,bb[98]= 2,bb[97]= 4,bb[96]= 6,bb[95]= 8,bb[94]=10,bb[93]=12,bb[92]=14,bb[91]=16,bb[90]=18,
'''

aa = [x*2 for x in range(0,100)] 
bb = [x*2 for x in range(99,-1,-1)] 
aa
len(aa)
bb
len(bb)
print(aa[:10])
for i in range(0,10) :
    print("aa[%2d]=%2d" % (i,aa[i]), end=",")

print(bb[len(bb)-1:len(bb)-11:-1])
print(bb[-1:-11:-1])

for i in range(len(bb)-1,len(bb)-11,-1) :
    print("bb[%2d]=%2d" % (i,bb[i]), end=",")  


'''
5. 다음 모레시계모양을 출력하기
[결과]
모래시계의 높이를 홀수로 입력하세요 : 5
*****
 ***
  *
 ***
*****
'''

row = int(input("모래시계의 높이를 홀수로 입력하세요 :"))
for i in range(0,row//2+1):
    print(" "*i,end="")
    print("*"*(row-(i*2)))
for i  in range(row//2+1,row):
    print(" "*(row-i-1),end="")
    print("*"*(row-(row-i)*2+2))
    
    
'''
 6. 나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
 등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
 나라 입력시 "종료" 입력되면 프로그램 종료.
 종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
'''

country = {}
while True :
    indata = input(str(list(country.keys())) +\
                   " 수도를 알고 싶은 나라는(종료)?")
    if indata in country :
        print("<%s> 나라의 수도는 <%s>입니다."  %(indata,country.get(indata)))
    elif indata=="종료" :
        break
    else :  
        print("등록된 나라가 아닙니다.")
        yn = input("수도를 등록하시겠습니까?(y/n)")
        if yn == 'y' :
            f = input("수도이름을 입력하세요 : ")
            country[indata] = f

print("등록된 나라:")
for i in country.keys() :
   print("%s => %s " % (i,country[i]))



"""
7. 화면에서 숫자를 입력받아 야구 게임하기
   시스템이 서로다른 임의의 숫자 4개를 저장
   화면에서 숫자4자리를 입력받아 스트라익, 볼을 출력
   정답 입력시 종료. 
"""
# 숫자야구는 알지만 코딩하기에 너무 어려워서
#구글링해서 가져오긴 했는데 계속 보면서 이해하는중...

import random

num1 = set()
while(len(num1)<4):
    num1.add(random.randrange(0,10))
num = list(num1)
print(num)
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
    
    
    
    
    
    
    