# Emergency-Triggered Microloan App

A mobile application that enables users to request **emergency microloans** with **voice verification** and **location tracking**.

- **Frontend:** MIT App Inventor (`.aia` project)  
- **Backend:** Python Flask + Firebase Realtime Database  

---

## Features
- User registration and login  
- Emergency loan requests with simulated consent and voice verification  
- Location capture for emergency requests  
- Real-time loan status checking  

---

## Installation

### Backend
- Clone the repository:  
  `git clone https://github.com/thanseera172/Emergix-App.git
  `cd Emergix-App 
- Install dependencies:  
  `pip install flask flask-cors firebase-admin`  
- Add your Firebase service account key as `serviceAccountKey.json`  
- Run the server:  
  `python app.py`  
- Backend runs at `http://localhost:5000`  

### Frontend
- Open [MIT App Inventor](https://appinventor.mit.edu)  
- Import the `.aia` file: **Projects → Import project (.aia) from my computer**  
- Connect the Web components to the backend API URLs  

---

## Usage
- Launch the app on an Android device or emulator  
- Register or log in  
- Request an emergency microloan with voice verification and location consent  
- Check the status of your loan in real-time  

---

## License
This project is licensed under the **MIT License**
