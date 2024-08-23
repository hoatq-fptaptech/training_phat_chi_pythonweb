from sqlalchemy import create_engine
from pandas import *
#connect db
engine = create_engine('mysql+pymysql://root:root@localhost:3306/training_blog')

def read_data(sql):
    data = read_sql_query(sql, engine)
    return data.to_dict()
def insert_post(post):
    dataset = DataFrame({
        "title": [post["title"]],
        "author": [post["author"]],
        "content": [post["content"]],
    })
    dataset.to_sql('posts', engine, if_exists='append', index=False)