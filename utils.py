import json
import streamlit as st
from cryptography.fernet import Fernet
from backports.pbkdf2 import pbkdf2_hmac
import secrets

key = st.secrets["F_KEY"]
KEY = key.encode('utf-8')

def register_user(name, username, password):
    if not name or not username or not password:
        return {"type": "error", "message": "Fill all fields!"}
    try:
        with open("users.json", "r") as f:
            users = json.loads(f.read())
    except FileNotFoundError:
        with open('users.json', 'w') as f:
            f.write(json.dumps([]))
            return {"type": "error", "message": "Try Again, File Regenerated!"}
    except json.JSONDecodeError:
        with open('users.json', 'w') as f:
            f.write(json.dumps([]))
            return {"type": "error", "message": "Try Again, File Regenerated!"}
    if users != []:
        for user in users:
            if user["username"] == username:
                return {"type": "error", "message": "Username already exists!"}
    salt = secrets.token_bytes(16)
    hashed_pass = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000).hex()
    users.append({"name": name, "username": username, "salt": salt.hex(), "password": hashed_pass})
    with open("users.json", "w") as f:
        json.dump(users, f)
        return {"type": "Success", "message": "Registered Successfully!"}

def login_user(username, password):
    try:
        with open("users.json", "r") as f:
            users = json.loads(f.read())
            for user in users:
                if user["username"] == username:
                    salt = bytes.fromhex(user["salt"])
                    hashed_pass = pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000).hex()
                    if user["password"] == hashed_pass:
                        return {"type": "Success", "message": "Login Successful!"}
                    else:
                        return {"type": "error", "message": "Incorrect Password!"}
            return {"type": "error", "message": "User not found!"}
    except FileNotFoundError:
        with open('users.json', 'w') as f:
            f.write(json.dumps([]))
        
        return {"type": "error", "message": "Try Again, File Regenerated!"}
    except json.JSONDecodeError:
        with open('users.json', 'w') as f:
            f.write(json.dumps([]))
        return {"type": "error", "message": "Try Again, File Regenerated!"}


def save_data(username, message, passkey, label):
    try:
        with open('data.json', 'r') as f:
            messages = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        messages = []
    
    salt = secrets.token_bytes(16)
    hashed_passkey = pbkdf2_hmac("sha256", passkey.encode("utf-8"), salt, 100000).hex()
    f = Fernet(KEY)
    encrypted_message = f.encrypt(message.encode("utf-8"))
    messages.append({"username": username, "message": encrypted_message.decode("utf-8"), "passkey": hashed_passkey, "salt": salt.hex(), "label": label})
    with open("data.json", "w") as f2:
        json.dump(messages, f2)
    return True

def load_data(username):
    f = Fernet(KEY)
    try:
        with open("data.json", "r") as f:
            data = json.loads(f.read())
            user_labels = []
            for object in data:
                if object["username"] == username:
                    user_labels.append(object["label"])
            return user_labels
    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump([], f)
            return []

def load_info(label, username, passkey):
    fn = Fernet(KEY)
    try:
        with open("data.json", "r") as f:
            data = json.loads(f.read())
            if passkey == "":
                return {"type": "error", "message":"Enter Passkey"}
            for object in data:
                if object["username"] == username and object["label"] == label:
                    salt = bytes.fromhex(object["salt"])
                    hashed_passkey = pbkdf2_hmac("sha256", passkey.encode("utf-8"), salt, 100000).hex()
                    if object["passkey"] == hashed_passkey:
                        decrypted_message = fn.decrypt(object["message"].encode("utf-8"))
                        return {"type": "success", "message":decrypted_message.decode("utf-8")}
                    else:
                        return {"type": "error", "message":"Invalid Passkey"}
    except FileNotFoundError:
        with open('data.json', 'w') as f:
            json.dump([], f)
    