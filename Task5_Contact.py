import streamlit as st
import pandas as pd

if 'contacts' not in st.session_state:
    st.session_state.contacts = pd.DataFrame(columns=['Name','Phonenumber','email','address'])
st.title("📗Contact Book📖")

# Get The Values From The user
with st.form('Add-contact'):
    st.header('Add New Contact📙')
    Name = st.text_input('Enter Your Name')
    Phonenumber = st.text_input('Enter Your Phone Number')
    email = st.text_input('Enter Your Email')
    address = st.text_area('Enter Your Address')
    submit = st.form_submit_button("Add Contact")
    
    if submit:
        if Name and Phonenumber and email and address:
            new_add = pd.DataFrame([[Name,Phonenumber,email,address]],columns=['Name','Phonenumber','email','address'])
            st.session_state.contacts = pd.concat([st.session_state.contacts,new_add],ignore_index=True)
            st.success("Contact Add successfully")
        else:
            st.error("Please Fill all details")
            
            
#view saved contacts
st.header("View Contact")
st.dataframe(st.session_state.contacts)

#EDIT AND DEL
if 'edit_contact' not in st.session_state:
    st.session_state.edit_contact = None
    
    
if 'Del_contact' not in st.session_state:
    st.session_state.Del_contact = None
    

for index, row in st.session_state.contacts.iterrows():
    cols = st.columns((4, 2, 2, 2, 1, 1))
    name = cols[0].text_input('Name', value=row["Name"], key=f"Name{index}", on_change=None)
    Phonenumber = cols[1].text_input('Phonenumber', value=row["Phonenumber"], key=f"Phonenumber{index}", on_change=None)
    email = cols[2].text_input('email', value=row["email"], key=f"email{index}", on_change=None)
    address = cols[3].text_input('address', value=row["address"], key=f"address{index}", on_change=None)
    
    if cols[4].button("Save contact ", key=f"save{index}"):
        st.session_state.contacts.at[index, 'Name'] = name
        st.session_state.contacts.at[index, 'Phonenumber'] = Phonenumber
        st.session_state.contacts.at[index, 'email'] = email
        st.session_state.contacts.at[index, 'address'] = address
        st.success("Contact updated successfully!")   

    if cols[5].button("Delete contact", key=f"delete{index}"):
        st.session_state.contacts.drop(index, inplace=True)
        st.session_state.contacts.reset_index(drop=True, inplace=True)
        st.experimental_rerun()
        st.success("Contact deleted successfully!")
        

    
#view saved contacts
st.header("Edit View Contact")
st.dataframe(st.session_state.contacts)