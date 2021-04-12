# Django3 User Authentification System

## Implementation of Django 3 built-in user authentification system, including password reset


![Alt text](https://raw.githubusercontent.com/roldel/Django3-user-auth-system/main/django-auth.gif "a title")

This project devlopment, has been made very easy by the LearnDjango team ( you can see their tutorial [here](https://learndjango.com/tutorials/django-password-reset-tutorial "LearnDjango tutorial") )

&nbsp;
&nbsp;
### Some modification I have made over tutorial code, to make it fully operational :
- SIGNUP : 
  - The default Userform was used for the Signup view. It did not include the email field. So new users could sign up, but then, not benefit from the email recovery function. I have sorted this out by creating a form from User model, specifying 'email' in the required fields. Then I have updated the views.py to manage this form and its data.  
- TEMPLATES : 
  - Templatetags include and extend changed, to add a footer and a dummy company name
  - Addition of the password recovery URL on the logged off side as well ( users had to be logged in to be displayed with the email recovery option, not so convenient when you lose your password ) 


&nbsp;
&nbsp;
## How to make it work ? 🚀

### Setup your django environment
I have included the Dockerfile and docker-compose.yml in the repo. If you want to know more, about how to set up docker with django, feel free to have a look [here](https://github.com/roldel/Docker-For-Django-Starter-Files). Docker is just an option though, other environment with django3 will work as well

### Set up the project
Clone the project locally
In the config.settings.py file, update the SECRET_KEY value to your dev or production key.
You can then perform the initial DB migration. It is required, as we will be using the User built-in model (from django.contrib.auth.models)
```{bash}
python manage.py migrate 
```
Your project is now already good to go, You can start your development server and give a try at your auth system.

### Email setup ✉️
In this project, django will only save the password reset emails, in a "sent_emails" directory, in the project root. It will not send them.
To make it operational, you will need an SMTP server, from a provider. Gmail can be an easy one to start with.

Then in config.settings.py :
replace :
```{bash}
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))
```
with  :
```{bash}
EMAIL_BACKEND = ‘django.core.mail.backends.smtp.EmailBackend’
EMAIL_HOST = ‘smtp.gmail.com’
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = ‘your_account@gmail.com’
EMAIL_HOST_PASSWORD = ‘your account’s password’
```

For your gmail SMTP to process the emails, make sure you allow "Less secure apps" in your associated google account settings. Also you might have to clear the security warnings that might arise, as you start to use the service (gmail will send you an email) 




