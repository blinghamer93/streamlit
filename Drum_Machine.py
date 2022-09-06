import streamlit as st
import pandas as pd
import time 
from playsound import playsound
from threading import Thread

st.set_page_config(
     page_title="Drum Machine 3000",
     page_icon="🧊",
     menu_items={
         'About': "This app was made by Alec Schwinghamer.Check me out [here](https://www.linkedin.com/in/alecschwinghamer/)."
     }
 )

st.title('Ultra Drum Machine 3000', anchor=None)
st.write("[Download the template](https://docs.google.com/spreadsheets/d/1WLKpOcwYqN_OLGdw7-gOAGRMhEi0CaKGiww4FsI0Bv0/edit?usp=sharing) and then upload it below to start becoming a beat god. ")

uploaded_file = st.file_uploader("Choose a file")

sound = st.selectbox(
     'Select your sound:',
     ("Volca Dry","Volca Stutter"))

note = st.selectbox(
     'Note length:',
     ("1/8","1/16"))

loops = st.slider('Select amount of bars:', 1, 32, 2)

bpm = st.slider('Select BPM:', 60, 200, 80)

def Kick():
    playsound(f'Samples/{sound}/Kick.WAV')
def Snare():
    playsound(f'Samples/{sound}/Snare.WAV')
def Lo_Tom():
    playsound(f'Samples/{sound}/Lo Tom.WAV')
def Hi_Tom():
    playsound(f'Samples/{sound}/Hi Tom.WAV')    
def Closed_Hat():
    playsound(f'Samples/{sound}/Closed Hat.WAV')    
def Open_Hat():
    playsound(f'Samples/{sound}/Open Hat.WAV')        
def Clap():
    playsound(f'Samples/{sound}/Clap.WAV')
def Claves():
    playsound(f'Samples/{sound}/Claves.WAV')
def Agogo():
    playsound(f'Samples/{sound}/Agogo.WAV')
def Crash():
    playsound(f'Samples/{sound}/Crash.WAV')
    


if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)

    if note == '1/16':
        second = 60/(bpm*4)
    else: 
        second = 60/(bpm*2)

    for y in range (loops):    
        for i in range(16):
            time.sleep(second)
            if df.iloc[0,i+1] == 'x':
                Thread(target=Kick).start()
            if df.iloc[1,i+1] == 'x':
                Thread(target=Snare).start()
            if df.iloc[2,i+1] == 'x':
                Thread(target=Lo_Tom).start()
            if df.iloc[3,i+1] =='x':
                Thread(target=Hi_Tom).start()
            if df.iloc[4,i+1] =='x':
                Thread(target=Closed_Hat).start()
            if df.iloc[5,i+1] =='x':
                Thread(target=Open_Hat).start()       
            if df.iloc[6,i+1] =='x':
                Thread(target=Clap).start()
            if df.iloc[7,i+1] =='x':
                Thread(target=Claves).start()
            if df.iloc[8,i+1] =='x':
                Thread(target=Agogo).start()
            if df.iloc[9,i+1] =='x':
                Thread(target=Crash).start()
