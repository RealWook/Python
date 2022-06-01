article = {} #빈 딕셔너리 생성
def menu():
    """이 함수는 데이터 입력 및 출력을 선택하는 메뉴를 나타내는 함수입니다."""

    while True:
        print("=================입력 처리 메뉴===================")
        print("=============(메뉴 순서대로 실행하세요)=============")
        menu = int(input("메뉴 : 0.종료 , 1.데이터 입력 , 2.데이터 출력 ==> "))
        print()

        if (menu == 0):
            print("종료되었습니다.")
            break

        elif (menu == 1):
            input_() #1번 입력하면 입력함수로 이동

        elif (menu == 2):
            view(article) #2번 입력하면 출력함수로 이동


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
    dic = {"물품번호 : " + article_number : {'품목명' : article_name, '물품단가' : article_price, '보유수량' : article_quantity}}
    article.update(dic) #글로벌로 선언한 딕셔너리 업데이트, 중복된 키는 병합되는 키의 값 적용

    return article #리턴값은 업데이트한 아티클 딕셔너리



def view(article):
    """이 함수는 입력받은 데이터를 통해, 출력을 나타내는 함수입니다."""

    print("******************** 물품 등록 정보 ***********************")
    for key,value in article.items(): #itmes 메서드는 키와 값을 쌍으로 묶은 투플객체를 리턴한다, 반복문을 사용하여 아티클 딕셔너리의 key인 물품번호,value값인 품목명,물품단가,보유수량 딕셔너리를 반복하여 출력한다.
        print(key)
        print(value)
        print()
menu()



