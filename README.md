# Binary Classification

## Steps to run this project
1. Install the dependencies
```
$ pip install -r requirements.txt
```
2. Create a .env file inside the prediction folder 

For Linux/Unix/Debian Distribution
```
$ cp prediction/.env.example prediction/.env
```
In Windows
```
> @copy prediction\.env.example > prediction\.env
```
3. Run the migrations
```
$ python manage.py migrate
```
4. Run the server
```
$ python manage.py runserver
```
5. Open http://localhost:8000 in your browser