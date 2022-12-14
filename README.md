create env and install packages in the requirements.txt file
create database sm (set username and password in settings file)
<!-- drop database sm; -->
activate environment
RUN COMMAND python manage.py migrate
RUN COMMAND python manage.py runserver

API discription

USER CREATION
method - POST
url - localhost:8000/user/register
payload - {"username":"joedam", "password":"testmypass", "password2":"testmypass", "email":"joe@gmail.com","first_name":"joe", "last_name":"george"}

GET TOKEN
method - POST
url - localhost:8000/api-token-auth
payload - {"username":"joedam", "password":"testmypass"}

GET USER DEATILS
method - GET [header(Authorization: Token <key>)]
url - localhost:8000/user/get-details

FOLLOW USER
method - POST [header(Authorization: Token <key>)]
url - localhost:8000/user/follow
payload - {"id":2}

UNFOLLOW USER
method - POST [header(Authorization: Token <key>)]
url - localhost:8000/user/unfollow
payload - {"id":2}

MAKE A POST(tweet)
method - POST [header(Authorization: Token <key>)]
url - localhost:8000/post/new
payload (form-data) with keys 
    text hold msg 
    media holds image/video file

DELETE A POST(remove a tweet)
method - DELETE
url - localhost:8000/post/new
{"id":2}

LATER you can go to http://localhost:8000/