# Logs Analysis
###### Tianrui Zhang
## Program Description
The program in this project will connect to a web server log database, use PostgreSQL queries to analyze log data and print out the answers to some questions. No user input is needed.

## Instruction
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html), the virtual machine.
2. Download Vagrant [configuration file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
3. Assuming the configuration file is located inside your **Downloads** folder, change to the **vagrant** directory in the terminal with `cd Downloads/FSND-Virtual-Machine/vagrant`.
4. Start Vagrant by running the command `vagrant up`.
5. Run `vagrant ssh` to log in to the newly installed Linux Virtual Machine.
6. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Put this file into the **vagrant** directory, which is shared with the virtual machine.
7. Download the **code.py** in this submission and put it into the **vagrant** directory.
8. Change to the shared directory by running `cd /vagrant`.
9. Load the data by using the command `psql -d news -f newsdata.sql`.
10. Import the views by using the command `psql -d news -f create_views.sql`.
11. Run `python3 code.py` to execute this program.

## Views Created

`CREATE VIEW slug_views AS
    SELECT split_part(PATH, '/', 3) AS slug,
    count(split_part(PATH, '/', 3)) AS views
    FROM log
    GROUP BY slug;`

`CREATE VIEW author_articles AS
    SELECT authors.name, articles.slug
    FROM authors, articles
    WHERE authors.id = articles.author;`

`CREATE VIEW author_views AS
    SELECT name, views
    FROM author_articles, slug_views
    WHERE author_articles.slug = slug_views.slug
    ORDER BY views DESC;`

`CREATE VIEW date_status AS
    SELECT time::DATE as date,
    status,
    COUNT(status)
    FROM log
    GROUP BY date, status;`

`CREATE VIEW date_status_percentage AS
    SELECT *,
    count / SUM(count) OVER(PARTITION BY date) AS percentage
    FROM date_status;`
