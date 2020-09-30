# Inventory Management System by Eurymedons

### Basic Info - 
A well designed management system(browser based web application) for eliminating time consuming physical management systems/methods, error-prone manual record keeping and physical reporting methods.

This project is based on python with  various user-friendly features which are completely customizable and editable in the long run.

A preview is shown below

![Image Preiew](https://github.com/codesbyN/Inventory-image-Eurymedon/blob/master/SScollage.png "Image Preview")
### Features -
  * Frameworks -
  
       Django framework, Dango Rest, Bootstrap
  * User friendly UI created with Bootstrap 
  * Various database in different sections
  * Admin panel created with Django
  * Customizable user login system with  editable user profiles
  * Contact page for easier help and feedbacks 
### Functional features -
  * Dashboard/Charts for visualization of the data 
  * Admin panel customizable and different access level
  * Encryption feature in lieu of barcode system for better and safe transfer of data in the check in/out system. Also it can be used with various other features, hence improving its flexibility
  * Specific ID system for employees and different items, equipped with the encryption feature
  * Categories for different types of items stored. Each item has its own profile and can be viewed for more details. More categories can be added as per requirements if needed
  * Record/History feature for different kinds of items 
  * Record keeping of users and filter feature for easy and fast searches
  * Pdf download option of records to be used as hard copy.
  * Navigation tutorial section for easy use.
  * Only selected admins or superusers are permitted for full acccess of the inventory. Only superusers/selected admins can give users specific permissions and other customzatios from the admin panel.
  * A user friendly chatbot for easy maintanence and help of the system
### Installation - 
The `requirements.txt` file contains all the required libraries to be installed.

Use `pip install -r requirements.txt` to install the required dependencies(Or pip3).

python to be more than 3.0.0 and django –version 3.1.1. Also bootstrap 4.1,4.0

Extra apps needed are -
  * Pillow 
  * WeasyPrint
  * Crispy_forms
  * Widget tweaks
  * chart js

 Use `pip install libname` to install the apps.
 
 Steps after extracting the zip file - 
  * Go to the project folder and start the environment with conda or venv.
  * Run `python manage.py collecstatic`
  * Run `python manage.py makemigrations` -> `python manage.py sqlmigrate appname migration_number` -> `python manage.py migrate`
  * Finally run `python manage.py runserver` to run the site on your localhost on port 8000.
  * use `python manage.py createsuperuser` to create a super user and then login to the admin panel and enjoy the databases.
  
  ### Site is hosted on eurymedon-inventory.herokuapp.com
  
