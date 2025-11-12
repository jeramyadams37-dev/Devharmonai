import streamlit as st

def show():
    st.header("💎 Staking Rewards Test")
    st.write("TEST: This is a minimal staking test page")
    
    if st.button("Test Button"):
        st.success("Button works!")
