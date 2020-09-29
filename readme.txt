1. install virtual environment : pip install virtualenv
2. create virtual environment : virtualenv virtualenv_name
3. activate virtual environment  : virtualenv_name\scripts\activate

*if facing an error in power shell then :
- open it as adminstrator then type : Set-ExecutionPolicy remoteSigned
- When PowerShell asks you if you want to make the changes, Enter A on your keyboard to say yes to all and then hit enter.
- Close PowerShell and open it in your project folder again.
- go to step no. 3

4. install django : pip install django
5. start django project :  django-admin startproject BuyersStation
6. apply migration so you can use the app : python manage.py migrate



7. start an app : django-admin startapp products
  