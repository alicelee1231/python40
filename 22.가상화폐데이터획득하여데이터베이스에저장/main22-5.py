import pandas as pd
import sqlite3

db_path = r"22.가상화폐데이터획득하여데이터베이스에저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)
readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col='index')
readed_df.to_sql('BTC_NEW', con, if_exists='replace')
print(readed_df)