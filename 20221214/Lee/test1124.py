# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:58:40 2022

@author: KITCOOP
test1124_a.py
"""

'''
1. 삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램을 작성

[결과]
삼각형의 높이를 입력하세요 : 5 
    *         공백 :4=h-1       * : 1  =  1*2-1
   ***        공백 :3=h-2       * : 3  =  2*2-1
  *****       공백 :2=h-3       * : 5  =  3*2-1
 *******
*********

공백 4 3 2 1 
* 1 3 5 7 9
'''
h=5
for i in range(0,h+1) :
    print(" "*(h-i),end="")
    print("*"*((i*2)-1))

#우연히 풀었다고 봐야되나..
#위에 공백과 * 옆에 쓰여진거 넣어보다 됨.






































row = int(input("삼각형의 높이를 입력하세요"))
for i in range(1,row+1) : #1~삼각형의 높이
    print(" "*(row-i),end="")
    print("*"*(i*2-1))

'''
2. 년도를 입력받아 윤년인지 평년인지 출력하기.
윤년은 4로 나누어 떨어지고, 100 나누어 떨어지지 않거나, 
400으로 나누어 떨어지면 윤년.
그외는 평년

년도를 입력하세요 : 2020
2020년은 윤년입니다.

년도를 입력하세요 : 2021
2021년은 평년입니다.
'''

year=int(input("년도를 입력하세요"))
if((year%4==0) and (year%100!=0) or (year%400==0)):
    print(str(year)+"년은 윤년입니다.")
else:
    print(str(year)+"년은 평년입니다.")
    
#and or 직접쓸것  




































year = int(input("년도를 입력하세요 : "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) :
    yun = '윤년'
else :
    yun = '평년'
print(year,"년은 ",yun,"입니다.")


if year % 400 == 0 :
    yun = '윤년'
elif (year % 4 == 0)  and (year % 100 != 0) :
    yun = '윤년'
else :    
    yun = '평년'

print(year,"년은 ",yun,"입니다.")
    
'''
3. 1 부터 1000 까지의 홀수의 합계 계산시 
최초로 1000이 넘는 숫자는 
구하는 프로그램을 작성해 보자.
'''
hap=0
for i in range(1,1000+1) :
    if i % 2== 1 :
       hap += i
    if hap >= 1000:
        break
        print("%d" % hap)
##왜 안나올까 천넘으면 멈추고 그 값을 내보내인데 왜안되는거









































hap,i = 0,0  
for i in range(1,1001,2) :  # i : 1,3,5,7,9....999
    hap += i  
    if hap >= 1000 :
         break  
print("1~1000의 홀수의 합에서 최초로 1000이 넘는 위치 : %d, \
      합계: %d" % (i,hap))


"""
4. 화씨온도= (( 9 / 5) * 섭씨온도) + 32 인 경우 섭씨
 -20 ~ 50 도까지를 화씨 온도로 변경하여 작성하기
"""

tempe = int(input("온도를 입력하세요"))
if (-20 <= tempe <= 50):
    h = (( 9 / 5) * tempe) + 32
    print("화씨온도"+str(h))
else:
    print("섭씨온도"+str(tempe))






































for c in range(-20,51) :  #c: -20 ~ 50 
    print("섭씨온도:",c,",화씨온도:",((9/5) * c) + 32)

'''
5. 금액을 입력받아 동전(500,100,50,10,1)으로 바꿔 주는 프로그램 작성하기
           동전의 갯수를 최소개로한 각각의 동전의 갯수를 구하는 프로그램 작성하기
금액을 입력하세요: 3750
500원동전 : 7개
100원동전 : 2개
50원동전 :  1개
10원동전 :  0개
1원동전  :  0개
'''


won = int(input("금액을 입력하세요:"))
num1=won//500
num2=won%500
print("500원동전 : "+str(num1)+"개")
num2
num3=num2//100
num4=num2%100
print("100원동전 : "+str(num3)+"개")
num5=num4//50
num6=num4%50
print("50원동전 : "+str(num5)+"개")
num7=num6//10
num8=num6%10
print("10원동전 : "+str(num7)+"개") 
num9=num8//1
num10=num8%1
print("1원동전 : "+str(num9)+"개")






































money = int(input("금액을 입력해주세요 : "))
temp = money
print("500원 동전의 갯수:",temp//500,"개")
temp %= 500                             
print("100원 동전의 갯수:",temp//100,"개")
temp %= 100                             
print("50원 동전의 갯수:",temp//50,"개")  
temp %= 50                              
print("10원 동전의 갯수:",temp//10,"개") 
temp %= 10                              
print("1원 동전의 갯수:",temp,"개")      

print()
# [500,100,50,10,1] : 리스트표시
temp = money
for m in [500,100,50,10,1] : #m:500,100,50,10,1
    print("%d원 동전의 갯수: %d" % (m,temp//m),"개")
    temp = temp % m

'''
6. 구구단 가로로 출력하기

2X 2=  4  3X 2=  6  4X 2=  8  5X 2= 10  6X 2= 12  7X 2= 14  8X 2= 16  9X 2= 18 
2X 3=  6  3X 3=  9  4X 3= 12  5X 3= 15  6X 3= 18  7X 3= 21  8X 3= 24  9X 3= 27 
...   
...


'''

for i in range(2,10):
    for j in range(2,10):
      print("%dX%2d=%3d" % (i,j,(i*j)) ,end="\t")
      
#가로출력으로 어떻게 바꿔야될지...




































for i in range(2,10) :
    print("%5d단%3s" % (i," "),end="") # %3s : 공백문자열 3자리 출력.
print()
for j in range(2,10) :  # 2
    for i in range(2,10) :     # 2
        print("%2dX%2d=%3d " % (i,j,(i*j)),end="")
    print()  

