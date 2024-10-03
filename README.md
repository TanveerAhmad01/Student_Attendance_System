<h1>Student Attendance System with Face Recognition</h1>

<h3>Overview</h3>
<p>This project implements a Student Attendance System using face recognition technology. It leverages OpenCV for video capture and face detection, and integrates with Firebase for data storage and retrieval. The system provides a user-friendly dashboard to manage attendance records efficiently.</p>

<h3>Features</h3>
<p><strong>Real-time Face Recognition:</strong> Detects and recognizes faces in real-time using a webcam.</p>

<p><strong>Attendance Tracking:</strong> Automatically marks attendance for recognized students and updates the database.</p>

<p><strong>User-Friendly Dashboard:</strong> Displays student information, including name, roll number, year, and major.</p>

<p><strong>Modular Design:</strong> Easily add or modify modules for different functionalities.</p>

<p><strong>Data Storage:</strong> Utilizes Firebase for storing user data and attendance records.</p>

<h3>Adding Users</h3>
<p>The system allows you to add new users with their face data for attendance tracking. To add a user, follow these steps:</p>
<ol>
    <li>Instantiate the <strong>AddUser</strong> class with the student's details:
        <pre><code>user = AddUser(name="Student Name", Roll_No="123", Year="2024", Major="Computer Science")</code></pre>
    </li>
    <li>Call the <strong>add_user_data</strong> method with the path to the student's image:
        <pre><code>user.add_user_data("path/to/image.jpg")</code></pre>
    </li>
    <li>The user's face encodings and information will be stored in the Firebase database for future attendance tracking.</li>
</ol>
<p>Ensure that the image provided contains a clear view of the student's face for successful encoding.</p>

<h3>Prerequisites</h3>
<ul>
    <li>Python 3.x</li>
    <li>OpenCV</li>
    <li>NumPy</li>
    <li>Face Recognition</li>
    <li>Firebase Admin SDK</li>
    <li>CVZone</li>
    <li>A webcam</li>
</ul>

<h3>Installation</h3>
<ol>
    <li>Clone the repository:
        <pre><code>https://github.com/TanveerAhmad01/Student_Attendance_System.git
cd student-attendance-system</code></pre>
    </li>
    <li>Install required packages:
        <pre><code>pip install opencv-python numpy face_recognition cvzone firebase-admin</code></pre>
    </li>
    <li>Ensure you have a Firebase project set up. Follow these steps:
        <ul>
            <li>Create a Firebase project on the <a href="https://console.firebase.google.com/">Firebase Console</a>.</li>
            <li>Enable the Realtime Database.</li>
            <li>Download the Firebase Admin SDK configuration file (usually a JSON file).</li>
            <li>Place the JSON file in the project directory and modify the code to reference it.</li>
        </ul>
    </li>
</ol>

<h3>Usage</h3>
<ol>
    <li>Add student images and face encodings to the Firebase database.</li>
    <li>Update the path to your background image and student modules in the code.</li>
    <li>Run the application:
        <pre><code>python main.py</code></pre>
    </li>
    <li>Press 'q' to quit the application.</li>
</ol>

<h3>Code Explanation</h3>
<ul>
    <li><strong>Camera Class:</strong> Handles video capture, face detection, and attendance marking.</li>
    <li><strong>FetchData Method:</strong> Retrieves user data and face encodings from Firebase.</li>
    <li><strong>Run Method:</strong> Main loop for video processing, face recognition, and attendance updating.</li>
</ul>

<h3>Output Screenshots</h3>
<p>Below are some screenshots demonstrating the functionality of the Student Attendance System:</p>

<img>![Screenshot 2024-10-03 073936](https://github.com/user-attachments/assets/c2d01163-d50a-469e-97ca-31273a411a46)



<h3>Contributing</h3>
<p>Contributions are welcome! Feel free to fork the repository and submit a pull request.</p>

<h3>License</h3>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h3>Acknowledgements</h3>
<ul>
    <li><a href="https://opencv.org/">OpenCV</a></li>
    <li><a href="https://github.com/ageitgey/face_recognition">Face Recognition</a></li>
    <li><a href="https://firebase.google.com/">Firebase</a></li>
    <li><a href="https://github.com/cvzone/cvzone">CVZone</a></li>
</ul>
