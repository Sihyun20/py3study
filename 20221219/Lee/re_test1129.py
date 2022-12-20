#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:44:46 2022

@author: ryong
"""
'''
클래스에서 사용되는 연산자에 사용되는 특수 함수
+   __add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)

생성자 : __init__(self,...) : 클래스 객체 생성시 요구되는 매개변수에 맞도록 매개변수 구현
출력   : __repr__(self) : 클래스의 객체를 출력할때 문자열로 리턴.
'''
'''
   추상함수 : 자손클래스에서 강제로 오버라이딩 해야 하는 함수
             함수의 구현부에 raise NotImplementedError
             를 기술함
'''


'''
1. main이 실행 되도록  Rect 클래스 구현하기
    가로,세로를 멤버변수로.
    넓이(area),둘레(length)를 구하는 멤버 함수를 가진다
    클래스의 객체를 print 시 :  (가로,세로),넓이:xxx,둘레:xxx가 출력
[결과]
(10,20), 넓이:200,둘레:60
(10,10), 넓이:100,둘레:40
200 면적이 더 큰 사각형 입니다.
'''    
    
class Rect :
    width=0
    height=0
    def __init__(self,width,height) :
        self.width = width
        self.height = height
    def area(self) :    
        return self.width * self.height
    def length(self) :  
        return (self.width + self.height) * 2
    def __lt__(self,other):
        return self.area() < other.area()
    def __gt__(self,other):
        return self.area() > other.area()
    def __eq__(self,other):
        return self.area() == other.area()
    def __repr__(self):
        return("(%d,%d), 넓이:%d,둘레:%d" \
               % (self.width,self.height,self.area(),self.length()))

if __name__ == '__main__' :
    rect1=Rect(10,10)
    rect2=Rect(10,10)
    print(rect1)
    print(rect2)
    if rect1 > rect2 :
        print("%s 면적이 더 큰 사가형 입니다." % rect1.area())
    elif rect1 < rect2 :       
        print("%s 면적이 더 큰 사가형 입니다." % rect2.area())
    elif rect1 == rect2 :       
        print("면적이 같은 사가형 입니다.")

#코드는 맞는거 같은 결과값 print가 __repr__이 왜 출력이 안되는지 모르겠음
#소스는 코드문제들 중 Car클래스문제 참고해서 클래스 만들었고 
#main부분은 __name__='__main__'이라는게 생소해서 답안 참고했음
#=>
#출력값이 여러개일때 ()로 묶어줘야함 꼭
#숫자요소 입력된 변수를 출력해줘야 문제의 결과값처럼 나올 수 있음 그래서
#print(rect1), print(rect2) 추가해줌 그러니까 출력됨.

class rectangle:
     def __init__(self,width,height):
         self.width = width
         self.height = height
     def area(self):
         return self.width*self.height
     def round(self):
         return(self.width + self.height)*2

a = int(input("가로 : "))
l = int(input("세로 : "))
r = rectangle(a,l)
print("둘레는 %d이고 넓이는 %d이다."%(r.round(),r.area()))
#예은이 코드 입력받아서 출력하는 로직?은 좋음


'''
2. main 이 실행 되도록, Calculator 클래스를 상속받은 
   UpgradeCalculator  클래스 구현하기
   
   Calculator  클래스
     value 멤버변수
     add 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 더하기
   UpgradeCalculator 클래스
     minus 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 빼기
'''   
 
class Calculator :
    value=0
    def add(self, other):
        self.value += other
        
class UpgradeCalculator(Calculator) :
    def minus(self, other):
        self.value -= other

main = UpgradeCalculator()
main.add(3)
main.minus(4)
print(main.value)

#에러가 나는데 왜 나는지 모르겠음
#TypeError: add() missing 1 required positional argument: 'other'
# => UpgradeCalculator() ()missing...omg





'''
3. 2번에서 구현한 Calculator 클래스를 이용하여 
   MaxLimitCalculator 클래스 구현하기
MaxLimitCalculator 클래스에서 value 값은 절대 100 이상의 값을 가질수 없다.
'''
    
class MaxLimitCalculator(Calculator) :
     def value1(self,v) :
        self.value += v
        if self.value > 100 :
            self.value = 99
        print("Max클래스value:%d" % self.value)

mlc = MaxLimitCalculator()
mlc.value1(200)

#+= 줄이 오류 unsupported operand type(s) for +=: 'method' and 'int'
#뭐가 문제인지 모르겠음 코드에 예시문제 car부분 참고한건데 type을 어떻게 고쳐야되는지 모르겠음
#=>#
#def함수 변수명이 value와 같아서 오류가 났었다 그러므로 변수명에 신경쓸것.
# Calculator를 상속했으니 value라는 변수명으로 값을 받아야 했는데 그렇게 안했었다.
#예시문제의 car를 보고하다보니 그런 오류를 범함.





'''
4. 다음 코드는 알파벳 대문자의 모스 부호를 저장한 딕셔너리 데이터입니다. 
대문자 알파벳을 입력받아 알파벳의 해당하는 모스 부호를 출력하는 코드를 작성하시오 

[결과]
모스 부호로 표시할 단어(알파벳 대문자) : ABC
A : .-
B : -....
C : -.-.
'''
code = {'A':'.-', 'B':'-....', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}


sign = input("모스 부호로 표시할 단어(알파벳 대문자) : ")
for i in range(len(sign)) :
    print(sign[i],":",code[sign[i]])













'''
5. 학생들의 시험 성적가 다음과 같은 경우 성적의 합계와 평균을 출력하는 코드를 작성하시오
[결과]
총합: 355 ,평균: 71.0
'''
import re
#sub사용하기 위해서 re module을 import
data= 'hong:90,lee:80,kim:75,park:50,song:60'
type(data) #str
numbers = re.findall(r'\d+', data)
print(numbers)
numbers=list(map(int,numbers))
ssum=0
for i in numbers :
    ssum += i
    mean=ssum/len(numbers)
print("총합:%d ,평균:%.1f" % (ssum,mean))










