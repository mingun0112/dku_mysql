import pymysql
import os
import pandas as pd

def get_db_connection():
    return pymysql.connect(host='127.0.0.1', user='root', password='1234', db='classdb', charset='utf8mb4')


def goods_information():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, name, price, manufacturer FROM goods")
    goods = cur.fetchall()


    df = pd.DataFrame(goods, columns=["ID", "Product Name", "Price", "Manufacturer"])

    print("\n[상품 정보]")
    print(df.to_string(index=False)) 
    
    conn.close()

def goods_deletion():
    conn = get_db_connection()
    cur = conn.cursor()


    product_name = input("삭제할 상품 이름을 입력하세요: ")

    cur.execute("SELECT id, name, price, manufacturer FROM goods WHERE name LIKE %s", ('%' + product_name + '%',))
    goods = cur.fetchall()

    if goods:
        print("\n[검색된 상품 정보]")
        for idx, (id, name, price, manufacturer) in enumerate(goods, start=1):
            print(f"{idx}. {name} - {price} - {manufacturer}")

        try:
            choice = int(input("\n삭제할 상품 번호를 선택하세요: "))
            if 1 <= choice <= len(goods):
                selected_product = goods[choice - 1]
                selected_product_id = selected_product[0]

                cur.execute("DELETE FROM goods WHERE id = %s", (selected_product_id,))
                conn.commit()

                os.system('clear')
                print(f"{selected_product[1]}(이)가 삭제되었습니다.")
            else:
                print("잘못된 선택입니다.")
        except ValueError:
            print("유효하지 않은 입력입니다.")
    else:
        print("해당 이름을 가진 상품이 없습니다.")

    conn.close()

def goods_registration():
    conn = get_db_connection()
    cur = conn.cursor()

    product_name = input("상품 이름을 입력하세요: ")
    product_price = input("상품 가격을 입력하세요: ")
    product_manufacturer = input("상품 제조사를 입력하세요: ")
    

    try:
        product_price = float(product_price)
    except ValueError:
        print("유효하지 않은 가격입니다. 숫자만 입력하세요.")
        conn.close()
        return


    try:
        cur.execute(
            "INSERT INTO goods (name, price, manufacturer) VALUES (%s, %s, %s)",
            (product_name, product_price, product_manufacturer)
        )
        conn.commit()
        os.system('clear')
        print(f"상품 '{product_name}'이 성공적으로 등록되었습니다.")
    except pymysql.MySQLError as e:
        print(f"상품 등록 중 오류가 발생했습니다: {e}")
    
    conn.close()

def goods_management():
    while True:
        print("\n[상품 관리]")
        print("")
        print("1. 상품 정보")
        print("2. 상품 등록")
        print("3. 상품 삭제")
        print("4. 돌아가기")
        print("")
        

    
        choice = input("Select (1/2/3/4): ")
        os.system('clear')

        if choice == "1":
            goods_information()
        elif choice == "2":
            goods_registration()
        elif choice == "3":
            goods_deletion()
        elif choice == "4":
            break  
        else:
            print("오류, 재선택")
