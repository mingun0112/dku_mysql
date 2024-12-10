import pymysql
import pandas as pd
import os


def get_db_connection():
    return pymysql.connect(host='127.0.0.1', user='root', password='1234', db='classdb', charset='utf8mb4')


def customer_information():
    conn = get_db_connection()
    cur = conn.cursor()
    

    cur.execute("SELECT COUNT(*) FROM members")
    member_count = cur.fetchone()[0]
    print(f"\n[고객 수] 총 {member_count}명")


    cur.execute("SELECT username, email FROM members")
    customers = cur.fetchall()

    df = pd.DataFrame(customers, columns=["Username", "Email"])


    print("\n[고객 정보]")
    print(df)
    
    conn.close()

def customer_registration():
    print("\n[고객 등록] - 새로운 고객을 등록합니다.")
    try:
        username = input("고객 이름: ")
        email = input("고객 이메일: ")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO members (username, email) VALUES (%s, %s)", (username, email))
    except ValueError:
        print("잘못된 입력입니다.")
    conn.commit()
    print("고객이 성공적으로 등록되었습니다.")
    conn.close()


def customer_deletion():
    print("\n[고객 삭제] - 고객을 삭제합니다.")
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT username FROM members")
    customers = cur.fetchall()
    
    if not customers:
        print("삭제할 고객이 없습니다.")
        conn.close()
        return

    print("\n고객 목록:")
    for idx, customer in enumerate(customers, 1):
        print(f"{idx}. {customer[0]}")
    print(f"0. 뒤로가기")


    try:
        choice = int(input("\n삭제할 고객 번호를 선택하세요: "))
        if choice == 0: 
            print("뒤로 가기")
            os.system('clear')
            # conn.close()
            return
        if choice < 1 or choice > len(customers):
            print("유효하지 않은 번호입니다.")
            # conn.close()
            return
        username_to_delete = customers[choice - 1][0]


        cur.execute("DELETE FROM members WHERE username = %s", (username_to_delete,))
        conn.commit()
        os.system('clear')
        print(f"고객 '{username_to_delete}' 삭제 완료")
    except ValueError:
        print("잘못된 입력입니다.")
    finally:
        conn.close()

def customer_management():
    while True:
        print("")
        print("")
        print("")
        print("\n[고객 관리]")
        print("")
        print("1. 고객 정보")
        print("2. 고객 등록")
        print("3. 고객 삭제")
        print("4. 돌아가기")
        print("")

        choice = input("Select (1/2/3/4): ")
        os.system('clear')

        if choice == "1":
            customer_information()
        elif choice == "2":
            customer_registration()
        elif choice == "3":
            customer_deletion()
        elif choice == "4":
            break 
        else:
            print("오류, 재선택")
            
