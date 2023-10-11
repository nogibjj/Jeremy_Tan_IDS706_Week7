[![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week6/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week6/actions/workflows/cicd.yml)
## Jeremy_Tan_IDS706_Week7
### File Structure
```
Jeremy_Tan_IDS706_Week7/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── AD_flow.svg
├── data/
│   ├── serve_times.csv
│   └── event_times.csv
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── mylib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── query_log.md
├── README.md
├── requirements.txt
├── setup.sh
├── test_main.py
├── setup.py
└── user_guide.md
```
## Purpose of project
The goal of this project is to create an ETL-Query pipeline utilizing a cloud service like Databricks. This pipeline will involve tasks such as extracting data from FiveThirtyEight's public datasets, cleaning and transforming the data, then loading it into Databricks SQL Warehouse. Once the data is in place, we'll be able to run complex queries that may involve tasks like joining tables, aggregating data, and sorting results. This will be accomplished by establishing a database connection to Databricks. 
## Preparation
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 
3. make your own .env file to store your Databricks' secrets as it requires a conncection to be established to Databricks
3. extract: run `make extract`
4. transform and load: run `make transform_load`
4. query: run `make query` or alternatively write your own query using `etl-query general_query <insert query>`

## Complex Query
Explanations of query:
```sql
SELECT t1.server, t1.opponent,
        AVG(t1.seconds_before_next_point) as avg_seconds_before_next_point,
        COUNT(*) as total_matches_played
    FROM default.servetimesdb t1
    JOIN default.eventtimesdb t2 ON t1.id = t2.id
    GROUP BY t1.server, t1.opponent
    ORDER BY total_matches_played DESC
    LIMIT 10
```
The query retrieves data from two tables (default.servetimesdb and default.eventtimesdb), performs an **inner join** based on the id column, **calculates the average and count** for each unique combination of server and opponent, **orders the results by total_matches_played in descending order**, and limits the output to the top 10 rows. This query can help identify the most played matches grouped by the combination of server and opponent. You can see the results [here](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week6/blob/main/query_log.md) or here:

| server           | opponent             | avg_seconds_before_next_point | total_matches_played |
|------------------|---------------------|-----------------------------|---------------------|
| Nick Kyrgios      | Andy Murray          | 14.15789474                 | 76                  |
| Roger Federer     | Damir Dzumhur        | 16.25                       | 64                  |
| Andy Murray       | Joao Sousa           | 23.47826087                 | 46                  |
| Nicolas Almagro   | Rafael Nadal        | 21.59090909                 | 44                  |
| Bernard Tomic     | Thanasi Kokkinakis  | 20.65789474                 | 38                  |
| Benoit Paire      | Tomas Berdych       | 14.33333333                 | 36                  |
| Rafael Nadal      | Nicolas Almagro     | 29                          | 32                  |
| Carlos Berlocq    | Richard Gasquet     | 28.875                      | 32                  |
| Borna Coric       | Tommy Robredo       | 26.77419355                 | 31                  |
| Pablo Andujar     | Philipp Kohlschreiber | 30.93548387               | 31                  |


## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`

## Simple Vizualization of Process
![ETLQ](adflow.svg)

## References 
1. https://github.com/databricks/databricks-sql-python
2. https://github.com/nogibjj/cloud-database-LAB
3. https://learn.microsoft.com/en-us/azure/databricks/sql/admin/create-sql-warehouse
