# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 21:48:22 2022

@author: Galaxy Book Ion
"""

#1
'''
h = 5
1   4 1    (h-i)  (2i-1)
2   3 3
3   2 5
4   1 7
5   0 9

'''
h = int(input("높이를 입력하세요 : "))

for i in range(1,h+1):
    print(" "*(h-i), end="")
    print("*"*(2*i-1))


#2
year = int(input("년도 입력 : "))

if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 ==0):
            print(str(year),"년은 윤년입니다.")
        else:
            print(str(year),"년은 평년입니다.")
    else:
        print(str(year),"년은 윤년입니다.")

#3
sum = 0
for i in range(1, 1001):
    if(i%2 !=0):
        sum += i
    if(sum >= 1000):
        print(i)
        break

#4
for i in range(-20,51):
    f = ((9/5)*i)+32
    print("섭씨"+str(i)+"도 =", f)
    
#5
mon = int(input("금액을 입력하세요 : "))
m500 = mon//500
print("500원 동전 :",m500)
m100 = mon%500//100
print("100원 동전 :",m100)
m50 = mon%100//50
print("50원 동전 :",m50)
m10 = mon%50//10
print("10원 동전 :",m10)
m1 = mon%10
print("1원 동전 :",m1)

#6
for i in range(2,10):
    print("")
    for j in range(2, 10):
        print(str(j)+" X "+str(i)+" =", j*i, end="\t")
        






























    