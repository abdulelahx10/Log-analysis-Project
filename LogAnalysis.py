import psycopg2

DBNAME = "news"


def get_Q1():
    """Return What are the most popular three articles of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select articles.title, count(log.path) as views
            from articles left join log on log.path like '%' || articles.slug
            group by articles.title
            order by views desc limit 3
        """
    c.execute(query)
    articles = c.fetchall()
    db.close()
    return articles


def get_Q2():
    """Return Who are the most popular article authors of all time?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select authors.name, count(log.path) as views
            from authors
            join articles on authors.id = articles.author
            left join log on log.path like '%' || articles.slug
            group by authors.name
            order by views desc
        """
    c.execute(query)
    authors = c.fetchall()
    db.close()
    return authors


def get_Q3():
    """Return On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """
            select * from
                (select time::date as date,
                        (count(case when status like '4%'then 1 else null end)
                        * 100.0 / count(*)) as error_per
                from log
                group by date
                order by error_per desc) errors
            where errors.error_per > 2
        """
    c.execute(query)
    days = c.fetchall()
    db.close()
    return days


if __name__ == '__main__':
    print("Most popular three articles of all time is:")
    # print(get_Q1())
    for row in get_Q1():
        print('"{0}" - {1} views'.format(row[0], row[1]))
    print("--------------------------------------------\n")
    print("Most popular article authors of all time is:")
    # print(get_Q2())
    for row in get_Q2():
        print('"{0}" - {1} views'.format(row[0], row[1]))
    print("--------------------------------------------\n")
    print("Days did more than 1% of requests lead to errors is:")
    # print(get_Q3())
    for row in get_Q3():
        print('"{0}" - {1}% error'.format(row[0], row[1]))
