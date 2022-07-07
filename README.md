# Software Development Students motivation app

####  Reuben Kipkemboi
#### By Victoria Makena
####  Sandra Dindi
####  Ivy Kabere
####  Josephat Muriu

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#installation-requirements)
+ [Technology Used](#technologies-used)
+ [License](#license)
+ [Authors Info](#authors-info)

## Description
This is a platform where students can get authentic and verified information/inspiration/advice about the tech space. The information will be in the form of videos, audio, or articles/blogs.


[Go Back to the top](#software-development-students-motivation-app)


## User Stories

Admin Can :-

* Add a user
* Flag or remove posted content that violates the rules and guidelines.
* Approve content that can be published publicly on the platform.
* Deactivate a user.
* Create categories for content

Staff can :-

* Create a profile
* Create categories for content - DevOPs,Fullstack,Front-End
* Approve content that can be published publicly on the platform.
* Flag published content that violates the rules and guidelines.
* Post content
* Edit content details

Student can :-

* Create a profile
* Subscribe to categories that interest me
* Customize my interests at my pleasure.
* Post content 
* Read/view/listen to content 
* Comment on a post or start a thread on a comment -  much like how Reddit works.
* Add content to my wishlist
* Share/recommend videos
* Get customized recommendations depending on my preference indicated in my profile.
* Get notifications whenever new content is posted to my subscribed categories.
* View other users’ remarks, comments, comments on comments/all chained comments.



[Go Back to the top](#software-development-students-motivation-app)

Software Development Students motivation app Registration

![Registration](./app/static/images/register.png)

Software Development Students motivation app Login

![Login](./app/static/images/login.png)


Software Development Students motivation app Home Module

![Software Development Students motivation app](./app/static/images/home.png)

Why Software Development Students motivation app

![Software Development Students motivation app ](./app/static/images/why.png)


Our services as Software Development Students motivation app

![Software Development Students motivation app](./app/static/images/service.png)





## Behaviour Driven Development
| Behaviour | Input | Output |
| ---------------- | --------------- | ------------------ |
| Application starts | **On page load** | Login page for user to login |
| Registration| **Registration page** | The registration page has a register form for new users  to register to the application and are redirected to login.Depending on the user type after login users are directed to different views including the  |
| View Details | **View Details click** | `Views Details`button upon clicking this button an can be able to view more details about the machinery and even find an option to update or remove the machinery, and also see the orders that have been made  |
| View Description | **View Description button** | Upon click of `View description button` the user can be able to see the more details about the machinery or she wants to hire, e.g the pay-rate, a small description|
| Profile Icon | **Profile Icon click** | User gets option to view profile, update profile and logout.On view profile user can view and also edit his or her own profile.The logout button ends the users session|
| Forms | **Form filling** | User gets to fill in various forms, and depending on various tasks the form are meant for, upon submission the act is done e.g hiring form which is meant for user to fill in the details and submit the order.|


## Installation Requirements

### Prerequisites

- Django
- Pip & Python
- cloudinary 
- Postgres Database
- Gunicorn
- Angular

## Instructions
   
##### Clone Repository:  
Interface

```bash 
https://github.com/tori-bot/Motivation-app.git

```

Backend Logic
```bash
https://github.com/JosephatNgugi/Motivation-App-Frontend.git
```

##### Install and activate Virtual Environment virtual  

```bash 
cd <projectname> && python3 -m venv virtual && source virtual/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate

 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py runserver 

 or
 ./manage.py runserver
```
##### Test Application
  Run the application

[Go Back to the top](#software-development-students-motivation-app)


## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Angular](https://img.shields.io/badge/angular-%23DD0031.svg?style=for-the-badge&logo=angular&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE)

## Live Site

#### /



## Author's Info

 :email: [Reuben Kipkemboi](https://gmail.com) 

 :email: [Victoria Makena](https://gmail.com) 

 :email: [Sandra Dindi](https://gmail.com)

 :email: [Ivy Kabere](https://gmail.com) 

 :email: [Josephat Muriu](https://gmail.com)

<p align = "center">
    &copy; 2022 @SDSM Team.
</p>
