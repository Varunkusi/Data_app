import streamlit as st

st.title("Data scince internship-Data app")
st.subheader(":blue[K.varun kumar]")
st.write("click here for [linkedin](https://www.linkedin.com/in/varun0511/)")
st.write("click here for [github](https://github.com/Varunkusi)")
st.snow()

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()