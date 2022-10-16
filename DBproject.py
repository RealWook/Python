#고객 관리 프로그램


import sqlite3 #sqlite를 사용하기 위해 모듈을 불러온다.

con = sqlite3.connect("customer.db") #connect 메소드는 DB파일과 연결하여 데이터베이스를 연다.
cursor = con.cursor() #DB파일과 연결한 후 연결 객체의 cursor 메소드로 커서 객체를 구한다.
#커서는 sql문을 실행하고 결과를 읽는 객체이다.

cursor.execute("DROP TABLE IF EXISTS tblCustomer") #tblCustomer라는 테이블이 존재하면 삭제한다.
cursor.execute("""CREATE TABLE tblCustomer (NAME CHAR(15) PRIMARY KEY, BIRTH CHAR(20), PHONE CHAR(15), ADDR TEXT, THINGS TEXT)""")
#execute메소드로 tblCustomer 테이블을 생성한다, 테이블의 속성도 지정한다.
con.commit() #테이블 생성 후 커밋



def menu():

    """메뉴함수"""

    while True:
        print("===============================메뉴===================================")
        menu = int(input("메뉴 : 0.조회 , 1.고객정보 입력 , 2.고객정보 수정 , 3.고객정보 삭제 , 4.종료 >> " ))
        print()

        if (menu == 0):
            view() #0번 입력하면 조회함수로 이동

        elif (menu == 1):
            input_() #1번 입력하면 입력함수로 이동

        elif (menu == 2):
            update() #2번 입력하면 수정함수로 이동

        elif (menu == 3):
            delete() #3번메뉴는 삭제함수로 이동

        elif (menu == 4):
            cursor.close() #객체를 닫아주고
            con.close() #종료전 파일 닫아준다.
            print("종료되었습니다.")
            break
        else:
            print("메뉴를 다시 입력해주세요")
            print()




def view():

    """고객 정보 조회함수 (조회 메뉴 1,2 로 나뉘어 진다)"""

    print("조회 메뉴 >>> 1.고객 전체정보 조회 , 2.특정고객 조회")

    choice = int(input("조회 메뉴를 선택해주세요 : "))
    print()

    if (choice == 1): #고객의 전체정보 조회메뉴
        cursor.execute("SELECT * FROM tblCustomer") #execute메소드 사용하여 sql명령문 실행한다.
        table = cursor.fetchall() #table 변수에 cursor객체에서 실행한 fetchall()메소드의 리턴값을 담는다.
        # fetchall() 메소드는 모든 레코드(행)을 한꺼번에 읽어 리스트로 리턴하며, 읽을 것이 없으면 빈 리스트를 되돌려준다.

        if (table == []):
            #만약 table이 비어있다면
            print("조회 할 고객 정보가 없습니다.")
            print()
        else:  #만약 table이 비어있지 않다면
            for record in table:
                print("이름 : %s, 생년월일 : %s, 전화번호 : %s, 주소 : %s , 주문정보 : %s" %record)


    elif (choice == 2): #특정고객 조회 메뉴

        cus_name = input("조회하실 고객의 이름을 입력해주세요 : ") #조회 할 고객의 이름정보
        cus_birth = input("조회하실 고객의 생년월일을 입력하세요 (6자리 ex 980414) : ")  #조회 할 고객의 생년월일 정보
        print()

        cursor.execute("SELECT * FROM tblCustomer WHERE NAME = '%s' AND BIRTH = '%s' " %(cus_name,cus_birth))  #execute메소드 사용하여 sql명령문 실행한다.
        record = cursor.fetchone()  #fetchone() 메소드는 레코드 하나를 읽으며 반복적으로 호출하면, 다음레코드 계속 읽는다
        #더 읽을 레코드가 없으면 None값을 리턴한다.

        if (record == None): #record 안에 고객의 정보가 없을 시
            print("조회할 고객 정보가 없습니다.")
            print()

        else:  #record 안에 고객의 정보가 None이 아니면
            print("%s 고객님의 정보입니다." %cus_name)
            print("이름 : %s, 생년월일 : %s, 전화번호 : %s, 주소 : %s , 주문정보 : %s" %record)
            print()




