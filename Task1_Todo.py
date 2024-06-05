                # DABHI DHRUVI R
                # TO-DO_APP





import streamlit as st
import numpy as np
import pandas as pd


st.title("To-Do-List ✅")

if 'Task' not in st.session_state:
    st.session_state.Task = []

def add_task(task,status):
    st.session_state.Task.append({'Task':task,'status':status})
    
def edit_your_task(index,new_task,new_status):
    st.session_state.Task[index]['Task']= new_task
    st.session_state.Task[index]['status']= new_status
    
def delete_task(index):
    st.session_state.Task.pop(index)
    
# DATA FROM USER 
with st.form(key="Add_Task_List"):
    Task_List = st.text_area('Enter Your Task Here')
    Task_Status = st.selectbox('Status',['Not Started','In Progress','Completed'])
    submit = st.form_submit_button('Add You Task ')
    if submit and Task_List:
        add_task(Task_List,Task_Status)
        # st.success("Your Task Added Successfully")
        st.success(f"Your Task: {Task_List} and status is:   {Task_Status}")
    else:
        st.error("Plase Write A Task ") 
    
    # View Your Task
if st.session_state.Task:
    st.write(" View Your  Task List ")  
    for i ,Task in enumerate(st.session_state.Task,start=1):
        st.write(f"{i}.{Task['Task']} -> {Task['status']}")
        # if st.session_state.Task:
                # # st.write(" View Your Edit Task List ")  
                # for i ,Task in enumerate(st.session_state.Task,start=1):
                #     st.write(f"{i}.{Task['Task']} -> {Task['status']}")
    task_num = st.number_input('Task Number',min_value=1,max_value=len(st.session_state.Task),step=1,key='task_num')
    with st.form(key="edit_task_form"):
        edit_text = st.text_input('Edit TASK',key="edit_task_form")
        edit_task = st.selectbox('Edit Status',['Not Started','In Progress','Completed'],key='edit_text')
        edit_btn = st.form_submit_button("Edit Task📝")
        if edit_btn and edit_text:
            edit_your_task(task_num-1,edit_text,edit_task)
            # st.success("Task edit successfully")
            st.success(f"{task_num} Updated to {edit_text} 'with status' {edit_task}")
            st.experimental_rerun()  
                
                #
            # if st.session_state.Task:
            #     st.write(" View Your Edit Task List ")  
            #     for i ,Task in enumerate(st.session_state.Task,start=1):
            #         st.write(f"{i}.{Task['Task']} -> {Task['status']}")
                    
    del_btn = st.button('Delete Task ❎')
    if del_btn:
        delete_task(task_num-1)
        st.success(f"task  {task_num} deleted")
        st.experimental_rerun()