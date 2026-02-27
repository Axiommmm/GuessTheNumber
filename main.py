import streamlit as st
import random as rd

if "number" not in st.session_state:
    st.session_state.number = rd.randint(1,101)
    st.session_state.step = 1    
    st.session_state["guesses"] = []
guesses: list[int] = st.session_state["guesses"]

st.title("The number is between 1 and 100")

for guess in guesses:
    if ( guess > st.session_state.number ):
         st.error(f"{guess} High!")
    elif ( guess < st.session_state.number ):
         st.error(f"{guess} Low!")
    else:
        st.success(f"{guess} You Won!")

with st.form(clear_on_submit=True, key="input"):
    inp = st.number_input("Enter your guess: ", min_value=1, max_value=100,step=1, value=None)
    button = st.form_submit_button("Guess")
    
    if button and inp:
        st.session_state.guesses.append(inp)
        st.rerun()
