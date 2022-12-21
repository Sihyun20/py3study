#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:12:46 2022

@author: ryong
"""

'''
1. mod2.py 파일을 읽어서 mod2.bak 파일로 복사하기.
'''
import mod2
infp = open("mod2.py","r")  #원본파일. 읽기위한 파일
outfp = open("mod2.bak","w") #복사본파일. 쓰기위한 파일
while True :
    indata = infp.read() #설정된 버퍼의 크기만큼 읽기
    if not indata :  #파일의 끝. EOF(End of File)
        break
    outfp.write(indata) #복사본파일에 데이터 쓰기
infp.close()
outfp.close() 









'''
2. 현재폴더에 temp폴더를 생성하고, 생성된 폴더에 indata.txt 파일에
   키보드에서 입력된 정보 저장하는 프로그램 구현하기
'''

import os
path = os.getcwd();
path
os.mkdir("temp")
outfp = open("temp/indata.txt","w")
while True :
    outstr = input("내용입력=>")
    if outstr == '' :
        break
    outfp.writelines(outstr+"\n")
outfp.close() 

#업로드 후 필요없는부분이 있어서 수정함.






'''
3.원본 파일의 이름을 입력받고, 입력받은 복사본 파일이름으로 복사하는 
  프로그램 작성하기
  원본파일이 없는 경우 원본 파일이 존재하지 않습니다. 출력하기

[결과]
원본파일의 이름을 입력하세요 : aaa
원본파일이 존재하지 않습니다.

원본파일의 이름을 입력하세요 : data.txt
복사본파일의 이름을 입력하세요 : databak.txt
복사완료
'''
import os
from os import path
import shutil

origin = r'/Users/ryong/python/data.txt'
copy = r'/Users/ryong/python/databak.txt'

inFp = None
fName = input("원본파일의 이름을 입력하세요: ")
if os.path.exists(fName):
    inFp = open(fName, "r")
    shutil.copy(origin,copy)
    cFile = input("복사본파일의 이름을 입력하세요 : ")
    outFp = open(cFile, "r")
    print("복사완료")
    inFp.close()
    outFp.close()
else:
    print("원본파일이 존재하지 않습니다.")
    
###copy는 되는데 복사본의 이름을 입력받아 그 이름으로 복사가 되는게 아니고
###위에서 copy경로에 이름을 써줬기 때문에 그 이름과 동일하게 복사본파일 이름을 입력하면 
###파일이 그 경로에 존재해서 그다음 프린트인 복사완료가 나옴..

import os
name = input("원본파일의 이름을 입력하세요 : ")
if os.path.exists(name):
     du_name = input("복사본 파일의 이름을 입력하세요 : ")
     ori = open(name, "r", encoding = "UTF-8")
     dup = open(du_name, "w", encoding = "UTF-8")
     while True:
         indata = ori.read()
         if not indata:
             break
         dup.write(indata)
     ori.close()
     dup.close()
     print("복사 완료")
else : 
     print("원본파일이 존재하지 않습니다.")
###시현이 답이 생각에 흐름과 동일하게 가서 적당하고 딱 좋음!
###해결못했던 복사가 먼저되는 것을 이 코드로는 간단하게 해결 좋아~    








'''
 4. 다음 number 데이터를 이용하여 큰글씨를 출력하는 프로그램 작성하기 
   [결과]
   숫자를 입력하세요 =>12345
     *  ***  ***  * *  ***  
     *    *    *  * *  *    
     *  ***  ***  ***  ***  
     *  *      *    *    *  
     *  ***  ***    *  ***  
'''
number= [["*** ",
          "* * ",
          "* * ",
          "* * ",
          "*** "],
	     ["  * ",
          "  * ",
          "  * ",
          "  * ",
          "  * "],
		 ["*** ","  * ","*** ","*   ","*** "],
		 ["*** ","  * ","*** ","  * ","*** "],
		 ["* * ","* * ","*** ","  * ","  * "],
		 ["*** ","*   ","*** ","  * ","*** "],
		 ["*** ","*   ","*** ","* * ","*** "],
		 ["*** ","  * ","  * ","  * ","  * "],
		 ["*** ","* * ","*** ","* * ","*** "],
		 ["*** ","* * ","*** ","  * ","  * "]
		]

inNum = input("숫자를 입력하세요 =>")
num = [i for i in inNum]
num = list(map(int,num))

for i in range(5):
    for j in range(len(num)):
        print(number[num[j]][i], end="")
    print()



###뭔가 반복해서 입력값에 맞춰 출력되야되는데 
###어떻게 식을 세워야될지 모르겠음....넘어렵
###=>
###표를 만들어서 넣어보거나 노트에 적어봐서 어떻게 나와야되는지 눈으로
###확연히 보이도록 해서 풀어보자(사부의 팁)
###input받을때 int로 받으면 인덱스로 뽑아와서 하는게 안됨 그부분 유의









'''
 5. sqlite의 mydb의 테이블의 내용 조회하기
 sql 구문을 입력하고 다음과 같은 결과가 출력되도록 프로그램을 작성하시오
[결과]
sql 입력하세요=========
select * from member

조회 레코드수: 6 ,조회 컬럼수: 3

('hongkd', '홍길동', 'hongkd@aaa.bbb')
('kimsg', '김삿갓', 'kimsg@aaa.bbb')
('test1', '테스트1', 'test1@aaa.bbb')
('test2', '테스트2', 'test2@aaa.bbb')
('test3', '테스트3', 'test3@aaa.bbb')
('test4', '테스트4', 'test4@aaa.bbb')
sql 입력하세요=========
insert into member (id,name,email) values ('a','a','a')
sql 입력하세요=========
select * from member

조회 레코드수: 7 ,조회 컬럼수: 3

('hongkd', '홍길동', 'hongkd@aaa.bbb')
('kimsg', '김삿갓', 'kimsg@aaa.bbb')
('test1', '테스트1', 'test1@aaa.bbb')
('test2', '테스트2', 'test2@aaa.bbb')
('test3', '테스트3', 'test3@aaa.bbb')
('test4', '테스트4', 'test4@aaa.bbb')
('a', 'a', 'a')
sql 입력하세요=========
'''
import sqlite3      
conn = sqlite3.connect("mydb")
cur = conn.cursor()
inSql =input("sql 입력하세요=========")
print(inSql)
a=cur.execute("select count(*) from member")
while True :
    d1 = input("sql 입력하세요========== ") 
    if d1 == '' :
       break 
    d2 = input("sql 입력하세요========== )
    d3 = input("sql 입력하세요========== )
b= "insert into member (id,name,email) values ('"+d1+"','"+d2+"','"+d3+"')"
print("조회 레코드수: ",a ,"조회 컬럼수: ", )
cur.execute(inSql)
while True :
    row = cur.fetchone() 
    if row == None :
        break
    print()
    print(row)
cur.close()
conn.close()

###sql과 파이썬을 어떻게 혼합해서 써야 출력이 되는지...
### sql구문 실행하는 명령문을 변수에 넣을 수 있는건지..
###할수있는데까지해봄.. 근데 이거저거 조합하다보니 엉망인것같음..

import sqlite3
conn = sqlite3.connect("mydb") 
cur = conn.cursor()
while True :
    sql = input("sql 입력하세요=========\n")
    if sql=="" :
        break
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) > 0 : #select 구문인 경우
       print()
       print("조회 레코드수:",len(rows),",조회 컬럼수:",len(rows[0]))    
       print()
       for row in rows :
           print(row)
cur.close()
conn.close();

###위는 예시답인데,
###생각보다 답을 보니 간단했는데 len, for, if를 잘 사용해야겠다.
###내가 푼 방식?을 어떻게 정리해야 오류없이 문제의 답으로 향할 수 있는지
###고민이 더 필요하다.













