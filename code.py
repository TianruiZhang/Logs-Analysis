#!/usr/bin/env python3

import psycopg2


def fetch_popular_articles():
    connection = psycopg2.connect(dbname="news")
    cursor = connection.cursor()
    cursor.execute('''
    SELECT articles.title, slug_views.views
    FROM articles, slug_views
    WHERE articles.slug = slug_views.slug
    ORDER BY views DESC
    LIMIT 3
    ''')
    rows = cursor.fetchall()
    print("1. What are the most popular three articles of all time?")
    for row in rows:
        print("\"" + str(row[0]) + "\"" + " - " + str(row[1]) + " views")
    cursor.close()
    connection.close()


def fetch_popular_authors():
    connection = psycopg2.connect(dbname="news")
    cursor = connection.cursor()
    cursor.execute('''
    SELECT name, SUM(views) AS views
    FROM author_views
    GROUP BY name
    ORDER BY views DESC
    ''')
    rows = cursor.fetchall()
    print("2. Who are the most popular article authors of all time?")
    for row in rows:
        print(str(row[0]) + " - " + str(row[1]) + " views")
    cursor.close()
    connection.close()


def fetch_worst_days():
    connection = psycopg2.connect(dbname="news")
    cursor = connection.cursor()
    cursor.execute('''
    SELECT TO_CHAR(date, 'Mon dd, YYYY'), TO_CHAR(100*percentage, '9D99%')
    FROM date_status_percentage
    WHERE percentage>0.01 AND status = '404 NOT FOUND'
    ''')
    rows = cursor.fetchall()
    print("3. On which days did more than 1% of requests lead to errors?")
    for row in rows:
        print(str(row[0]) + " -" + str(row[1]) + " errors")
    cursor.close()
    connection.close()


if __name__ == "__main__":
    fetch_popular_articles()
    print("\n")
    fetch_popular_authors()
    print("\n")
    fetch_worst_days()
