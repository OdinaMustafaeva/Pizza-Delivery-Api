# Pizza-Delivery-Api
This is a REST API for a Pizza delivery service built for fun and learning with FastAPI, SQLAlchemy and PostgreSQL. The video playlist is 
[here](https://www.youtube.com/playlist?list=PLEt8Tae2spYnLMAf8RGCNYhovIFZHVsPP)


## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
| *POST* | ```/auth/signup/``` | _Register new user_| _All users_|
| *POST* | ```/auth/login/``` | _Login user_|_All users_|
| *POST* | ```/auth/refresh/``` | _refresh token_|_All users_|
| *GET* | ```/orders/``` | _User order_|_All users_|
| *PUT* | ```/order/{order_id}/update``` | _Update an order_|_All users_|
| *DELETE* | ```/order/{order_id}/delete/``` | _Delete/Remove an order_ |_All users_|
| *POST* | ```/orders/create/``` | _Create order_|_All users_|
| *GET* | ```/orders/{order_id}``` | _Order id _|_All users_|
| *GET* | ```/user/porfile``` | _User Profile_|_User Profile_|
| *GET* | ```/docs/``` | _View API documentation_|_All users_|

## How to run the Project
- Install Postgreql
- Install Python
- Git clone the project with ``` git clone https://github.com/jod35/Pizza-Delivery-API.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Set Up your PostgreSQL database and set its URI in your ```database.py```
```
engine=create_engine('postgresql://postgres:<username>:<password>@localhost/<db_name>',
    echo=True
)
```

- Create your database by running ``` python init_db.py ```
- Finally run the API
``` uvicorn main:app ``
