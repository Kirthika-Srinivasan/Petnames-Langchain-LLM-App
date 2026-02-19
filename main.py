import langchain_helper as lch
import streamlit as st

st.title("Pets Name Generator")

animal_type_selected = st.sidebar.selectbox("What is your pet type?", ("Cat", "Dog", "Cow", "Hamster"))

if animal_type_selected == "Cat":
    pet_color = st.sidebar.text_area(label = "What color is your cat?", max_chars=15)

if animal_type_selected == "Dog":
    pet_color = st.sidebar.text_area(label = "What color is your dog?", max_chars=15)

if animal_type_selected == "Cow":
    pet_color = st.sidebar.text_area(label = "What color is your cow?", max_chars=15)

if animal_type_selected == "Hamster":
    pet_color = st.sidebar.text_area(label = "What color is your hamster?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type_selected, pet_color)
    st.text(response['pet_name'])