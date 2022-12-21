# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:44:38 2022

@author: Galaxy Book Ion
"""


'''
1. mod2.py 파일을 읽어서 mod2.bak 파일로 복사하기.
'''
infp = open("mod2.py","r",encoding="UTF-8")
outfp = open("mod2.bak","w", encoding="UTF-8")
#rb는 바이너리 - 이미지, 동영상 등 . 걍 파일은 r
while True :
    indata = infp.read() #설정된 버퍼의 크기만큼 읽기
    if not indata :  #EOF(End of File)
        break
    outfp.write(indata) 
infp.close()
outfp.close() 

'''
2. 현재폴더에 temp폴더를 생성하고, 생성된 폴더에 indata.txt 파일에
   키보드에서 입력된 정보 저장하는 프로그램 구현하기
'''
import os
os.mkdir("temp")
out = open("indata.txt","w", encoding="UTF-8")
while True:
    outstr = input("내용 입력 : ")
    if outstr == '':
        break
    out.writelines(outstr+"\n")
out.close()



# 입력 내용 확인해보기
inp = open("indata.txt", "r", encoding = "UTF-8")
while True:
    instr = inp.readline()
    if instr == None or instr == "":
        break
    print(instr, end="\n")
inp.close()

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
		 ["*** ",
          "  * ",
          "*** ",
          "*   ",
          "*** "],
		 ["*** ","  * ","*** ","  * ","*** "],
		 ["* * ","* * ","*** ","  * ","  * "],
		 ["*** ","*   ","*** ","  * ","*** "],
		 ["*** ","*   ","*** ","* * ","*** "],
		 ["*** ","  * ","  * ","  * ","  * "],
		 ["*** ","* * ","*** ","* * ","*** "],
		 ["*** ","* * ","*** ","  * ","  * "]
		]

n = input("숫자를 입력하세요 : ")
num = [i for i in n]
num = list(map(int, num))

for i in range(5):
    for j in range(len(num)):
        print(number[num[j]][i], end="")
    print()


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
while True:
    sqlq = input("sql 입력하세요========== \n")
    if sqlq == "":
        break
    cur.execute(sqlq)
    conn.commit()
    if "select" in sqlq:
#        print("조회 레코드 수 :",", 조회 컬럼수 :") 이거 몰랑ㅇ.. 꼭 답 처럼 fetchall() 써서 푸는 방법 밖에 없을까?

        while True :
            row = cur.fetchone()
            if row == None :
                break
            print(row)
        
conn.close()




