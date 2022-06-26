# API_endpoints
test task

for run this project you need use following steps:
1) open your terminal, go to Desktop or another folder by 'cd' command;
2) paste in terminal: "git clone https://github.com/olegatorh/API_endpoints.git"; 
3) open API_endpoints and run: "python3 -m venv <name_of_virtualenv>";
4) then activate it, (linux): "source <name_of_virtualenv>/bin/activate", (windows): "<name_of_virtualenv>/Source/activate.bat";
5) back to previos folder wich includes manage.py and run: "pip install --upgrade pip" and after "pip install -r requirements.txt";
6) now you need fill your settings for mysql server, in folder APIendpoints rename file .env.example to .env and fill all parameters, hint(secret key you take from here https://djecrety.ir/) all mysql database paramenters from mysqlserver
7) create superuser by python manage.py createsuperuser
8) after all dependencies will install and you filled .env run: "python manage.py runserver";

# DESCRIPTION
to check all avilable api endpoint you need to go to http://localhost:8000/api/
there you will see page with this urls
{
    "doctor": "http://127.0.0.1:8000/api/doctor/",
    "direction": "http://127.0.0.1:8000/api/direction/"
}

in doctor page you can 
