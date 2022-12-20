# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:28:51 2022

@author: 예은
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
# 가로,세로를 입력하여 둘레와 넓이를 출력하는건 성공했지만
# 어느 면적이 더 넓은지 비교하는 코딩은 실패하였다.

class rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def __repr__(self) :  #객체 print시 호출되는 함수
        return "(%d,%d), 넓이:%d,둘레:%d" % \
       (self.width,self.height,self.area(),self.length())
    def __gt__(self,other) :
        return self.area() > other.area()
    def __lt__(self,other) :
        return self.area() < other.area()
    def __eq__(self,other) :
        return self.area() == other.area()
    def area(self) :    
        return self.width * self.height
    def length(self) :  
        return (self.width + self.height) * 2
    
if __name__ == "__main__" :
     rect1 = rectangle(10,20) 
     rect2 = rectangle(10,10)
     print("rect1=",rect1)
     print("rect2=",rect2)
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
# 솔직하게 말하자면 문제이해하는 시간도 오래걸리고
# 문제 푸는법도 헷갈려서 강사님 코드 가져와서 이해하는중

class Calculator:
      value=0
      def add(self, val):
          self.value += val

class UpgradeCalculator(Calculator) :
      def minus(self, val):
          self.value -= val
 

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)



'''
3. 2번에서 구현한 Calculator 클래스를 이용하여 
   MaxLimitCalculator 클래스 구현하기
MaxLimitCalculator 클래스에서 value 값은 절대 100 이상의 값을 가질수 없다.
'''
# 솔직하게 말하자면 문제이해하는 시간도 오래걸리고
# 문제 푸는법도 헷갈려서 강사님 코드 가져와서 이해하는중

class MaxLimitCalculator(Calculator) :
      def add(self, val):   
          self.value += val
          if self.value > 100 :
              self.value = 100
    
cal = MaxLimitCalculator()
cal.add(50) 
print(cal.value) 
cal.add(60)
print(cal.value)  



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

data = input("모스 부호로 표시할 단어(알파벳 대문자) : ")
for i in range(len(data)) :
    print(data[i],":",code[data[i]]) 



'''
5. 학생들의 시험 성적가 다음과 같은 경우 성적의 합계와 평균을 출력하는 코드를 작성하시오
[결과]
총합: 355 ,평균: 71.0
'''
import re
data = 'hong:90,lee:80,kim:75,park:50,song:60'

pattern = re.compile("\\d+")
tlist = re.findall(pattern,data)
print(type(tlist))
tlist = list(map(int,tlist))
print(tlist)
print("총합:",sum(tlist),
      ",평균:",sum(tlist)/len(tlist))
    
    
    
    
    
    
    
