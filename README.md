<a href="https://i.ibb.co/j3Hsqrp/logo.png">
    <img src="https://i.ibb.co/j3Hsqrp/logo.png" align="right" height="200"/>
</a>









# Inventory Management System by Eurymedons


## Basic Info <img src="https://raw.githubusercontent.com/aemmadi/aemmadi/master/wave.gif" width="30px">
A well designed management system(browser based web application) for eliminating time consuming physical management systems/methods, error-prone manual record keeping and physical reporting methods.

This project is based on python with  various user-friendly features which are completely customizable and editable in the long run.

A preview is shown below
![Image Preview](https://github.com/codesbyN/Inventory-image-Eurymedon/blob/master/SS1.png "Image Preview")
### Features - :eyes: 
  * Frameworks -
  
       Django framework, Dango Rest, Bootstrap
  * User friendly UI created with Bootstrap 
  * Various database in different sections
  * Admin panel created with Django
  * Customizable user login system with  editable user profiles
  * Contact page for easier help and feedbacks 
## Functional features - :handshake:
  * Dashboard/Charts for visualization of the data 
  * Admin panel customizable and different access level
  * Encryption feature in lieu of barcode system for better and safe transfer of data in the check in/out system. Also it can be used with various other features, hence improving its flexibility. Also it reduces the disadvantages in case of security of barcode systems.
  * Specific ID system for employees and different items, equipped with the encryption feature
  * Categories for different types of items stored. Each item has its own profile and can be viewed for more details. More categories can be added as per requirements if needed
  * Record/History feature for different kinds of items 
  * Record keeping of users and filter feature for easy and fast searches
  * Pdf download option of records to be used as hard copy.
  * Navigation tutorial section for easy use.
  * Only selected admins or superusers are permitted for full acccess of the inventory. Only superusers/selected admins can give users specific permissions and other customzatios from the admin panel.
  * A user friendly chatbot for easy maintanence and help of the system
  
  
# Installation - 
The `requirements.txt` file contains all the required libraries to be installed.

Use `pip install -r requirements.txt` to install the required dependencies(Or pip3).

python to be more than 3.0.0 and django –version 3.1.1. Also bootstrap 4.1,4.0

Extra apps needed are -
  * Pillow 
  * WeasyPrint
  * Crispy_forms
  * Widget tweaks
  * chart js
  * gtk for windows

 Use `pip install libname` to install the apps.
 
 Steps after extracting the zip file - 
  * Go to the project folder and start the environment with conda or venv.
  * Run `python manage.py collecstatic`
  * Run `python manage.py makemigrations` -> `python manage.py sqlmigrate appname migration_number` -> `python manage.py migrate`
  * Finally run `python manage.py runserver` to run the site on your localhost on port 8000.
  * use `python manage.py createsuperuser` to create a super user and then login to the admin panel and enjoy the databases.
  
  ## Issues to be solved - :hourglass:
 * The chatbot is still an incomplete feature. Also as this is a prototype it has few errors to be solved but it perfectly shows the features and the main aim of of the project we built.
 * Since we had only one month and we have only made a prototype with a basic template, everything in the website can be improved with given time and made better.

# Technologies used
![JavaScript](https://img.shields.io/badge/-JavaScript-black?style=flat-square&logo=javascript)
![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Bootstrap](https://img.shields.io/badge/-Bootstrap-563D7C?style=flat-square&logo=bootstrap)
![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=flat-square&logo=elasticsearch)
![Git](https://img.shields.io/badge/-Git-black?style=flat-square&logo=git)
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3)
![Heroku](https://img.shields.io/badge/-Heroku-430098?style=round&logo=heroku) 
![django](https://img.shields.io/badge/-django-450098?style=round&logo=django)  
  

  ### Site is hosted on [Eurymedon Inventory](http://eurymedon-inventory.herokuapp.com)
  **To login to the admin and view the models go to**
  [admin login](eurymedon-inventory.herokuapp.com/admin) 
  ### login : demo
  ### Password:inventory
  
  
  # A quick Navigation and feature info
  [Charts](http://eurymedon-inventory.herokuapp.com/dashboard/) - This is where you can dyanamically view charts in different ways, these are easily customizable according to the user needs.
  
  [Encryption](http://eurymedon-inventory.herokuapp.com/encryption/encryption/) - This is the menu for the encryption system.
  
  [Categories](http://eurymedon-inventory.herokuapp.com/categories) -  This is menu for categories and product information page.
  
  [People List and Pdf](http://eurymedon-inventory.herokuapp.com/users/user-list) -  This is place where you can use our filter option and also elastisearch to find a specific product or person. This page can also show you the pdf option by which you can download any record.
  
  [The Chatbot](http://eurymedon-inventory.herokuapp.com/thechatbot/thechatbot) -  GET/POST/PUT/DELETE for Questionaires - Use for listing questionaires
  
  [Chat list](http://eurymedon-inventory.herokuapp.com/chat/thechatbotchat/) - GET/POST/PUT/DELETE for Chat history of User
  
  [Chat instance](http://eurymedon-inventory.herokuapp.com/chat/thechatbotchat/chatbot/) - Uploading json file of dialog tree
  
