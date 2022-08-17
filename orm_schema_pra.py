from sqlalchemy import Table, Column, Integer, String, MetaData

meta = MetaData()
users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )

# Usersテーブルの確認
print(meta.tables['Users'])

# すべてのテーブルの確認
for table in meta.tables:
    print(table)

# columns, もしくはcでカラム名の参照が可能
print(users.columns.name)
print(users.c.name)

# すべてのカラムの確認
for col in users.c:
    print(col)

# primary_keyで主キーを参照可能
for pk in users.primary_key:
    print(pk)

# その他のカラムの属性の確認
print(users.c.id.name)
print(users.c.id.type)
print(users.c.id.nullable)
print(users.c.id.primary_key)
