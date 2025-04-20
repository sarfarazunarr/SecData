import streamlit as st
from utils import register_user, login_user, load_data, save_data, load_info

if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "is_loggedin" not in st.session_state:
    st.session_state["is_loggedin"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "menus" not in st.session_state:
    st.session_state["menus"] = ["Create Account", "Login"]
    
menu_items = st.session_state["menus"]

st.set_page_config(page_title="Secure Data Store")

with st.sidebar:
    menu_item = st.radio(label="Menu bar", label_visibility="hidden", options=menu_items)
    st.session_state["page"] = menu_item
    

if st.session_state["page"] == "Home" and st.session_state["is_loggedin"]:
    st.text(f"Hi {st.session_state["username"]},")
    st.title("Welcome to SecData!")
    st.text("Platform that keeps you messages and data encrypted!")
    
    @st.dialog("Add New Data") 
    def add_data():
        with st.form(key="add_data_form", clear_on_submit=True):
            label = st.text_input("Label")
            message = st.text_area("Message")
            passkey = st.text_input("Passkey", type="password")
            
            if st.form_submit_button("Submit"):
                save_data(st.session_state["username"], message, passkey, label)
                st.success("Data added successfully!")
                st.rerun()
    if st.button("Add New Data"):
        add_data()
        
    data_labels = load_data(st.session_state["username"])
    if data_labels == []:
        st.text("No data found! Create a new one")
    if len(data_labels) > 0:
        label = st.selectbox("Select a label", data_labels)
        passkey = st.text_input("Enter passkey: ")
        if st.button("View Data"):
            data = load_info(label, st.session_state["username"], passkey)
            @st.dialog("Your Data")
            def show_data(data):
                st.write("Label: ", label)
                st.write(f"**Message**: {data}")
            
            if data["type"] == "error":
                st.error(f"{data['message']}")
            elif data["type"] == "success":
                show_data(data["message"])
           
elif st.session_state["page"] == "Login":
    st.title("Login Now!")
    st.text("Login to your account and enter your secure world!")
    
    with st.form(key="login"):
        l_username = st.text_input("Username")
        l_password = st.text_input("Password", type="password")
        
        if st.form_submit_button("Login Now"):
            l_data = login_user(l_username, l_password)
            if l_data["type"] == "error":
                st.error(f"{l_data["message"]}")
            elif l_data["type"] == "Success":
                st.session_state["is_loggedin"] = True
                st.session_state["username"] = l_username
                st.session_state["menus"] = ["Home", "Logout"]
                st.success(f"{l_data['message']}")
                st.rerun()

 
elif st.session_state["page"] == "Create Account":
    st.title("Register Now!")
    st.text("Get into SecData and be part of the secure world!")
    
    with st.form(key="register"):
        r_name = st.text_input("Name")
        r_username = st.text_input("Username")
        r_password = st.text_input("Password", type="password")
        if st.form_submit_button("Register Now"):
            data = register_user(r_name, r_username, r_password)
            if data["type"] == "error":
                st.error(f"{data["message"]}")
            elif data["type"] == "Success":
                st.success(f"{data['message']}")

elif st.session_state["page"] == "Logout":
    st.session_state["is_loggedin"] = False
    st.session_state["username"] = ""
    st.session_state["menus"] = ["Create Account", "Login"]
    st.session_state["page"] = "Login"
    st.rerun()
        