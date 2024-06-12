# A mental health chatbot- powered by Django & machine learning


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
![image](https://github.com/ujjwal197629/mental-health-chatbot-using-django-and-machine-learning/assets/129583515/58088dca-4c62-4667-8a26-cde005178225)


![image](https://github.com/ujjwal197629/mental-health-chatbot-using-django-and-machine-learning/assets/129583515/b86b43e6-d119-4b5d-abee-9776b1ff9b67)


![image](https://github.com/ujjwal197629/mental-health-chatbot-using-django-and-machine-learning/assets/129583515/c8f6840c-8cfb-45e7-ad0b-64c2fe0c2e06)


![image](https://github.com/ujjwal197629/mental-health-chatbot-using-django-and-machine-learning/assets/129583515/50d5478b-90ab-4828-b472-19ba5f327e47)



