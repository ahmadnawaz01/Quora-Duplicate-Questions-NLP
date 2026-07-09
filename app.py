import streamlit as st
import helper
import pickle
import time 


st.set_page_config(
    page_title="Duplicate Question Finder",
    page_icon="👯‍♂️",
    layout="centered"
)


@st.cache_resource
def load_model():
    return pickle.load(open('model.pkl', 'rb'))

model = load_model()


st.title('👯‍♂️ Duplicate Question Pairs')
st.markdown("""Enter two questions below to check if they share the exact same intent.
""")
st.divider()


with st.container():
    q1 = st.text_area(
        'Question 1',  
        height=100
    )
    q2 = st.text_area(
        'Question 2',  
        height=100
    )

st.write("") 

if st.button('Find Match 🔍', type='primary', use_container_width=True):
    
   
    if not q1 or not q2:
        st.warning("⚠️ Please enter both questions to compare them.")
    else:
        
        with st.spinner('Analyzing semantic equivalence...'):
            query = helper.query_point_creator(q1, q2)
            result = model.predict(query)[0]
            time.sleep(0.5) 
            
        st.divider()
        

        if result == 1:
            st.success('**Result: Duplicate!** These questions have the same underlying meaning.', icon="✅")
            st.balloons()
        else:
            st.error('**Result: Not Duplicate!** These questions are asking different things.', icon="❌")