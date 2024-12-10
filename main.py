import pymysql
import lib.customer as customer
import lib.goods as goods
import lib.order as order
import os


conn = pymysql.connect(
    host='localhost',        
    user='root',              
    password='1234',         
    database='classdb',    
    port=3306,
    charset='utf8mb4'                
)
cur = conn.cursor()

   

def order_inquiry():
    print("\n[주문 조회] - Order inquiry...")

os.system('clear')
print("*" * 5, "고급프로그래밍실습 과제", "*" * 5)
print("")
print("")
print(" " * 15, "MySQL")
print("-" * 35)


while True:
    print("\nSelect an option:")
    print("")
    print("1. 고객 관리")
    print("2. 상품 조회")
    print("3. 주문 조회")
    print("4. 종료")
    print("")

  
    choice = input("select (1/2/3/4): ")
    print("-" * 35)
    os.system('clear')

    if choice == "1":
        customer.customer_management()  

        
    elif choice == "2":
        goods.goods_management()
        print("-" * 35)
    elif choice == "3":
        order.order_management()
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("오류, 재선택")
