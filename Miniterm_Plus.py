article = {} #빈 딕셔너리 생성
def menu():
    """이 함수는 데이터 입력 및 출력을 선택하는 메뉴를 나타내는 함수입니다."""

    while True:
        print("=================입력 처리 메뉴===================")
        print("=============(메뉴 순서대로 실행하세요)=============")
        menu = int(input("메뉴 : 0.종료 , 1.데이터 입력 , 2.데이터 출력 , 3.데이터 조회 , 4.데이터 수정, 5.데이터 삭제 ==> "))
        print()

        if (menu == 0):
            print("종료되었습니다.")
            break

        elif (menu == 1):
            input_() #1번 입력하면 입력함수로 이동

        elif (menu == 2):
            view(article) #2번 입력하면 출력함수로 이동

        elif (menu == 3):
            inquiry(article) #3번메뉴는 조회메뉴, 조회함수로 이동

        elif (menu == 4):
            modify(article) #4번메뉴는 수정메뉴, 수정함수로 이동

        elif (menu == 5):
            delete_(article) #5번메뉴는 삭제메뉴, 삭제함수로 이동


def input_():
    """이 함수는 물품의 데이터를 입력받는 함수입니다."""

    article_number = input("물품 번호를 입력하세요(4자리) : ")
    article_name = input("품목명을 입력하세요 : ")
    article_price = input("물품단가를 입력하세요 : ")
    article_quantity = input("보유수량을 입력하세요 : ")
    print()
    print("입력이 완료되었습니다!")
    print()

    #!!!!중요!!!!  딕셔너리 저장, 이중 딕셔너리
    dic = { article_number : {'품목명' : article_name, '물품단가' : article_price, '보유수량' : article_quantity}}
    article.update(dic) #글로벌로 선언한 딕셔너리 업데이트

    return article #리턴값은 업데이트한 아티클 딕셔너리



def view(article):
    """이 함수는 입력받은 데이터를 통해, 출력을 나타내는 함수입니다."""

    print("********************* 물품 등록 정보 ***********************")
    for key,unit in article.items(): #itmes 메서드는 키와 값을 쌍으로 묶은 투플객체를 리턴한다, 반복문을 사용하여 아티클 딕셔너리의 key인 물품번호,value값인 품목명,물품단가,보유수량 딕셔너리를 반복하여 출력한다.
        print(key)
        print(unit)
        print()



def inquiry(article):
    """이 함수는 데이터를 조회하는 함수입니다."""
    article_number2 = input("조회하실 물품 번호를 입력하세요(4자리) : ")
    if article_number2 in article: #입력받은 조회 할 물품번호가 아티클 딕셔너리에 키로 있을경우
            print(article_number2)
            print(article[article_number2]) #사전[키] 형식 = 키의 값 구해준다.
            print("조회가 완료되었습니다!")
    else:
        print("조회 할 물품이 없습니다.")



def modify(article):
    """이 함수는 데이터를 수정하는 함수입니다."""
    article_number2 = input("수정하실 물품 번호를 입력하세요(4자리) : ")
    if (article_number2 not in article): #수정 할 품목이 없는 경우 안내
        print("수정 할 품목이 없습니다.")

    for key, unit in article.items(): #key, unit으로 제어변수 2개 선언한다음, items()메소드를 통해, 아티클 딕셔너리의 키와 값을 반복한다.
        if (key == article_number2):
            article_name = input("수정하실 품목명을 입력하세요 : ")
            article_price = input("수정하실 물품단가를 입력하세요 : ")
            article_quantity = input("수정하실 보유수량을 입력하세요 : ")

            article2 = {article_number2 : {'품목명' : article_name, '물품단가' : article_price, '보유수량' : article_quantity}} #반복문 안 if문 들여쓰기 주의
            article.update(article2) #수정한 아티클2 딕셔너리를 원래 있던 아티클 딕셔너리에 업데이트한다.

            print()
            print("수정이 완료되었습니다!")

            return article



def delete_(article):
    """이 함수는 데이터를 삭제하는 함수입니다."""
    article_number2 = input("삭제하실 물품 번호를 입력하세요(4자리) : ")

    if (article_number2 not in article): #삭제 할 품목이 없는 경우 안내
        print("삭제 할 품목이 없습니다.")

    for key,unit in article.items():
        if (key == article_number2): #삭제할 물품번호가, 아티클딕셔너리의 키 값인, 물품번호에 있을 때
            ans = input("정말 삭제하시겠습니까? 맞으면 Y, 아니면 N이라고 입력해주세요 : ") #삭제는 신중해야 하므로, 한번 더 물어보는 메세지 작성
            if (ans == 'Y'):
                del article[key] #del 딕셔너리[key] 명령을 통해 삭제하고싶은 물품번호(key)의 value를 같이 삭제한다.
                break
            elif (ans == 'N'):
                print("삭제를 취소하셨습니다.")
            else:
                print("다시 입력해주세요")
    print("삭제가 완료되었습니다!")
    print()

menu()