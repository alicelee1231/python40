import pandas as pd
import sqlite3

db_path = r"22.가상화폐데이터획득하여데이터베이스에저장\coin.db"
con = sqlite3.connect(db_path,isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col='index')

print(readed_df)