# Udacity Log analysis Project

Python program that print an analysis of a Database log

## Getting Started

### Tables:
The program will work only on these Tables:

```
                                  Table "authors"
 Column |  Type   |                      Modifiers                       
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    | 
 id     | integer | not null default nextval('authors_id_seq'::regclass)

========================

                                  Table "articles"
 Column |           Type           |                       Modifiers                       
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     | 
 body   | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)

========================

                                  Table "log"
 Column |           Type           |                    Modifiers                     
--------+--------------------------+--------------------------------------------------
 path   | text                     | 
 ip     | inet                     | 
 method | text                     | 
 status | text                     | 
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
```

### Prerequisites

The python program require psycopg2 library to run, to install:

```
pip install psycopg2
```

[Vagrant](https://www.vagrantup.com/downloads.html) and [VirtualBox](https://www.virtualbox.org/wiki/Downloads) are needed

The used [Vagrantfile](https://www.dropbox.com/s/w3gsd5ve3t6qzs1/Vagrantfile?dl=0) to create Vagrant

Download [newsdata.sql](https://www.dropbox.com/s/vf6rab76chg685d/newsdata.sql?dl=0) to setup the database and place it in repository folder

## Running the the program
cd to the folder of the program:

```
cd Path/to/folder
```

Before running the program you need to setup the database by running newsdata.sql:

```
psql -d news -f newsdata.sql
```

running the program:

```
python3 LogAnalysis.py
```

## Functions
There's four main functions and a main to run them:

The following function connect to the database and execute the given query and return the result:

```
def execute_query(QUERY_STRING)
```

The following function return the most popular three articles of all time:

```
def get_Q1()
```

Used query in the function:

```
select articles.title, count(log.path) as views
from articles left join log on log.path like '%' || articles.slug
group by articles.title
order by views desc limit 3
```

The following function return the most popular article authors of all time:

```
def get_Q2()
```

Used query in the function:

```
select authors.name, count(log.path) as views
from authors
join articles on authors.id = articles.author
left join log on log.path like '%' || articles.slug
group by authors.name
order by views desc
```

The following function return the days did more than 1% of requests lead to errors:

```
def get_Q3()
```

Used query in the function:

```
select * from
    (select time::date as date,
            (count(case when status like '4%'then 1 else null end)
            * 100.0 / count(*)) as error_per
    from log
    group by date
    order by error_per desc) errors
where errors.error_per > 1
```

## Output

```
Most popular three articles of all time is:
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views
--------------------------------------------

Most popular article authors of all time is:
"Ursula La Multa" - 507594 views
"Rudolf von Treppenwitz" - 423457 views
"Anonymous Contributor" - 170098 views
"Markoff Chaney" - 84557 views
--------------------------------------------

Days did more than 1% of requests lead to errors is:
"2016-07-17" - 2.2626862468027260% error
```

## Authors

* **Abdulelah Alshalhoub** - *Initial work* - [abdulelahx10](https://github.com/abdulelahx10)
