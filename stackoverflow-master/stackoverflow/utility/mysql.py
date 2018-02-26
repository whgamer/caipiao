import json
import pymysql

conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="0303", db="chenx", charset="utf8")
cur = conn.cursor()

# 创建数据库表
"""
create table stackoverflow(
    s_links int(11) not null primary key,
    s_views int(11),
    s_votes int(11),
    s_answers int(11),
    s_tags text,
    s_questions text
);

"""
with open(r"e:\python\stackoverflow\data\result.json", "r", encoding="utf-8") as f:
    data = json.load(f)

    def insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions):

        sql = "insert into stackoverflow(s_links, s_views, s_votes, s_answers, s_tags, s_questions) " \
              "values(%s, %s, %s, %s, %s, %s)"
        value = (s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        cur.execute(sql, value)
        conn.commit()
        print("Insert s_links: " + s_links)

    for _, value in enumerate(data):

        s_links, s_views, s_votes, s_answers, s_tags, s_questions = value
        try:
            insert_db(s_links, s_views, s_votes, s_answers, s_tags, s_questions)
        except Exception as e:
            print(e)