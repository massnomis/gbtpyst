import openai
import streamlit as st
st.set_page_config(layout="wide")

openai.api_key = ChatGBT_API

st.title("ChatGPT")

prompt = st.text_area("Enter Prompt", height=400)


def gptresp():
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None, 
    temperature=0.5,
).choices[0].text
    return response



if st.button("Submit"):
    response = gptresp()
    response = response.replace("Response:", "")


    with st.expander('Prompt'):

        st.write(prompt)


    with st.expander('Response (code)'):

        st.code(response)

    with st.expander('Response (text)'):
        st.write(response)
