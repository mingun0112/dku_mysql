import pymysql
import os
import pandas as pd

def get_db_connection():
    return pymysql.connect(host='127.0.0.1', user='root', password='1234', db='classdb', charset='utf8mb4')



def order_registration():

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, username FROM members")
        customers = cur.fetchall()

        print("\n고객 목록:")
        for idx, (customer_id, username) in enumerate(customers, 1):
            print(f"{idx}. {username}")

        choice = int(input("\n등록할 고객 번호를 선택하세요: "))
        if choice < 1 or choice > len(customers):
            print("유효하지 않은 번호입니다.")
            return
        customer_id = customers[choice - 1][0]


        cur.execute("SELECT id, name, price FROM goods")
        goods = cur.fetchall()

        print("\n상품 목록:")
        for idx, (good_id, name, price) in enumerate(goods, 1):
            print(f"{idx}. {name} (가격: {price}원)")

     
        product_choice = int(input("\n주문할 상품 번호를 선택하세요: "))
        if product_choice < 1 or product_choice > len(goods):
            print("유효하지 않은 번호입니다.")
            return
        product_id = goods[product_choice - 1][0]


        quantity = input("주문할 수량을 입력하세요: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("올바른 수량을 입력하세요.")
            return
        quantity = int(quantity)

        sql = "INSERT INTO cart (member_id, goods_id, quantity) VALUES (%s, %s, %s)"
        cur.execute(sql, (customer_id, product_id, quantity))
        conn.commit()

        print("주문이 성공적으로 등록되었습니다!")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        conn.close()


def view_orders():
 
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        sql = """
            SELECT 
                cart.id AS order_id,
                members.username AS customer_name,
                goods.name AS product_name,
                goods.price AS product_price,
                cart.quantity,
                (goods.price * cart.quantity) AS total_price
            FROM cart
            JOIN members ON cart.member_id = members.id
            JOIN goods ON cart.goods_id = goods.id
        """
        orders_df = pd.read_sql(sql, conn)

        if not orders_df.empty:
            print("\n주문 정보 (pandas):\n")
            print(orders_df.to_string(index=False)) 
        else:
            print("\n등록된 주문이 없습니다.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        conn.close()
def delete_order():

    try:
        conn = get_db_connection()
        cur = conn.cursor()

     
        sql = """
            SELECT 
                cart.id AS order_id,
                members.username AS customer_name,
                goods.name AS product_name,
                goods.price AS product_price,
                cart.quantity,
                (goods.price * cart.quantity) AS total_price
            FROM cart
            JOIN members ON cart.member_id = members.id
            JOIN goods ON cart.goods_id = goods.id
        """
        cur.execute(sql)
        orders = cur.fetchall()


        if not orders:
            print("\n등록된 주문이 없습니다.")
            return

        print("\n주문 목록:")
        for idx, (order_id, customer_name, product_name, product_price, quantity, total_price) in enumerate(orders, 1):
            print(f"{idx}. 고객: {customer_name}, 상품: {product_name}, 수량: {quantity}, 총 금액: {total_price}원")

        choice = int(input("\n삭제할 주문 번호를 선택하세요: "))
        if choice < 1 or choice > len(orders):
            print("유효하지 않은 번호입니다.")
            return
        
        order_id_to_delete = orders[choice - 1][0]

        delete_sql = "DELETE FROM cart WHERE id = %s"
        cur.execute(delete_sql, (order_id_to_delete,))
        conn.commit()

        print(f"주문 ID {order_id_to_delete}가 성공적으로 삭제되었습니다.")

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
    finally:
        conn.close()


def order_management():
    while True:
        print("\n[주문 관리]")
        print("")
        print("1. 주문 정보")
        print("2. 주문 등록")
        print("3. 주문 삭제")
        print("4. 돌아가기")
        print("")
        

    
        choice = input("Select (1/2/3/4): ")
        os.system('clear')

        if choice == "1":
            view_orders()

        elif choice == "2":
            order_registration()
        elif choice == "3":
            delete_order()
        elif choice == "4":
            break  
        else:
            print("오류, 재선택")
