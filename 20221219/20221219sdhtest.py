# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:22:48 2022

@author: super
"""

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
    w=0
    h=0
    def __init__(self,w,h):
        self.w = w
        self.h = h
    def __repr__(self):
        return "(%d,%d), 넓이:%d,둘레:%d" % \
       (self.w,self.h,self.area(),self.length())
    def __lt__(self, o) :
        return self.area() > o.area()
    def __gt__(self, o):
        return self.area() < o.area()
    def __eq__(self, o):
        return self.area() == o.area()
    def area(self):
        return self.w*self.h
    def length(self):
        return (self.w+self.h)*2
 #결과가 왜 다르게 나오지?

if __name__ == "__main__" :
     rect1 = Rect(10,20)
     rect2 = Rect(10,10)
     print(rect1)
     print(rect2)
     if rect1 > rect2 :
         print(rect1.area(),"면적이 더 큰 사각형 입니다.")
     elif  rect1 < rect2 :  
         print(rect2.area(),"더 큰 사각형 입니다.")
     elif rect1 == rect2 :
         print(rect1.area(),"=",rect2.area(),"같은 크기의 사각형 입니다.")

'''
2. main 이 실행 되도록, Calculator 클래스를 상속받은 
   UpgradeCalculator  클래스 구현하기
   
   Calculator  클래스
     value 멤버변수
     add 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 더하기
   UpgradeCalculator 클래스
     minus 멤버함수 => 현재 value의 값에 매개변수로 받는 값을 빼기
'''   
class Calculator:
      value=0
      def add(self, val):
          self.value += val

class UpgradeCalculator(Calculator) :
      def minus(self, val):
          self.value -= val
 

cal = UpgradeCalculator()  #객체화 
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력
'''
3. 2번에서 구현한 Calculator 클래스를 이용하여 
   MaxLimitCalculator 클래스 구현하기
MaxLimitCalculator 클래스에서 value 값은 절대 100 이상의 값을 가질수 없다.
'''
class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value += val
        if self.value >100 :
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
print(cal.value) # 50 출력
cal.add(60) # 60 더하기
print(cal.value) # 100 출력
#ez


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

s = input('알파벳 입력:')
words = s.split(' ')
for i in words:
    chars = i.split()
    for j in chars:
        print(code[j], end= '')
    print('', end=' ')
    
print()

''' 실행 후 밑에 에러 발생 ㅠ
Traceback (most recent call last):

  File "C:\Users\super\AppData\Local\Temp/ipykernel_21488/2607200147.py", line 11, in <module>
    print(dic[j], end= '')

KeyError: 'avx'
'''

'''
5. 학생들의 시험 성적가 다음과 같은 경우 성적의 합계와 평균을 출력하는 코드를 작성하시오
[결과]
총합: 355 ,평균: 71.0
'''

data= 'hong:90,lee:80,kim:75,park:50,song:60'
average = sum(data.value()) / len(data)
print(average)

''' 난 잘 못 없고 노트북이 문제인듯
Traceback (most recent call last):

  File "C:\Users\super\AppData\Local\Temp/ipykernel_21488/516992938.py", line 2, in <module>
    average = sum(data.value()) / len(data)

AttributeError: 'str' object has no attribute 'value'
'''