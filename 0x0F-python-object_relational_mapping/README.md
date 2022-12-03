## 0x0F. Python - Object-relational mapping

> This repository contains the tasks for `Python - Object-relational mapping` project and a description of what each program or function does:

### Learning Objectives

* Why Python programming is awesome
* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table


### Tasks

#### Task: 0-select_states.py
Write a script that lists all states from the database hbtn_0e_0_usa:
* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed). You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by states.id

#### Task: 1-filter_states.py
Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
* Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed). You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by states.id

#### Task: 2-my_filter_states.py
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed). You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. You must use format to create the SQL query with the user input. Results must be sorted in ascending order by states.id

#### Task: 3-my_safe_filter_states.py
Write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
* Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection). You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by states.id

#### Task: 4-cities_by_state.py
Write a script that lists all cities from the database hbtn_0e_4_usa
* Your script should take 3 arguments: mysql username, mysql password and database name. You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by cities.id. You can use only execute() once

#### Task: 5-filter_cities.py
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
* Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!). You must use the module MySQLdb (import MySQLdb). Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by cities.id. You can use only execute() once

#### Task: model_state.py
Write a python file that contains the class definition of a State and an instance Base = declarative_base():
* State class: inherits from Base. links to the MySQL table states. class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key. class attribute name that represents a column of a string with maximum 128 characters and can’t be null. You must use the module SQLAlchemy. Your script should connect to a MySQL server running on localhost at port 3306

#### Task: 7-model_state_fetch_all.py
Write a script that lists all State objects from the database hbtn_0e_6_usa
* Your script should take 3 arguments: mysql username, mysql password and database name. You must use the module SQLAlchemy. You must import State and Base from model_state - from model_state import Base, State. Your script should connect to a MySQL server running on localhost at port 3306. Results must be sorted in ascending order by states.id

#### Task: 


#### Task: 


#### Task: 


#### Task: 


#### Task: 


#### Task: 


#### Task: 


#### Task: 






___

#### Files:
* []()

