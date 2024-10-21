#csvファイルに保存したデータをデータベースのProductテーブルに挿入

import csv
from sqlalchemy.orm import Session
from .mymodels import Product
from .database import engine

# CSVファイルのパス
csv_file_path = "C:/Users/kouji/Desktop/Tech0/step4/tech0_step4_pos_app_items.csv"

# データベースへのセッションを作成
session = Session(bind=engine)

# CSVファイルを開いて読み込む
with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    print("CSV Columns:", reader.fieldnames)  # ここでカラム名を表示
    for row in reader:
        print(row)  # 行データを表示して確認
        # Productオブジェクトを作成
        product = Product(
            CODE=row['CODE'],  # CSVのカラム名に合わせる
            NAME=row['NAME'],
            PRICE=int(row['PRICE'])
        )
        # データベースに追加
        session.add(product)

# データをコミットして保存
session.commit()

# セッションを閉じる
session.close()