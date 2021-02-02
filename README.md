# 587_final_project

### Data Generation 
We originally generated the mock data using an open source program on github located at https://github.com/sqalpel/wisconsin. However, after looking at the source code and the resulting csv files produced we realized that the program didn't adhere to the updated Wisconsin Benchmark Schema that accounted for scaleability. We ended up using a program that was developed by Neha Agrawal the Ta. The program is located within this repository at /Part_1/data_generator/data_generator.py. The program was easy to read and was simple to run and generate the data. All that we had to do to generate the data was specify the number of tuples in the source code and it produced a csv file that matched the updated Wisconsin Benchmark Schema that account for scalability. After the csv files were created, we went through each of them and added the column names. To upload the data into BigQuery on the google cloud platform, we uploaded each of the csv files and selected the auto detect schema and input parameters checkbox. BigQuery correctly detected each of the column data types. 

### Database System 
The system that we decided to use for this project is BigQuery on the Google Cloud Platform. BigQuery was chosen for a couple of reasons, the main reason being that we don't have to worry about differences in performance due to CPU/RAM. This would be the case if running on our local machines or by using the postgres hosted on the campus (because of shared hardware). Using BigQuery we can have more confidence that the results from testing are accurate and not influenced by other factors. 

BigQuery is a highly optimized and scalable RDBMS, so it will be difficult to 'break' during benchmarking, but that is exactly what we are setting out to do, as well as evaluate how it stands up to more traditional queries. The literature online indicates that the quickest way to dampen BigQuery's scalability is by introducing custom operations or data types, which we may add later in the project. The work will be in finding *exactly* what causes scalable upsets, such as noticing one custom operation or data type causes slow downs but similar-looking types do not. From there, we may make inferences regarding buffer and cache management, query optimization, and so on. 

### Proof of Implementation
![alt text](Part_1/Screenshots/BigQuery_tables.png)  
![alt text](Part_1/Screenshots/BigQuery_table_data_types.png)  
![alt text](Part_1/Screenshots/BigQuery_table_details.png)  
![alt text](Part_1/Screenshots/BigQuery_tuple_preview.png)  
 
### Lessons learned 
One lesson that we learned is that BigQuery does not allow you to specify Primary or secondary keys. We discovered this when trying to generate the column names from executing a sql query and trying to specify primary keys. After looking through the BigQuery documentation we confirmed this. Are initial impression of BigQuery is that it appears that there is less customization as compared to other database systems. Some of the advantages to BigQuery was that it was extremely simple to set up and create the datasets and the tables. BigQuery also appears to be well documented which will be helpful as we begin to learn the details of the system.

