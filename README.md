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
This is a platform where students can get authentic and verified information/inspiration/advice about the tech space. The information will be in the form of images, text and articles/blogs.


[Go Back to the top](#software-development-students-motivation-app)

## Admin Login Credentials 🔑

```json
{
  "username": "",
  "password": ""
}
```
## User Stories

Admin Can :-

* Flag or remove posted content that violates the rules and guidelines.
* Deactivate a user.
* Create categories for content

Staff can :-

* Create a profile
* Create categories for content - DevOPs,Fullstack,Front-End
* Flag published content that violates the rules and guidelines.
* Post content
* Edit content details

Student can :-

* Create a profile
* Subscribe to categories that interest me
* Customize my interests at my pleasure.
* Post content 
* Read/view/listen to content 
* Comment on a post or start a thread on a comment.
* Add content to my wishlist
* Get notifications whenever new content is posted to my subscribed categories.
* View other users’ remarks, comments, comments on comments/all chained comments.


## Behaviour Driven Development
| Behaviour | Input | Output |
| ---------------- | --------------- | ------------------ |
| Application starts | **On page load** | Home page and a `signup button` for user to login |
| Registration| **Registration page** | The registration page has a register form for new users  to register to the application and are redirected to login.Depending on the user type after login users are directed to different views including the .A user can register as a `staff` or a `student`.The Administrator is just allowed to login.A `student user` uses an email with `@student` while for `staff users` their email format includes `@staff` |
| View Details | **View Details click** | `Views Details`button upon clicking this button an can be able to view more details about posts |

| Forms | **Form filling** | User gets to fill in various forms, and depending on various tasks the form are meant for, upon submission the act is done e.g making a post, updating the post details|

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

## Live Sites

#### https://josephatngugi.github.io/Motivation-App-Frontend

#### https://software-dev-motivation.herokuapp.com/ 



## Author's Info

 :email: [Reuben Kipkemboi](https://gmail.com) 

 :email: [Victoria Makena](https://gmail.com) 

 :email: [Sandra Dindi](https://gmail.com)

 :email: [Ivy Kabere](https://gmail.com) 

 :email: [Josephat Muriu](https://gmail.com)

<p align = "center">
    &copy; 2022 @SDSM Team.
</p>
