# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 12:47:37 2022

@author: gong6
"""
#1
class Rect:
    w = 0
    h = 0
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def __repr__(self):
        return "(%d,%d), 넓이:%d,둘레:%d" % \
       (self.w,self.h,self.area(),self.length())
    
    def __gt__(self, other):
        return self.area() > other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __eq__(self, other):
        return self.area() == other.area()
    
    def area(self):
        area = self.w*self.h
        return area
    def length(self):
        length = 2*(self.w+self.h)
        return length
        
   

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


#2
class Calculator:
    value = 0
    def add(self, value):
        self.value += value

class UpgradeCalculator(Calculator) :
    def minus(self, value):
        self.value -= value
    

cal = UpgradeCalculator() 
cal.add(10)
cal.minus(7)

print(cal.value)



#3
class Calculator:
    value = 0
    def add(self,value):
        self.value += value

class MaxLimitCalculator(Calculator):
    def add(self, value):
        self.value += value
        if self.value >= 100:
            self.value = 100


cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)


#4
code = {'A':'.-', 'B':'-....', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..'}

word = input("모스부호로 표시할 단어(알파벳 대문자로 입력) : ")
alpha = [_ for _ in word]
for i in range(len(alpha)):
    print(alpha[i], ":", code[alpha[i]])


#5

data= 'hong:90,lee:80,kim:75,park:50,song:60'
key = []
val = []
sum = 0
data_list = data.split(",")
for data in data_list :
    dt = data.split(":")
    key.append(dt[0])
    val.append(dt[1])
    sum += int(dt[1])

print("총합 :",sum,"평균 :", sum/len(key))





