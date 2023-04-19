import streamlit as st
import random
from PIL import Image

def guess_number():
    st.write("# Let's play a game on your Birthday!")
    st.write("### Guess the number and get a birthday surprise! 😉")
    st.write("Choose a number between 1 and 10:")
    number = st.number_input("", min_value=1, max_value=10, step=1, key="number_input")
    if st.button("Guess"):
        if random.randint(1, 3) == number:
            st.write("# 🎉🎂🎈 Happy Birthday! 🎈🎂🎉")
            st.write(" ## To the Best SISTER in the World 😀🥳 ")
            st.write(" #### May all your Dreams come true and may this year bring you lots of Joy, Happiness and Success.")
            st.write(" ### Enjoy your Special day! 🎁🥳")
            st.write(" # Have a Blast! 💣🥳")
            banner_img = Image.open("banner.jpg")
            st.image(banner_img, use_column_width=True)
            cake_img = Image.open("cake.jpg")
            st.image(cake_img, use_column_width=True)
        else:
            st.write("Sorry, that's not the correct number. Try again!")
            
                  
            
    st.write("#### Thank you for Visiting \nProject by Gehan P")
            
            
if __name__ == "__main__":
    guess_number()