def input_():
    """고객 정보 입력함수"""

    custlist2 = [] #빈리스트 생성

    name = input("고객의 이름을 입력하세요 : ")
    birth = input("고객의 생년월일을 입력하세요 (6자리 ex 980414) : ")
    phone = input("고객의 전화번호를 입력하세요(ex 010-1111-1111) : ")
    addr = input("고객의 주소를 입력하세요 : ")
    things = input("고객의 주문정보를 입력하세요 : ")
    print()
    print("고객 입력이 완료되었습니다 !")
    print()

    custlist = (name,birth,phone,addr,things) #빈리스트 안에 입력받은 정보들을 담는다.
    custlist2.append(custlist) #리스트들을 하나씩 추가한다.

    cursor.executemany("INSERT INTO tblCustomer(NAME,BIRTH,PHONE,ADDR,THINGS) VALUES(?,?,?,?,?)",custlist2)
    #리스트를 db에 입력할 땐 excutemany 메소드를 사용해야한다.

    con.commit() #insert후 commit 해준다.




def update():
    """고객정보 수정 함수"""

    up_name = input("수정하실 고객의 이름을 입력하세요 : ")
    up_birth = input("수정하실 고객의 생년월일을 입력하세요(6자리 ex 980414) : ")
    print()
    cursor.execute("SELECT * FROM tblCustomer WHERE NAME = '%s' and BIRTH = '%s' " %(up_name,up_birth)) #execute메소드를 통해 sql명령문 실행한다.
    #where절에서 조건을 주어 조건에 맞게 선택을 한다.
    record = cursor.fetchone() #fetchone() 메소드는 레코드 하나를 읽으며 반복적으로 호출하면, 다음레코드 계속 읽는다
    # 더 읽을 레코드가 없으면 None값을 리턴한다.

    if (record == None): #record안에 고객정보가 없을 시
        print("수정하실 고객의 정보가 없습니다")
        print()

    else:
        print()
        print("현재 %s 고객님의 정보입니다." %up_name) #고객정보를 먼저 한번 출력해준다
        print("이름 : %s, 생년월일 : %s, 전화번호 : %s, 주소 : %s , 주문정보 : %s" %record)
        print()

        up_addr = input("수정하실 주소를 입력하세요 : ") #수정 할 주소를 받는다.
        up_order = input("수정하실 주문정보를 입력하세요 : ") #수정 할 주문정보를 받는다.
        cursor.execute("UPDATE tblCustomer SET ADDR = '%s' , THINGS = '%s' WHERE NAME = '%s' AND BIRTH = '%s'" %(up_addr,up_order,up_name,up_birth))
        # execute메소드를 통해 sql명령문 실행한다.
        con.commit()
        print()
        print("수정이 완료되었습니다 !")
        print()


def delete():
    """고객정보 삭제 함수"""

    de_name = input("삭제하실 고객의 이름을 입력하세요 : ")
    de_birth = input("삭제하실 고객의 생년월일을 입력하세요 : ")

    cursor.execute("SELECT * FROM tblCustomer WHERE NAME = '%s' and BIRTH = '%s' " %(de_name,de_birth)) #execute메소드를 통해 sql명령문 실행한다.
    record = cursor.fetchone() #fetchone() 메소드는 레코드 하나를 읽으며 반복적으로 호출하면, 다음레코드 계속 읽는다
    print()

    if(record == None):   #record안에 고객정보가 없을 시
        print("삭제하실 고객의 정보가 없습니다.")
        print()

    else:
        print("현재 %s 고객님의 정보입니다." %de_name) #고객정보를 먼저 한번 출력해준다.
        print("이름 : %s, 생년월일 : %s, 전화번호 : %s, 주소 : %s , 주문정보 : %s" %record)
        print()

        key = int(input("정말 삭제하시려면 1을 입력해주세요 : "))  #삭제는 신중하게 해야 하므로, 한번 더 물어본다.

        if(key == 1): #삭제를 선택하면
            cursor.execute("DELETE FROM tblCustomer WHERE NAME = '%s' and BIRTH = '%s'" %(de_name,de_birth)) #execute메소드를 통해 sql명령문 실행한다.
            con.commit()
            print()
            print("삭제가 완료되었습니다 !")
            print()
        else:
            print("잘못 입력하셨습니다.")
            print()


menu()
