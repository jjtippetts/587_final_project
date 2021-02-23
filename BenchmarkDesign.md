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
**Measuring Performance:** Query Insights is a built in feature. It allows you to monitor query execution time and database load for specific queries.
As a bonus, one can use built-in postgres features, such as ps_stat_statements that can be run locally to record the runtime of queries. 

## Performance Experiment Design
Queries are expected to run around half a minute. 


**1.**
* i. What performance issue are you testing?  
Compare Query performance of an index on struct data type (postgres) and no index on struct data type (Big Query). This test will use a GIN index.
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?  
We will be using a slightly modified schema of the wisconsin benchmark schema that includes custom data types. These custom datatypes will be structs that contain a unique integer and unique string that are copies of the unique2 and stringu1 attributes. The table will be a single size of 100k tuples.
* iii. What queries will you run? (provide the SQL)  

SELECT COUNT(customDataType.structNum) AS customInt  
FROM 100Ktup  
WHERE customDataType.structNum BETWEEN 0 AND 99  


SELECT COUNT(customDataType.structNum) AS customInt  
FROM 100Ktup  
WHERE customDataType.structNum BETWEEN 792 AND 1791  

* iv. What results do you expect to get?  
It is expected that postgres will have better performance because of the ability to have indexes on custom data types. 


**2.**
* i. What performance issue are you testing?  
Compare Query performance of an index on struct data type (postgres) and no index on struct data type (Big Query). This test will use a GIST index.
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?  
We will be using a slightly modified schema of the wisconsin benchmark schema that includes custom data types. These custom datatypes will be structs that contain a unique integer and unique string that are copies of the unique2 and stringu1 attributes. The table will be a single size of 100k tuples.
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
Compare Query performance of an index on struct data type (postgres) and no index on struct data type (Big Query). This test will use a b-tree index
on a composite type (expression).
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?  
We will be using a slightly modified schema of the wisconsin benchmark schema that includes custom data types. These custom datatypes will be structs that contain a unique integer and unique string that are copies of the unique2 and stringu1 attributes. The table will be a single size of 100k tuples.
* iii. What queries will you run? (provide the SQL)  

SELECT COUNT(customDataType.structNum) AS customInt  
FROM 100Ktup  
WHERE customDataType.structNum BETWEEN 0 AND 99  


SELECT COUNT(customDataType.structNum) AS customInt  
FROM 100Ktup  
WHERE customDataType.structNum BETWEEN 792 AND 1791  

* iv. What results do you expect to get?  
It is expected that postgres will have better performance because of the ability to have indexes on custom data types. 


**4.**

* i. What performance issue are you testing? Grabbing multiple attributes in a tuple as the database scales
* ii. What data sets will you include in the test? Will you use a single size data set or will you use multiple data sets of different sizes?
Use 1k, 10k, 100k, and 1000k relations
* iii. What queries will you run? (provide the SQL)
INSERT INTO TMP
SELECT *
FROM 100Ktup  
WHERE customDataType.structNum BETWEEN 0 AND 99  

INSERT INTO TMP
SELECT *
FROM 1000Ktup  
WHERE customDataType.structNum BETWEEN 792 AND 1791  

* iv. What results do you expect to get?
It is expected that the postgres database will have the best query performance because it is a relational database which is optimized for storing rows whereas Google Big Query is a cloumnar database and optimized for storing columns of data. Since this query selects all of the data in a row, it is assummed that postgres will perform better.


## Lessons Learned
One lesson that we learned it that Google Big Query does not take in csv data with custom data types because they don't support nested data. To get around this you either have to load the data in using a filetype that does support nested data or if the struct data values are based off of other attributes you can add the struct data type after the rest of the data has been loaded in. Then fill in the struct column using the values from the other columns. We chose to load in the data using the second approach because are script to load in the data created a csv file.

Furthermore, although deploying our databases through Google Cloud and virtual machines is generally quick and easy, there are some annoying drawbacks
to not being given superuser priveleges on the Cloud, which can needlessly complicate testing. For example, using the PostgreSQL function COPY is off-
limits when using a Cloud SQL instance, save some workarounds that are hit-or-miss. This causes us to work around the infrastructure more than we 
planned, but is to be expected to some degree for enterprise level software.