import pymysql

# MySQL 연결 설정
connection = pymysql.connect(
    host='localhost',         # Docker 컨테이너가 로컬에서 실행되므로 localhost
    user='root',              # MySQL 사용자 이름
    password='1234',          # MySQL 비밀번호
    database='classdb',     # db.sql에서 생성한 데이터베이스 이름
    port=3306                # Docker에서 노출된 MySQL 포트
)

try:
    # 커서 생성
    cursor = connection.cursor()

    # 예제: 데이터베이스에 있는 테이블 목록 가져오기
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("Tables in the database:")
    for table in tables:
        print(table[0])

finally:
    # 연결 종료
    connection.close()
