from sqlalchemy import create_engine

engine = create_engine('sqlite:///test.db')

# 接続
with engine.connect() as con:

    # Drop文を実行
    con.execute("DROP TABLE IF EXISTS USERS")

    # Create文を実行
    con.execute(
        "CREATE TABLE USERS(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

    # 投入データの定義
    rows = (
        {"id": 1, "name": "Sato", "age": 31},
        {"id": 2, "name": "Suzuki", "age": 18},
        {"id": 3, "name": "Yamada", "age": 40},
        {"id": 4, "name": "Kuro", "age": 30},
    )

    # Insert文を実行
    for row in rows:
        con.execute(
            f"INSERT INTO USERS (id, name, age) VALUES({row['id']}, '{row['name']}', {row['age']})")

    # Select文を実行
    rows = con.execute("SELECT * FROM USERS;")
    for row in rows:
        print(row)

    # Update文を実行
    con.execute("UPDATE USERS SET age=42 WHERE id = 3")

    # Delete文を実行
    con.execute("DELETE FROM USERS WHERE id = 4")

    # 更新の確認
    print('***更新後***')
    rows = con.execute("SELECT * FROM USERS;")
    for row in rows:
        print(row)
