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


## Running the the program

cd to the folder of the program:

```
cd Path/to/folder
```

running the program:

```
python3 LogAnalysis.py
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


