CREATE VIEW slug_views AS
    SELECT split_part(PATH, '/', 3) AS slug,
    count(split_part(PATH, '/', 3)) AS views
    FROM log
    GROUP BY slug;

CREATE VIEW author_articles AS
    SELECT authors.name, articles.slug
    FROM authors, articles
    WHERE authors.id = articles.author;

CREATE VIEW author_views AS
    SELECT name, views
    FROM author_articles, slug_views
    WHERE author_articles.slug = slug_views.slug
    ORDER BY views DESC;

CREATE VIEW date_status AS
    SELECT time::DATE as date,
    status,
    COUNT(status)
    FROM log
    GROUP BY date, status;

CREATE VIEW date_status_percentage AS
    SELECT *,
    count / SUM(count) OVER(PARTITION BY date) AS percentage
    FROM date_status;
