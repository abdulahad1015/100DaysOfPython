#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os

from dotenv import load_dotenv
load_dotenv()


# os.environ['MY_ENV_VAR']="123456789"
MY_ENV_VAR=os.getenv('MY_ENV_VAR')
print(MY_ENV_VAR)
