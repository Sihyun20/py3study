# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 11:51:00 2022

@author: Galaxy Book Ion
"""


#1
def fibo(n):
    f = [0 for i in range(n)] #그냥 f=[] 로 하면 오류남. 왜 꼭 개수를 지정해줘야하는지?
    f[0] = 0  
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f

n = int(input("피보나치 수열의 요소 개수를 입력하세요(3 이상의 값) : "))
print("fibo(",n,") = ", end="")
fi = fibo(n)
print(fi)



#2
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




#3
x = int(input("자연수를 입력하세요 : "))
lb = lambda x: x%2 != 0
if lb(x):
    print('odd')
else:
    print('even')



#4
num = list(input().split('-'))
gen = num[1][0:1]
if(gen == '1' or gen == '2'):
    print("남자")
if(gen == '3' or gen == '4'):
    print("여자")



#5
# 문자열도 인덱스가 되는걸 완전히 까먹고 있었음
ori="abcdefghijklmnopqrstuvwxyz0123456789"
enc="`~!@#$%^&*()-_+=|[]{};:,./qwertyuiop"


x = input("input : ")
result = ""
for i in range(len(x)):
    idx = ori.find(x[i])
    result += enc[idx]

print("암호화")
print(result)
print("복호화")
print(x)



#6
hexa = input("16진수를 입력하세요 : ")
if "0x" in hexa:
    print(int(hexa,16))
else:
    print("16진수 아님")