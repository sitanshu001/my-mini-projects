import streamlit as st
import re
import os

cur_folder = os.getcwd()
text_folder_path = os.path.join(cur_folder,"text_files")
text_files_list = os.listdir(text_folder_path)
text_files_tuple = ("",)+tuple(text_files_list)

data_science_folder_path = os.path.join(text_folder_path,"Data Science")
data_science_list = os.listdir(data_science_folder_path)
data_science_tuple=("",)+tuple(data_science_list)

web_dev_folder_path = os.path.join(text_folder_path,"Devlopment Website")
web_dev_list = os.listdir(web_dev_folder_path)
web_dev_tuple=("",)+tuple(web_dev_list)

other_folder_path = os.path.join(text_folder_path,"other folders")
other_folder_list = os.listdir(other_folder_path)
other_folder_tuple=("",)+tuple(other_folder_list)

ltr = ""
fnl = ""
final_letter = ""
targets = None
save = ""
unique_targets = []
ans = []
use_this_file=""

st.title("Any Passage/Text Editor")
st.text("(Helpfull For Cover Letter/application Editing)")

st.sidebar.subheader("Instruction")
st.sidebar.markdown("""
                    - The variable portion should be inside square brackets '[' & ']' to edit those portion.
                    - """)
st.markdown("---")
st.sidebar.markdown("---")

auto_manual=st.selectbox("auto/manual",("","upload pre-existing file","enter manually"))

if(auto_manual == "enter manually"):
    st.header("Insert Your Basic Text")
    ltr = st .text_area("Enter text (for a blank line enter 2 times to save the text enter ctrl + enter)")

elif(auto_manual  == "upload pre-existing file"):
    field = st.selectbox("field :",text_files_tuple)

    for i in text_files_tuple:
        if i != "":
            st.checkbox(i)
            use_this_file = i
            allowed_to_use_this_file = st.button("open")
        if allowed_to_use_this_file:
            with open(f"{use_this_file}","r") as sfile:
                sfile.write(use_this_file)

            if field == "Webdev":
                to_be_active_file = st.selectbox("Webdev Formats :",web_dev_tuple)

            elif field == "Data Science":
                to_be_active_file = st.selectbox("Data Science Format :",data_science_tuple)
            elif field == "text_files":
                to_be_active_file = st.selectbox("other text files: ",other_folder_tuple)

ltr = ltr.replace("*","")
ltr = ltr.replace("\\","")
fnl = ltr.replace("[","")
fnl = fnl.replace("]","")
targets = re.findall(r'\[(.*?)\]',ltr)

for target in targets:
    if target not in unique_targets:
        unique_targets.append(target)

for i in range(len(unique_targets)):
    ans.append(st.text_input(unique_targets[i]))
    fnl=fnl.replace(unique_targets[i],ans[i])
st.markdown("---")

wana_print = st.sidebar.checkbox("wana print?")

if (wana_print):
    st.header("Updated Text")
    st.subheader("Here is your Updated Text!!")
    st.write(fnl)

save = st.sidebar.checkbox("Do You want to save this file")
st.sidebar.markdown("---")
if (save): 
    field = st.selectbox("field :",("","Web Dev","Data Science","other_files"))
    if field == "Web Dev":
        select_to_save = st.selectbox("Webdev Formats :",web_dev_tuple)
    elif field == "Data Science":
        select_to_save = st.selectbox("Data Science Format :",data_science_tuple)
    elif field == "text_files":
        select_to_save = st.selectbox("other text files: ",other_folder_tuple)
            
    file_count=len(text_files_list)
    filename="sample_"+str(file_count)
    with open(f"{text_folder_path}//{filename}.txt", "w") as file:
        file.write(fnl)

st.sidebar.subheader("Upcoming Targeted Updates")
st.sidebar.markdown("""
                    - Response
                    - Clean Ui
                    - Extra features:
                        - save to a location
                    """)
