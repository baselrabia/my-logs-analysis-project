# my-logs-analysis-project
Logs Analysis Project - Udacity Full Stack Web Developer nanodegree 2019

Building an informative summary from logs by sql database queries.

Interacting with a live database "newsdata.sql" from the command line and from the python code. 

This project is a part of the Udacity's Full Stack Web Developer Nanodegree.

## Technologies used
1. PostgreSQL
2. Python code with DB-API
3. Linux-based virtual machine (VM) Vagrant

## What is the output of this project my-logs-analysis-project
Reporting tool should answer the following questions:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

#### Output File  ```output for logs project .txt ``` is attached in this repository you can check it.

* Project follows good SQL coding practices: Each question should be answered with a single database query.  
* The code presents its output in clearly formatted plain text.


## Project Requirements
System setup and how to view this project:

This project makes use of Udacity's Linux-based virtual machine (VM) configuration which includes all of the necessary software to run the application.

1. Download [Vagrant](https://www.vagrantup.com/) and install.
2. Download [Virtual Box](https://www.virtualbox.org/) and install. 
3. Clone this repository to a directory of your choice.
4. Download the **newsdata.sql** (extract from **newsdata.zip**) and **logs_project.py** files from the respository and move them to your **vagrant** directory within your VM.

#### Run these commands from the terminal in the folder where your vagrant is installed in: 
1. ```vagrant up``` to start up the VM.
2. ```vagrant ssh``` to log into the VM.
3. ```cd /vagrant``` to change to your vagrant directory.
4. ```psql -d news -f newsdata.sql``` to load the data and create the tables.
5. ```python logs_project.py``` to run the reporting tool.

## Documentation Resources of PostgreSQL 
* [PostgreSQL 9.5 Documentation](https://www.postgresql.org/docs/9.5/static/index.html)
