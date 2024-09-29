import firebase_admin
from firebase_admin import credentials, db
import numpy as np
class Database:
    def __init__(self):
        self.db_reference = 'self.connect_to_database'
        if not firebase_admin._apps:
            cred = credentials.Certificate("studentattendancesystem-d2223-firebase-adminsdk-f59pw-965975fee4.json")
            firebase_admin.initialize_app(cred, {
                "databaseURL": "https://studentattendancesystem-d2223-default-rtdb.firebaseio.com"
            })


    def get_user(self):
        ref = db.reference()  
        data = ref.get()  
        return data
      
    
    def add_user(self,user_data):
        ref = db.reference()
        new_user_ref = ref.push(user_data)
        print("Data added successfully:")




