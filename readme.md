# Secure Data Store
A platform to store your data securely with encryption and decryption on the client side.

## Table of Contents
* [About](#about)
* [Features](#features)
* [How to use](#how-to-use)
* [Tech Stack](#tech-stack)
* [Setup Locally](#setup-locally)
* [Contributing](#contributing)

## About
Secure Data Store is a web application that allows users to store their data securely. The data is encrypted on the client side using the Fernet symmetric encryption algorithm and the encrypted data is stored on the server. The data can only be decrypted by the user who uploaded it using their passkey.

## Features
*   User authentication using a username and password.
*   Store data securely using Fernet symmetric encryption algorithm.
*   Retrieve stored data using the passkey provided during upload.
*   User can view all the data they have uploaded.
*   User can delete the data they have uploaded.

## How to use
1.  Go to the [Secure Data Store website](https://secure-data-store.herokuapp.com/).
2.  Click on the "Create Account" button.
3.  Fill in the required details and click on the "Register Now" button.
4.  Click on the "Login" button.
5.  Fill in the required details and click on the "Login Now" button.
6.  Click on the "Add New Data" button.
7.  Fill in the required details and click on the "Submit" button.
8.  Click on the "View Data" button to view all the data you have uploaded.
9.  Click on the "Delete Data" button to delete the data you have uploaded.

## Screenshots
![Login Page](screenshots/login.png)
![Home Page](screenshots/home.png)
![Add Data Page](screenshots/add-data.png)
![View Data Page](screenshots/view-data.png)

## Tech Stack
*   Frontend, Backend: Streamlit
*   Backend: Flask
*   Database: JSON files
*   Encryption: Fernet symmetric encryption algorithm

## Setup Locally
1.  Clone the repository using the command `git clone https://github.com/sarfarazansari/secure-data-store.git`.
2.  Install the required packages using the command `pip install -r requirements.txt`.
3.  Run the app using the command `streamlit run app.py`.
4.  Open a web browser and go to `http://localhost:8501/`.

## Contributing
Contributions are welcome. If you want to contribute, please follow these steps:
1.  Fork the repository.
2.  Make the changes you want.
3.  Commit the changes.
4.  Push the changes to your forked repository.
5.  Open a pull request.

