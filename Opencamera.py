import cv2
import os
import numpy as np
import face_recognition 
import base64
class Camera:
    def __init__(self):
        self.openCamera = cv2.VideoCapture(0)
        self.backGroundImg = cv2.imread('modules/background.png')
        self.allModules = 'E:\\TanveerAhmad\\Student_Attendance_System\\Modules\\AllModules'
        self.allPic = os.listdir(self.allModules)
        self.bg_height, self.bg_width = 570, 950
        self.resizedBg = cv2.resize(self.backGroundImg, (self.bg_width, self.bg_height))
        self.moduleList = []
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.mode = 1
        self.face_Encodeings = []

    def FetchData(self):
        from fireBase import Database
        data = Database()
        users = data.get_user()  
        if users: 
            for key, value in users.items(): 
                 if 'faceEncodings' in value and value['faceEncodings']:
                    face_encoding = np.array(value['faceEncodings'][0])  
                    self.face_Encodeings.append((face_encoding,value['name'],value['Roll No'],value['Year'],value['attendance'],value['base64'],value['Major']))
                    
    def run(self):
        for i in self.allPic:
            self.moduleList.append(cv2.imread(os.path.join(self.allModules, i)))
        print(len(self.moduleList))
       
        while True:
            check, frame = self.openCamera.read()   
            self.resizedwebcam = cv2.resize(frame, (460, 370))
            gray_frame = cv2.cvtColor(self.resizedwebcam, cv2.COLOR_BGR2RGB)
            faces = self.face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                cv2.rectangle(self.resizedwebcam, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
            self.resizedBg[135:135+370, 50:50+460] = self.resizedwebcam
            resizeMode = cv2.resize(self.moduleList[self.mode], (325, 510))
            self.resizedBg[32:32+510, 600:600+325] = resizeMode

            curFram = face_recognition.face_locations(self.resizedwebcam)
            encodeWebcam = face_recognition.face_encodings(self.resizedwebcam,curFram)
           
            for webcam in(encodeWebcam):
                facematches = face_recognition.compare_faces([encoding[0] for encoding in self.face_Encodeings],webcam)
                # FaceDist = face_recognition.face_distance([encoding[0] for encoding in self.face_Encodeings],webcam)
                # print("Distances:", FaceDist)
                for i, match in enumerate(facematches):
                    if match == True:
                        user_info = self.face_Encodeings[i]
                        user_name = user_info[1]
                        roll_No = user_info[2]
                        Attendance = user_info[4]
                        Year = user_info[3]
                        base64_string = user_info[5]
                        Major = user_info[6]
                        print("User Info",user_name,roll_No,Attendance,Year,Major)
                        self.mode = 2

                        if self.mode == 2:
                            font_scale = 0.5
                            image_data = base64.b64decode(base64_string)
                            nparr = np.frombuffer(image_data, np.uint8)
                            decoded_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                            resized_image = cv2.resize(decoded_image, (170, 170))
                            self.resizedBg[144:144+170, 680:680+170] = resized_image

                            cv2.putText(self.resizedBg,str(Attendance), (645,100), 
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 1)

                            cv2.putText(self.resizedBg,str(roll_No), (756,398), 
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 1)

                            cv2.putText(self.resizedBg,user_name, (756,443), 
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), 1)

                            cv2.putText(self.resizedBg,Year, (843,500), 
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 1)

                            cv2.putText(self.resizedBg,Major, (680,501), 
                            cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), 1)

                        else:
                            self.mode = 1
                   
            cv2.imshow("Attendance Dashboard", self.resizedBg)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.openCamera.release()
        cv2.destroyAllWindows()

obj = Camera()
obj.FetchData()
obj.run()
