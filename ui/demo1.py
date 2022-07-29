# to run this , open terminal and type 
# command ctl+J
# streamlit run ui/demo1.py
# st. function which shows on screen


from xml.etree.ElementTree import Comment
import streamlit as st

#Text elements

st.title("Steamlit Demo")
st.header("Streamlit is awesome")
st.subheader("it's easy to use")
st.text("This is the simple text example")
st.write("This is magical function")
st.markdown("This is the **markdown** 'example' ")
st.success("This is success message")
st.info("This is an info message")
st.warning("This is a warning message")
st.error("This is an error message")
st.exception("This is an exception message")

# Media elements

st.image("ui/background.jpeg")
st.audio(r'D:\My Files\Python_001\Python_JUN_2022\ui\power.mp3')
st.video(r"https://youtu.be/Lcp2lrZhC6E")



# Widgets

name = st.text_input("Enter Your Userame")
cost = st.number_input("Enter the Cost")
comment = st.text_area("Enter remarks")
status = st.checkbox("save this data")
gender = st.radio("Gender",["Male","Female","Others"])
quarylist = ['How to use streamlit ?',
            'Is strealit free or paid ?',
            'Is gonna rain now']
quary = st.selectbox("what the quary", quarylist)
rating = st.slider("Select the Rating", 1,5)
btn = st.button("Submit the response")

# id btn is passed
if btn:
    st.write("Username:", name)
    st.write("Cost:", cost)
    st.write("Comment:",comment)
    st.write("Status:", status)
    st.write("Gender:", gender)
    st.write("Quary:", quary)
    st.write("Rating:",rating)
    