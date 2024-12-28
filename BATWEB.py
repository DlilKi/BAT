import streamlit as st
from PIL import Image
st.title("Streamlit")




margin_ran = 3

def margin():


    for i in range(1, (margin_ran + 1)):
      if i > 2:
            st.write(f"-----------------------------------------------------------------------------------------------")
            break

      else:
         st.write(" ")

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.title("Basic Animation & Tube")


st.write("A RecRoom Sponsored Class!")


st.title("Introduction")
margin()
head_img = Image.open("HeadTeach.jpg")
st.image(head_img, caption="Hey I am Emi formally known as Cloudx2 in RecRoom! I started playing RecRoom since July 2020, I started at the age of 26, and I always love to help those create and help them expand their creative minds! Give it your best!", width=250)



st.title("Class Information")
margin()







st.write("Invitation Link --> https://discord.gg/ayVNKFK7nb")