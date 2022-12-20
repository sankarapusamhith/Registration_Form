# registrationform_flask

> Clone Project 
1. Run following commands in cmd .
* git clone https://github.com/sankarapusamhith/registrationform_flask.git
* cd registrationform_flask

> Create Virtual Environment
1. Run following commands in cmd .
* pip install virtualenv 
* python -m venv env
* env\Scripts\activate

> Install required libraries
1. Run following command in cmd .
* python -m pip install -r requirements.txt 

> Create db instance
1. Run following command in cmd .
  * set FLASK_APP=run
* flask shell
2. Above command will open python shell . Run following commands in python shell .
* from home import db
* db.create_all()
* from home.models import User 
* exit()

> Start flask app
1. Run following command in cmd .
* flask run.py
2. Once the app is up and running , we'll get a link in terminal from which we can access the application .


> Info
* In this application we can register across 4 different roles .
* Register one user with each role to get clear picture of accessibility wrt to each role .
* After login users page will there , where visibilty access varies differ from each role .

