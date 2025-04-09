import streamlit as st
import pandas as pd

# uid_store=['user']
# pwd_store=['password']
log_df=pd.read_csv('loginpy.csv')

if "current_step" not in st.session_state:
    st.session_state.current_step = 1 
st.title('Socialgram')

def detail():
    st.title('Login')
    uid=st.text_input('user_id')
    pwd=st.text_input('password')
    
    if st.button("Login"):
    
        try:
            
            if (log_df.index[log_df['id']==uid]) == (log_df.index[log_df['pass']==pwd]):
                st.session_state.current_step = 2
            elif (uid not in log_df['id']) or ((log_df.index[log_df['pass']==pwd]) and (log_df.index[log_df['id']!=uid])):
                st.session_state.current_step = 3
            else:
                st.session_state.current_step = 3
        except ValueError as e:
            # st.warning(e)
            st.warning("user id/password wrong.\nPlease enter correct details before proceeding.")


def logged_in():
    st.title("Sucessfully logged in!!")

def log_in_failed():
    st.title("User not Found")
    if st.button("Sign In"):
        st.session_state.current_step = 4

def register():
    # for id in 
    st.title('Sign In')
    uid_r=st.text_input('user_id')
    pwd_r=st.text_input('password')
    # Load the existing CSV file
    # if uid_r. and pwd_r

    # New row as a dictionary
    new_row = {"id": uid_r, "pass": pwd_r}
    log_df = pd.read_csv("loginpy.csv")

    # Append new row
    log_df = pd.concat([log_df,pd.DataFrame([new_row])],ignore_index=True)

    if st.button("proceed"):
        log_df.to_csv("loginpy.csv",index=False)
        st.session_state.current_step =1
        
if st.session_state.current_step == 1:
    detail()
elif st.session_state.current_step == 2:
    logged_in()
elif st.session_state.current_step == 3:
    log_in_failed()
elif st.session_state.current_step == 4:
    register()
