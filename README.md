# StockTransactions


**INSTALATION**\
1- **clone the project** -> git clone https://github.com/sepide1371/StockTransactions.git

2- **create a virtual environment** -> virtualenv venv

3- **install required packages(in root of project)** -> pip install -r requirements.txt

4-**run tests** -> python manage.py test

5- **run project(in root of project)** -> python manage.py runserver


**SUPER USER INFOS**\
test super user info 
    username: "trade", \
    password: "123", \
    client_id: "g1WHTqymx0t4hiOFvo8DjKfHu6ZwiBDgyRbVxgvK", \
    clien_secret: "hMZYeEw693PInSI3KhUOjluHONQfvnyaejwAeGN9RH9adkZf5OaYhU4TQGDU96elKUq0K8k223AKj9HJLPoDeByXwORcS63GN4fm8z6sltHRBHwxvY9s1r9kPob8XjqB"



**POST MAN COLLECTION\**
postman collection file uploaded in root of project

**SWAGGER DOC**\
http://127.0.0.1:8000/swagger/


**ATTENTION**\
all of api uses oauth2-

**for get token call** -> http://127.0.0.1:8000/oauth/token/


and set body like below in 'application/x-www-form-urlencoded' Content-Type:

'client_id=g1WHTqymx0t4hiOFvo8DjKfHu6ZwiBDgyRbVxgvK&grant_type=password&username=trade&password=123'


and for use refresh token set body like below in 'application/x-www-form-urlencoded' Content-Type::

'client_id=g1WHTqymx0t4hiOFvo8DjKfHu6ZwiBDgyRbVxgvK&grant_type=refresh_token&refresh_token=dvHxx7HOVrmoCcYD7Qx9zwnAy4U0Mx'