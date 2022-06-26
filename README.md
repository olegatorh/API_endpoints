# API_endpoints
test task

for run this project you need use following steps:
1) open your terminal, go to Desktop or another folder by 'cd' command;
2) paste in terminal: "git clone https://github.com/olegatorh/API_endpoints.git"; 
3) open API_endpoints and run: "python -m venv <name_of_virtualenv>";
4) then activate it, (linux): "source <name_of_virtualenv>/bin/activate", (windows): "<name_of_virtualenv>/Source/activate.bat";
5) back to previos folder wich includes manage.py and run: "pip install --upgrade pip" and after "pip install -r requirements.txt";
6) now you need fill your settings for mysql server, in folder APIendpoints rename file .env.example to .env and fill all parameters, hint(secret key you take from here https://djecrety.ir/) all mysql database paramenters from mysqlserver;
7) run this command for adding tables in your database: "python manage.py makemigrations" and after "python manage.py migrate"
8) create superuser by python manage.py createsuperuser;
9) after all dependencies will install and you filled .env run: "python manage.py runserver";

# DESCRIPTION
to check all avilable api endpoint you need to go to http://localhost:8000/api/
there you will see page with this urls
{
    "doctor": "http://127.0.0.1:8000/api/doctor/",
    "direction": "http://127.0.0.1:8000/api/direction/"
}

in doctor page you can add new doctors, and ordering, searching, filtering by filter button, and also you can do same thing by using url;
in direction page you can only create a direction;
for looking  how use url filters click on filters button then  press needed filters or sort and after just check url it will be change for your filters,

Admin panel: http://127.0.0.1:8000/admin/
use your credentials from step 7 lo login
here you can add a doctors and directions, filter them, sort them, delete, edit, create new. 
