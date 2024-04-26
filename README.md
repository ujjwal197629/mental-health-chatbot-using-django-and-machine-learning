# General Ai mental health chatbot- powered by Django & machine learning


## How To Use This

First create a virtual environment(highly recommended)and run...

1. Run pip install -r requirements.txt to install dependencies

2. Replace this code
   SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
   in settings.py with your own secret key.
 
3. Create your own secret key with below python script  
    from django.core.management.utils import get_random_secret_key
    ; print(get_random_secret_key())

4. Set your secret key in your environment variable using this command by running command prompt as adminstrator if windows
setx DJANGO_SECRET_KEY "your_secret_key_here"

Now you can replace the step number 2 code with SECRET_KEY section in settings.py

5. Run python manage.py makemigrations

6. Run python manage.py migrate

7. Run python manage.py runserver

8. Navigate to http://127.0.0.1:8000/ in your browser



## Dataset used -

https://www.kaggle.com/code/jocelyndumlao/chatbot-for-mental-health-conversations


## Some Screenshots of This Webapp -

![image](https://github.com/ujjwal197629/Mental-Health-Chatbot/assets/129583515/98024e9e-3c89-4454-990c-751e3109d00d)



                                                  Home Page

                                                  

![image](https://github.com/ujjwal197629/Mental-Health-Chatbot/assets/129583515/fe06a19d-53ef-4a6d-a062-a31e1e9f631c)



                                                 Mobile view

                                                 

![image](https://github.com/ujjwal197629/Mental-Health-Chatbot/assets/129583515/d93572b9-ca80-41e7-b9f3-7adc26d0f947)


   
                                                  Login Page



![image](https://github.com/ujjwal197629/Mental-Health-Chatbot/assets/129583515/bf57ea29-7c15-470f-86eb-5be11222fb26)



                                           Sign up page mobile view



