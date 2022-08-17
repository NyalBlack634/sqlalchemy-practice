from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine

engine = create_engine('sqlite:///test.db')

# 接続
with engine.connect() as con:

    # Drop文を実行
    con.execute("DROP TABLE IF EXISTS USERS")

meta = MetaData(engine)
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

# metaデータの内容をデータベースに反映
meta.create_all()

with engine.connect() as con:
    # DBをアクセスして確認

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

    # Select文を実行する
    rows = con.execute("SELECT * FROM USERS")
    for row in rows:
        print(row)
