#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:56:48 2022

@author: ryong
"""

'''
1. 피보나치 수열 출력하기
   피보나치 수열은 0,1로 시작하고
   앞의 두수를 더하여 새로운 수를 만들어 주는 수열을 의미한다.
   피보나치 수열의 갯수를 입력받아 피보나치 수열을 갯수만큼 저장한
   리스트를 생성하는 함수 fibo 함수를 작성하기
   
   0 1 1 2 3 5 8 13 21 34 55 89 ....  
[결과]
피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) :10
fibo( 10 )=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]   
'''
num = int(input("피보나치 수열의 요소 갯수를 입력하세요(3이상의 값) : "))

x = [0,1]
y = []

if num < 2:
    print(x[0])
elif num <3:
    print(x[0], x[1])
else:
    for i in range(2,num):
        y = x[-1] + x[-2]
        x.append(y)

print("fibo(%d)=" % num, end="")
print(x)









'''
2. 주어진 자연수 N에 대해 N이 짝수이면 N!을,  홀수이면 ΣN을 구하는 코드를 작성하기
  4 : 4! = 4*3*2*1 = 24
  5 : Σ5 = 5+4+3+2+1 = 15
'''
evennumbers=1
oddnumbers=0
N=int(input("자연수를 입력하세요: "))
if (N % 2 == 0 ):
    for i in range(N, 0, -1):
        evennumbers *= i
    print(evennumbers)
elif (N % 2 == 1 ):
    for i in range(N, 0, -1):
        oddnumbers += i
    print(oddnumbers)
        
#print가 for구문안에 있어서 계속 반복됨












'''
3. 입력된 자연수가 홀수인지 짝수인지 판별해 주는 함수를 람다식을 이용하여 작성하기.
[결과]
자연수를 입력하세요 : 20
20 숫자는 짝수 입니다.

자연수를 입력하세요 : 25
25 숫자는 홀수 입니다.
'''

num = int(input("자연수를 입력하세요: "))
if num % 2 == 0:
    print("%d 숫자는 짝수 입니다." % num)
else :
    print("%d 숫자는 홀수 입니다." % num)


#람다식
b1 = lambda x:x%2==1
b2 = int(input('number : '))

if b1(b2) == True:
    print('%d 숫자는 홀수 입니다.' % b2)
else:
    print('%d 숫자는 짝수 입니다.' % b2)










'''
4. 화면에서 주민등록번호를 000000-0000000 형태로 입력받는다.
   주민등록번호 뒷자리의  첫 번째 숫자는 성별을 나타낸다. 
   주민등록번호에서 성별을 나타내는 숫자를 조회하여
   성별을 나타내는 숫자가 1,3 이면 남자로 2,4면 여자로 출력한다. 
   그외는 내국인아님으로 출력한다.
   -이 없는 경우는 '주민번호 입력오류' 출력하기
'''

id_num=input("주민등록번호를 000000-0000000 형태로 입력하세요: ")
try :
    idx = id_num.index("-")
except :
    print("주민번호 입력오류")
if  id_num[7] == '1' or id_num[7] =='3': 
    print("남자")
elif id_num[7] == '2' or id_num[7] =='4':
    print("여자")
else : 
    print("내국인아님")

#왜 남자가 나오는거냐..   
    
'''
5. 소문자와 숫자로 이루어진 문자를 암호화 하고 복호화 하는 프로그램 작성하기
  원래 문자 : a b c d e f g h i j k l m n o p q r s t u v w x y z 
  암호 문자 : ` ~ ! @ # $ % ^ & * ( ) - _ + = | [ ] { } ; : , . /

  원래 숫자 : 0 1 2 3 4 5 6 7 8 9 
  암호 숫자 : q w e r t y u i o p

[결과]
문자를 입력하세요 : abc123
암호화
`~!wer
복호화
abc123
'''    
origin="abcdefghijklmnopqrstuvwxyz0123456789"
cng_num="`~!@#$%^&*()-_+=|[]{};:,./qwertyuiop"
secrte=input("문자를 입력하세요(알파벳소문자&숫자0~9) : ")
result=""
for i in range(0, len(secrte)):
      result += cng_num[origin.find(secrte[i])]            
print("암호화=",result)  
secrte = result
result=""
for i in range(0, len(secrte)):
      result += origin[cng_num.find(secrte[i])]          
print("복호화=",result)










'''
6. 16진수를 입력하면 16진수 인지 아닌지 판단하여
   16진수가 맞으면 10진수로 변경하기.
   16진수가 아닌 경우 16진수 아님을 출력하기
'''
num = input("16진수 입력 : ")
try:
    num_16 = int(num,16)
except ValueError :
    print("16진수 아님")
else:
    print(num_16)


var = (input("16진수 입력 :"))

if ('0' <= var <= '9') or ('A' <= var <= 'F') or ('a' <= var <= 'f') :
    print("10진수 ==> ",int(var,16))
else :
    print("16진수가 아닙니다.")
#이건 한자리만 가능한 코드 구글링한건데 이건 문제가 있는 코드

hexa = input("16진수를 입력하세요 : ")
if "0x" in hexa:
    print(int(hexa,16))
else:
    print("16진수 아님")
#시현이 답인데 이게 직관적이고 이해하기 쉬운 코드라고 느낌 참고하겠음.








