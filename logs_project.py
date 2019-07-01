#!/usr/bin/env python
# Import psycopg2 module
import psycopg2


# helper function, help to start to connect database and fetch data from sql.
def run_query(sql):
    # Connect database
    conn = psycopg2.connect("dbname=news")
    # Start cursor to run queries and get results
    curs = conn.cursor()
    # Execute SQL query by cursor
    curs.execute(sql)
    # Fetch all results from the cursor and print them
    data = curs.fetchall()
    return data, conn


""" Get 3 popular articles
Return list of 3 most popular articles,with the top article at first."""


def popular_articles():

    print('1- Get 3 popular articles')

    sql = """select title ,num from
    (select substr(path,10),count(*) as num from log
    where path != '/' group by path) as clicks,articles
    where clicks.substr = slug order by num desc limit 3;"""

    run = run_query(sql)
    data = run[0]
    conn = run[1]

    for table in data:
        print('" ' + table[0] + ' "' + ' ----- ' + str(table[1]) + ' views')

    # Close connection
    conn.close()
    pass


# Get popular authors ..Return list of popular article authors,


def popular_authors():

    print('2- Get popular authors')

    sql = """select name , views from (select author , sum(num)
    as views from (select substr(path,10),count(*) as num from log
    where path != '/' group by path) as clicks,articles
    where clicks.substr = slug group by author order by views desc )
    as viewtotal,authors
    where author = authors.id;"""

    run = run_query(sql)
    data = run[0]
    conn = run[1]

    for table in data:
        print('" ' + table[0] + ' "' + ' ----- ' + str(table[1]) + ' views')

    # Close connection
    conn.close()
    pass


# Get Day on which >1% of HTTP errors from requests

def http_errors():

    print('3- Get Day on which more than 1 percentage of HTTP errors')

    sql = """select to_char(date,'MON DD,YYYY'),percentage_of_error from
    (select t_all_requests.date, all_requests, error_requests ,
    ((error_requests::float/ all_requests)*100) as percentage_of_error  from
    (select date_trunc('day', time) as date, count(*) as all_requests from log
    group by date ) as t_all_requests ,
    (select date_trunc('day', time) as date, count(*)
    as error_requests from log
    where status = '404 NOT FOUND' group by date) as t_error_requests
    where t_all_requests.date = t_error_requests.date
    order by t_all_requests.date desc) as t_perc
    where percentage_of_error > 1 ;"""

    run = run_query(sql)
    data = run[0]
    conn = run[1]

    for table in data:
        print(table[0] + ' ----- ' + str(table[1])[0:4] + '% errors')

    # Close connection
    conn.close()
    pass


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    http_errors()
