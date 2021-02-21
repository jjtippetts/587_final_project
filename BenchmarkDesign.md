# Benchmark Design
**Jordan Tippetts**  
**Adam Craig**

## System Selection
We chose to compare the performance of Google Big Query and Google Cloud SQL for Postgres. Specifically, we are interested in comparing the query performance of custom datatypes. Custom data types were originally not included in the original and updated wisconsin benchmark schema so it will be interesting to determine how the query performance differs in both the databases.

## System Research

### Big Query 
One of the first things that we noticed when researching Google Big Query is that it is not very customizable. For instance, Google Big Query doesn't allow for any sort of primary or secondary index to be created. This is because Google Big Query and many other cloud databases are columner databases. Columner databases are optimized for storing columns of data as compared to rows of data. Columnar datatabase are typically better suited to scale and big data processing.
**Measuring Performance:** 

### Google Cloud SQL for Postgres
Postgress in contrast to google Big Query, does allow for primary and secondary indexes. Postgress is also a relational database and is thus optimized for storing and retreiving rows of data. Postgres is also typically better at performing table joins of data.
**Measuring Performance:** Query Insights is a built in feature. It allows you to monitor query execution time and database load for specific queries

## Performance Experiment Design
Queries are expected to run around half a minute.

**1.**
* i. What performance issue are you testing? 
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?
* iii. What queries will you run? (provide the SQL)
* iv. What results do you expect to get?

**2.**
* i. What performance issue are you testing? 
Compare Query performance of an index on struct data type (postgres) and no index on struct data type (Big Query). 
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?
We Will be using a slightly modified schema of the wisconsin benchmark schema that includes custom data types. These custom datatypes will be structs that contain a unique integer and unique string that are copies of the unique2 and stringu1 attributes. The table will be a single size of 100k tuples.
* iii. What queries will you run? (provide the SQL)  

SELECT COUNT(customDataType.structNum) AS customInt
FROM 100Ktup
WHERE customDataType.structNum BETWEEN 0 AND 99  


SELECT COUNT(customDataType.structNum) AS customInt
FROM 100Ktup
WHERE customDataType.structNum BETWEEN 792 AND 1791

* iv. What results do you expect to get?
It is expected that postgres will have better performance because of the ability to have indexes on custom data types.

**3.**

* i. What performance issue are you testing? 
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?
* iii. What queries will you run? (provide the SQL)
* iv. What results do you expect to get?
**4.**

* i. What performance issue are you testing? 
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?
* iii. What queries will you run? (provide the SQL)
* iv. What results do you expect to get?


## Lessons Learned

