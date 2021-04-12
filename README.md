# Django3 User Authentification System

## Implementation of Django 3 built-in user authentification system, including password reset


![Alt text](https://raw.githubusercontent.com/roldel/Django3-user-auth-system/main/django-auth.gif "a title")

This project devlopment has been made very easy by the LearnDjango team ( you can see their tutorial [here](https://learndjango.com/tutorials/django-password-reset-tutorial "LearnDjango tutorial") )

&nbsp;
&nbsp;
### Some modification I have made over tutorial code, to make it fully operational :
- SIGNUP : 
  - The default Userform was used for the Signup view. It did not include the email field. So new users could sign up, but then, not benefit from the email recovery function. I have sorted this out by creating a form from User model, specifying 'email' in the required fields. Then I have updated the views.py to manage this form and its data.  
- TEMPLATES : 
  - Templatetags include and extend changed, to add a footer and a dummy company name
  - Addition of the password recovery URL on the logged off side as well ( users had to be logged in to be displayed with the email recovery option, not so convenient when you lose your password ) 


