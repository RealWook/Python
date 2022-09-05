custlist2 = []

def menu(): #디스플레이 용도, 전달되는 파라미터 없다
    """ 이 함수는 메뉴의 구성을 나타내는 함수 입니다."""

    print("================================메뉴================================") #메뉴를 나타냄
    menu = int(input("0.종료, 1.정보입력, 2.정보출력, 3.정보조회, 4.정보수정, 5.정보삭제 >>> "))
    return menu #함수를 호출하는 쪽에 결과로 전달



def main():
    """이 함수는 메뉴값을 전달받아, 메뉴를 실행하는 메인함수입니다."""

    while True:
        select = menu() #메뉴함수 리턴값을 변수에 대입.

        if (select == 0):
            print("종료되었습니다.")
            break

        elif (select == 1):
            input_() #정보입력 함수로 이동

        elif (select == 2):
            view() #정보출력 함수로 이동

        elif (select == 3):
            inquiry() #정보조회 함수로 이동

        elif (select == 4):
            modify() #정보수정 함수로 이동

        elif (select == 5):
            delete_() #정보삭제 함수로 이동

        else:
            print("잘못 입력하셨습니다.")



def input_():
    """이 함수는 고객 정보를 입력받는 함수입니다."""

    customer_ID = input("고객 아이디를 입력해주세요 : ")
    customer_pw = input("고객 비밀번호를 입력해주세요 : ")
    customer_name = input("고객 이름을 입력해주세요 : ")
    customer_gender = gender() #gender함수에서 return값을 받는다.
    customer_birth = input("고객의 생년월일을 입력해주세요 : ")
    customer_phone = input("고객의 전화번호를 입력해주세요 : ")
    customer_address = input("고객의 주소를 입력해주세요 : ")
    print()
    print("입력이 완료되었습니다!")

    custlist = [customer_ID,customer_pw,customer_name,customer_gender,customer_birth,customer_phone,customer_address]
    custlist2.append(custlist) #custlist2의 빈 리스트에 custlist를 append 시킨다.
    return custlist2




def gender():
    """이 함수는 성별을 나타내주는 함수입니다."""

    gender = ('남성', '여성')  # 성별을 튜플로 구성
    gen = input("성별을 입력해주세요 : ")
    if (gen == '1'):
        gen = gender[0]
    elif (gen == '2'):
        gen = gender[1]

    return gen




def view():
    """이 함수는 고객의 전체정보를 출력하는 함수입니다."""

    print("======================================고객 등록 정보======================================")

    print("고객수는  %d명 입니다." % len(custlist2))
    for a in range(len(custlist2)): #입력함수에서 append 된 custlist2의 길이만큼 반복한다.
        print(custlist2[a][0] + "번째 고객")
        print(custlist2[a])




def inquiry():
    """이 함수는 고객의 정보를 조회하는 함수입니다."""

    custid = input("조회하실 고객의 ID를 입력하세요 : ")

    for i in range(len(custlist2)): #입력함수에서 append 된 custlist2의 길이만큼 반복한다.
        if (custid == custlist2[i][0]):
            print("ID:{}, PW:{}, 이름:{}, 성별:{}, 생년월일:{}, 전화번호:{}, 주소:{}" .format(custlist2[i][0],custlist2[i][1],custlist2[i][2],custlist2[i][3],custlist2[i][4],custlist2[i][5],custlist2[i][6]))
            return #반복문을 돌면서 custid 가 custlist2[i][0]번째 값과 같을 시 그 값만 return해줌

    print("고객 ID가 없습니다.")




def modify():
    """이 함수는 고객 정보를 수정하는 함수입니다."""

    custid = input("수정하실 고객의 ID를 입력하세요 : ")
    for key in range(len(custlist2)): #입력함수에서 append 된 custlist2의 길이만큼 반복한다.
        if(custid == custlist2[key][0]):
            custlist2[key][1] = input("수정하실 암호를 입력해주세요 : ")
            custlist2[key][2] = input("수정하실 이름을 입력해주세요 : ")
            custlist2[key][5] = input("수정하실 전화번호를 입력해주세요 : ")
            custlist2[key][6] = input("수정하실 주소를 입력해주세요 : ")
            print()
            print("수정이 완료되었습니다!")
            return

    print("수정 할 아이디가 없습니다.")





def delete_():
    """이 함수는 고객 정보를 삭제하는 함수입니다."""

    custid = input("삭제하실 고객의 ID를 입력하세요 : ")

    for i in range (len(custlist2)): #입력함수에서 append 된 custlist2의 길이만큼 반복한다.

        if (custid == custlist2[i][0]):
            ans = input("정말 삭제하시겠습니까? 맞으면 Y, 아니면 N을 입력해주세요.")
            if (ans == 'Y'):
                custlist2.remove(custlist2[i])
                print("삭제가 완료되었습니다!")
                break
            elif (ans == 'N'):
                print("삭제를 취소하셨습니다.")
                return

        elif (custid != custlist2[i][0]):
            print("삭제 할 고객정보가 없습니다.")
            return
    else:
        print("삭제 할 고객 정보가 없습니다.")



main()
