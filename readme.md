# Getting started

This is where you would add all of the relevant information.
How to connect to the database in the `modules/connection.py` file, importing in the `news.sql` file.
All of that wonderful stuff would be handled here.  Example:

Each of the three queries are inside of the modules folder.
Each query will use `connection.py` to make the connection.
The three queries can either be overloaded or they can be changed in the connection folder.

Changing them in the connection folder is preferable.  To do that, go to `modules/connection.py`.

Then change the second argument in the following lines:

```python
dbname = kwargs.get('dbname', 'michaelsoileau')
user = kwargs.get('name', 'michaelsoileau')
password = kwargs.get('password', 'start')
```

To the name, user, and password of the database you are using.
You can download and install the news.sql file at 
[Some Udacity URL](http://www.google.com)

This version uses Python3 with virtualenv to handle dependencies.  Install those dependencies by running

```bash
pip install -r requirements.txt
```

Then run the project by using:

```bash 
python query_runner.py
```