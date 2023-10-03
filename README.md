
# Real-Time Face Recognition and Attendance System

The primary objective of this project is to develop a Real-Time Face Recognition and Attendance System that can efficiently recognize individuals using their faces in real-time video feeds from a webcam. The system aims to streamline attendance management by automating the process, eliminating the need for manual attendance tracking, and reducing the potential for errors.




## Setup Virtual Environment

Installing virtualenv

```bash
  pip install virtualenv # On Mac, pip3 install virtualenv 
```
Test your installation:

```bash
  virtualenv --version
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/harshraj6982/Face-Recognition-and-Attendance-System
```

Go to the project directory

```bash
  cd Face-Recognition-and-Attendance-System
```
Create a User Faces Directory

```bash
  mkdir user_faces
```
- Note: Add User Faces in user_faces directory in order to train and Recognize Face from Live Feed.

Create Virtual Environment

```bash
  virtualenv venv_name
```

Activate Virtual Environment

```bash
  source venv_name\Scripts\activate  # On Mac, use "source venv_name/bin/activate"
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start Execution

```bash
  python attendence.py
```

After Termination Of Program, Deactivate the Virtual Environment 

```bash
  deactivate
```