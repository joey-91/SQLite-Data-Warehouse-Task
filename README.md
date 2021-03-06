# Database Schema

![alt text](https://github.com/joey-91/SQLite-Data-Warehouse-Task/blob/main/diagrams/schema.PNG)


# Methodology

I have chosen a STAR schema model for this database, with a fact table and 2 dimension tables that are updated when a new input csv is run through the pipeline.


# Running Pipeline

This process is run from the ETL.py script. I have left commented out print statements so you can easily view the tables being updated at each stage of the code.


#  Slowly Changing Dimensions

To implement this, I've created an autoincrementing Primary Key for each dimension table. So that when new data is added to a dimension table a new key is auto-generated. 


# Unit Tests

I've used the unittest model to provide coverage of my helper functions.
