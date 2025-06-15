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

# auto = st.checkbox("upload file")
auto_manual=st.selectbox("auto/manual",("","upload pre-existing file","enter manually"))
# "enter text/upload file",("","manual","upload files")
# st.text("<--------- Check sidebar")
# while manual == True:
#     auto = False
    # while auto == True:
    #     manual = False
# while auto == True:
#     manual = False
    # while manual == True:
    #     auto == False
if(auto_manual == "enter manually"):
    st.header("Insert Your Basic Text")
    ltr = st .text_area("Enter text (for a blank line enter 2 times to save the text enter ctrl + enter)")

elif(auto_manual  == "upload pre-existing file"):
    field = st.selectbox("field :",text_files_tuple)

    for i in text_files_tuple:
        # # st.selectbox("hi",("ye","oh yesh"))
        if i != "":
        #     st.selectbox(f"{field} formats",text_files_tuple[i])
            st.checkbox(i)
            use_this_file = i
            allowed_to_use_this_file = st.button("open")
        if allowed_to_use_this_file:
            with open(f"{use_this_file}","r") as sfile:
                sfile.write(use_this_file)

            if field == "Webdev":
                to_be_active_file = st.selectbox("Webdev Formats :",web_dev_tuple)
                # for i in web_dev_tuple:
                #     if i!="":
                #         st.selectbox("Web dev")
            elif field == "Data Science":
                to_be_active_file = st.selectbox("Data Science Format :",data_science_tuple)
            elif field == "text_files":
                to_be_active_file = st.selectbox("other text files: ",other_folder_tuple)

ltr = ltr.replace("*","")
ltr = ltr.replace("\\","")
fnl = ltr.replace("[","")
fnl = fnl.replace("]","")
targets = re.findall(r'\[(.*?)\]',ltr)
# if targets:
    # st.write(targets)
for target in targets:
    if target not in unique_targets:
        unique_targets.append(target)

# st.write(unique_targets,len(unique_targets))
for i in range(len(unique_targets)):
    ans.append(st.text_input(unique_targets[i]))
    # print(unique_targets[i],ans[i])
    fnl=fnl.replace(unique_targets[i],ans[i])
st.markdown("---")
# print(final_letter)
# print(f"printable or not {final_letter.isprintable()}")
wana_print = st.sidebar.checkbox("wana print?")

if (wana_print):
    st.header("Updated Text")
    st.subheader("Here is your Updated Text!!")
    st.write(fnl)

save = st.sidebar.checkbox("Do You want to save this file")
st.sidebar.markdown("---")
if (save): 
    # text_folder=os.makedirs(text_folder_path)
    
    # try:
    #     os.makedirs(text_folder)
    # except Exception as e:
    #     # st.text(e)
    #     st.write("file exists move on to save")
    field = st.selectbox("field :",("","Web Dev","Data Science","other_files"))
    if field == "Web Dev":
        select_to_save = st.selectbox("Webdev Formats :",web_dev_tuple)
    elif field == "Data Science":
        select_to_save = st.selectbox("Data Science Format :",data_science_tuple)
    elif field == "text_files":
        select_to_save = st.selectbox("other text files: ",other_folder_tuple)
    # save_loc=st.selectbox("Where you want to save?",(text_files_tuple))
    # for locs in text_files_list:
    #     if locs == "Data Science":
            
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
st.table()
# st.text("length is")
# st.text(len(unique_targets))
# print(ans)
# st.write(final_letter)
#     for change in 
#         st.selectbox("change",change,st.text_input)
#     st.write(unique_targets,len(unique_targets))4
#     st.text(len(unique_targets))

# if save =="Yes":
#     file_path = "letter_"+"1"+".txt"
#     with open(file_path,"w") as file:
#         file.write(final_letter)
# st.write(fnl)


# print("============ END ============")


copy = """ 
**\[Your Name]**

\[Your Address]

\[City, State, Zip Code]

\[Email Address] | \[Phone Number] | \[LinkedIn or GitHub, if relevant]

**\[Date]**

 

**\[Hiring Manager’s Name]**

\[Company Name]

\[Company Address]

\[City, State, Zip Code]

**Dear \[Hiring Manager's Name],**

I am writing to express my interest in the Python Developer position at \[Company Name], as advertised on \[Job Board/Company Website]. With a strong background in Python programming and hands-on experience in backend development, data processing, and automation, I am excited about the opportunity to contribute to your development team.

Over the past \[X years], I have worked on a variety of Python-based projects, including \[mention a project, e.g., “developing RESTful APIs with Flask” or “automating data pipelines using Pandas and SQL”]. My proficiency in Python is complemented by experience with libraries and frameworks \such as \[Django, Flask, Pandas, NumPy, etc.], as well as working knowledge of Git, Docker, and relational databases like PostgreSQL or MySQL.

In my most recent role at \[Previous Company/Internship], I \[describe a key responsibility or accomplishment, e.g., “built a scalable backend service that reduced data processing time by 30%”]. I thrive in collaborative environments, enjoy problem-solving, and am always eager to learn new tools and best practices in software development.

I’m particularly drawn to \[Company Name] because of \[specific reason: e.g., "your innovative approach to cloud-native applications" or "your commitment to open-source contributions"], and I would be thrilled to be part of a team that values clean, efficient, and well-documented code.

Thank you for considering my application. I have attached my resume for your review and would welcome the opportunity to discuss how my skills and experiences align with your team’s needs. I look forward to hearing from you.

**Sincerely,**

**\[Your Name]**
"""

# st.write(ans)

# back works


# if save == "Yes":
    # import os
    # os.

# for el in ltr:
#     if el == "[":
#         print()
        




# sample lines:


# **\[Your Name]**

# \[Your Address]

# \[City, State, Zip Code]

# \[Email Address] | \[Phone Number] | \[LinkedIn or GitHub, if relevant]

# **\[Date]**