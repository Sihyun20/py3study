# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 20:43:58 2022

@author: 예은
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
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
n = int(input("피보나치 수열의 요소 개수를 입력하세요(3 이상의 값) : "))
print("fibo(",n,") = ", end="")
fi = fibo(n)
print(fi)

'''
2. 주어진 자연수 N에 대해 N이 짝수이면 N!을,  
   홀수이면 ΣN을 구하는 코드를 작성하기
  4 : 4! = 4*3*2*1 = 24
  5 : Σ5 = 5+4+3+2+1 = 15
'''
def fac(n):
    if(n==1):
        return 1
    else:
        return n * fac(n-1)

def sig(n):
    if(n==1):
        return 1
    else:
        return n+sig(n-1)
    
n = int(input("자연수를 입력하세요 : "))
if(n%2==0):
    print(n,":",str(n)+"! = ", fac(n))
else:
    print(n,": Σ"+str(n),"=", sig(n))
    


'''
3. 입력된 자연수가 홀수인지 짝수인지 판별해 주는 함수를
   람다식을 이용하여 작성하기.
[결과]
자연수를 입력하세요 : 20
20 숫자는 짝수 입니다.
자연수를 입력하세요 : 25
25 숫자는 홀수 입니다.
'''

num = int(input("자연수를 입력하세요"))
if (num & 2 == 1):
    print(num,"숫자는 홀수 입니다.")
else:
    print(num,"숫자는 짝수 입니다.")

    


'''
4. 화면에서 주민등록번호를 000000-0000000 형태로 입력받는다.
   주민등록번호 뒷자리의  첫 번째 숫자는 성별을 나타낸다. 
   주민등록번호에서 성별을 나타내는 숫자를 조회하여
   성별을 나타내는 숫자가 1,3 이면 남자로 2,4면 여자로 출력한다. 
   그외는 내국인아님으로 출력한다.
   -이 없는 경우는 '주민번호 입력오류' 출력하기
'''
jumin = input("주민등록번호 000000-0000000 형태로 입력 :")
jumin = jumin.split("-")[1]
if jumin[0] == "1" or jumin[0] =="3":
        print("남자")
elif jumin[0] == "2" or jumin[0] =="4":
        print("여자")
else:
        print("내국인 아님")
    
    
    
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

# 구글링으로도 이해가 안됨... 강사님 코드보면서 이해하는 중
plain = "abcdefghijklmnopqrstuvwxyz0123456789" 
cyper = "`~!@#$%^&*()-_+=|[]{};:,./qwertyuiop"

src = input("문자를 입력하세요 : ")
result = ""
for i in range(0,len(src)):
    result += cyper[plain.find(src[i])]
print("암호화")
print(src,"=",result)

src = result
result = ""
for i in range(0,len(src)):
    result += plain[cyper.find(src[i])]

print("복호화")
print(src,"=",result)

'''
6. 16진수를 입력하면 16진수 인지 아닌지 판단하여
   16진수가 맞으면 10진수로 변경하기.
   16진수가 아닌 경우 16진수 아님을 출력하기
'''

num16 = input("16진수 입력:")

if "0x" in num16:
    print(int(num16,16))
else:
    print("16진수 아님")
    


    








