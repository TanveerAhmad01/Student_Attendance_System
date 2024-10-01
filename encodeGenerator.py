import cv2
import face_recognition
from fireBase import Database
from firebase_admin import storage
import base64
class AddUser:
    def __init__(self, name, Roll_No, Year,Major):
        self.height = 500
        self.width = 500
        self.name = name
        self.Roll_No = Roll_No
        self.Year = Year
        self.Major = Major
        self.list = []
        self.base64 = ''
    def AddUserData(self, path):

        image_path = path
        image = cv2.imread(image_path)
        resize = cv2.resize(image, (self.height, self.width))
        x = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB) 
        face_encodings = face_recognition.face_encodings(x)
        _, buffer = cv2.imencode('.jpg', image)
        self.base64 = base64.b64encode(buffer).decode('utf-8')
        if face_encodings:
            self.list.append(face_encodings[0].tolist()) 
        else:
            print(f"No face found in {path}. Skipping.")

        
        user_data = {
            'name': self.name,
            'Roll No': self.Roll_No,
            'Year': self.Year,
            "Major": self.Major,
            'attendance': 0,
            'faceEncodings': self.list,
            "base64":self.base64
        }
        
       
        db_instance =Database()
        db_instance.add_user(user_data)




