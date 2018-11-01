#!/usr/bin/env python3
import psycopg2

DBNAME = "news"


def execute_query(QUERY_STRING):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    try:
        c.execute(QUERY_STRING)
    except psycopg2.Error as e:
        print(e.pgerror)
        pass
    result = c.fetchall()
    db.close()
    return result


def get_Q1():
    """Return What are the most popular three articles of all time"""
    query = """
            select articles.title, count(log.path) as views
            from articles left join log on log.path like '%' || articles.slug
            group by articles.title
            order by views desc limit 3
        """
    articles = execute_query(query)
    return articles


def get_Q2():
    """Return Who are the most popular article authors of all time"""
    query = """
            select authors.name, count(log.path) as views
            from authors
            join articles on authors.id = articles.author
            left join log on log.path like '%' || articles.slug
            group by authors.name
            order by views desc
        """
    authors = execute_query(query)
    return authors


def get_Q3():
    """Return On which days did more than 1% of requests lead to errors"""
    query = """
            select * from
                (select time::date as date,
                        (count(case when status like '4%'then 1 else null end)
                        * 100.0 / count(*)) as error_per
                from log
                group by date
                order by error_per desc) errors
            where errors.error_per > 1
        """
    days = execute_query(query)
    return days


if __name__ == '__main__':
    print("Most popular three articles of all time is:")
    # print(get_Q1())
    for row in get_Q1():
        print('"{0}" - {1} views'.format(row[0], row[1]))
    print("-" * 50, "\n")
    print("Most popular article authors of all time is:")
    # print(get_Q2())
    for row in get_Q2():
        print('"{0}" - {1} views'.format(row[0], row[1]))
    print("-" * 50, "\n")
    print("Days did more than 1% of requests lead to errors is:")
    # print(get_Q3())
    for row in get_Q3():
        print('"{0}" - {1}% error'.format(row[0], row[1]))
