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

char= input("한개의 문자를 입력하세요: ")
if char.isdigit() :
    print("%d + 20 = %d" % (int(char),20+int(char)))
if char.isupper() :
    print("대문자: %c" % char)
if char.islower() :
    print("소문자: %c" % char)
else :
    print("올바른 형식이 아닙니다.")





'''
2 (1)+(1+2)+(1+2+3)+... (1+2+3+...10)=220 출력하기

[결과]
(1)+(1+2)+(1+2+3)+(1+2+3+4)+(1+2+3+4+5)+(1+2+3+4+5+6)+(1+2+3+4+5+6+7)+(1+2+3+4+5+6+7+8)+(1+2+3+4+5+6+7+8+9)+(1+2+3+4+5+6+7+8+9+10)=220
'''

num = int(input("숫자를 입력하세요"))
hap = 0
hap_hap = 0
for i in range(1,num+1) :
    hap += i
    hap_hap = hap_hap+hap
print ("1부터 %d까지의 합:%d" % (num,hap_hap))

#수열 누적식을 출력하기 위해서 중첩 반복문을 어떻게 쓰면 될거같은데..모르겠음








'''
3. 화면에서 자연수를 입력받아 각각의 자리수의 합을 구하기.

[결과]
자연수를 입력하세요 : 12345
자리수 합 : 15
'''
print(sum(map(int, input('자연수를 입력하세요: '))))









'''
4. aa,bb 리스트를 생성하고,
aa 리스트는 0부터 짝수 100개를 저장하고
bb 리스트는 aa 배열의 역순으로 값을 저장하기.
aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기

[결과]
aa[ 0]= 0,aa[ 1]= 2,aa[ 2]= 4,aa[ 3]= 6,aa[ 4]= 8,aa[ 5]=10,aa[ 6]=12,aa[ 7]=14,aa[ 8]=16,aa[ 9]=18,
bb[99]= 0,bb[98]= 2,bb[97]= 4,bb[96]= 6,bb[95]= 8,bb[94]=10,bb[93]=12,bb[92]=14,bb[91]=16,bb[90]=18,
'''

aa=[x for x in range(0,101) if (x%2==0)]
print(aa)
aa.reverse()
print(aa)
bb = aa
print(bb)







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












'''
 6. 나라와 수도를 등록하고 화면에 나라이름을 입력받아 해당 나라의 수도를 출력하기
 등록된 나라가 아닌 경우 수도를 입력받아 등록하기.
 나라 입력시 "종료" 입력되면 프로그램 종료.
 종료시 등록된 모든 나라와 수도정보를 화면 출력하기. 
'''
capital={"대한민국":"서울","프랑스":"파리","영국":"런던"}
while True :
    capi=input(str(list(capital.keys())) + "입력시 수도 출력됨(종료):")
    if capi == '종료' :
        break
    if capi in capital :
        print("%s의 수도는 %s" % (capi,capital[capi]))
    else :
        print("%s는 등록된 나라가 아닙니다" % capi)
        y = input(capi+"를 등록하시겠습니까?(y/n)")
        if y.upper() == 'Y' :
            capi2 = input(capi +"의 수도는? :")
            capital[capi] = capi2
print("등록된 나라:")
for c in capital.items():
    print(c[0],":",c[1])
    















"""
7. 화면에서 숫자를 입력받아 야구 게임하기
   시스템이 서로다른 임의의 숫자 4개를 저장
   화면에서 숫자4자리를 입력받아 스트라익, 볼을 출력
   정답 입력시 종료. 
"""
mylist=()
import random
rnum = random.randrange(0,10) 
for i in set(range(1,5)) :
    rrnum = random.randrange(0,10)
 
B, A, S, E = set(int, input("0~9까지 중에서 4개의 숫자를 입력하세요(중복불가)").split()) 
print(B, A, S, E)













