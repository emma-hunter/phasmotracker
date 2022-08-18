#import flask
import streamlit as st
import pandas as pd
import time

DATA = pd.DataFrame(columns=['ID','Difficulty','Events','Hunts'])

st.title("PhasmoTracker v0.1")
st.caption("This is definitely a webpage I think!")
diff = st.radio("Difficulty", ["Amateur", "Intermediate", "Professional", "Nightmare"])
event = st.number_input("Number of Ghost Events", min_value=0, value=0, step=1, format='%d')
hunt = st.number_input("Number of Ghost Hunts", min_value=0, value=0, step=1, format='%d')
button = st.button("Save Data")

def makeSessionID():
	return pd.Timestamp.asm8

def storeData(diff, event, hunt):
	return st.write("I did something with what you gave me")

if button:
	st.write("[Lie] I am doing something!")
	storeData(diff, event, hunt)