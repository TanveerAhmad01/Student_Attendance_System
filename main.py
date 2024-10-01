

print("1 - Add new User")
print("2 - Mark Attendance")

user = int(input("Enter your Choice: "))
if user == 1:
    name = input("Enter User Name: ")
    roll = input("Enter User Roll No: ")
    year = input("Enter User Starting Year: ")
    Major = input("Enter User Deparment: ")
    pic = input("Enter the path of the image (e.g., E:\\TanveerAhmad\\Student_Attendance_System\\imagesData\\1.jpeg): ")

    from encodeGenerator import AddUser
    db_instance = AddUser(name, roll, year,Major)
    db_instance.AddUserData(pic) 
    
    from fireBase import Database
    db = Database()
    db.get_user()

elif user == 2:
    from Opencamera import Camera
    Camera.run() 
elif user == 3:
    pass