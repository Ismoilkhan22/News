from contextlib import closing
from django.db import connection
from methodism import dictfetchall, dictfetchone


def search_sql(key):
    sql = f"""
    SELECT title ,id, view, date, short_desc,img from news_new
    where title like '%{key}%' or short_desc like '%{key}%' or desc like '%{key}%'
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)
    return result
