
# Real-Time Face Recognition and Attendance System

The primary objective of this project is to develop a Real-Time Face Recognition and Attendance System that can efficiently recognize individuals using their faces in real-time video feeds from a webcam. The system aims to streamline attendance management by automating the process, eliminating the need for manual attendance tracking, and reducing the potential for errors.

## Install mpg123 (Not Required For MacOS Users)


**On Linux:**

1. Open a terminal window.

2. Update your package manager's list of available packages:

```bash
  sudo apt-get update
```

3. Install mpg123:

```bash
  sudo apt-get install mpg123
```

**On Windows:**

1. Download the mpg123 installer from the official website: mpg123.de: https://www.mpg123.de/download.shtml
2. Run the installer and follow the on-screen instructions.

Once mpg123 is installed, you can verify that it was installed successfully by running the following command in a terminal window:

```bash
  mpg123 --version
```
If you see the mpg123 version number displayed, then mpg123 was installed successfully.

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
- Add User Faces in user_faces directory in order to train and Recognize Face from Live Feed.
- Each file in the user_faces directory must have a unique File Name.
- Also, Only 1 image of a user must be there in user_faces directory. 
- Note: Images should be in the .jpg or .png format and file name should be the name of the Person. For Example, Image of Elon Musk should be saved as "Elon Musk.jpg"

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
  python attendance.py
```
Stop Execution

- Press q on the webcam window

View Attendance

- Open Attendance.csv file

After Termination Of Program, Deactivate the Virtual Environment 

```bash
  deactivate
```
