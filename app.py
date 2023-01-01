# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:18:37 2022

@author: Afroz
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 21:11:25 2022

@author: Afroz
"""

import numpy as np
import pickle
import streamlit as st

# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))



title = '<p style="font-family:Lucida Calligraphy; color:Red; font-size: 30px;">Transformer Health index Predicted By Using Artificial Intelligence</p>'
st.markdown(title, unsafe_allow_html=True)

st.subheader("High voltage power transformer condition assessment considering the health index value and its decreasing rate")
st.write("---")
with st.sidebar:
    
    st.sidebar.header('Introduction of Transformer health index (THI)')
    st.write("Power transformers are essential and expensive utilities in electrical systems."
                "This equipment is expected to be operated for years with maintaining its reliability and performance to provide a reliable electrical system."
                'Generally, the transformer has a life expectancy of 40 years or more. However, sometimes the power transformer failure may occur faster than it should because of degradation under the combination of thermal, electrical, chemical, mechanical and environmental stresses'
                ' While the transformer is operating, it is experiencing things that accelerate ageing, such as water content, temperature and oxidation. Therefore, transformer assessment has to be done to anticipate the sudden failure of the transformer..')
    
    st.sidebar.header('Description of Transformer health index (THI)')
    if st.checkbox("What is Transformer health index (THI)"):
        st.write("Transformer health index (THI) is a sophisticated tool for ranking the transformers in a fleet according to risks and intervention priority."
                " THI is a numerical score that shows the overall status of a transformer based on its condition-based monitoring."
                'The term “status” is synonymous to reliability, risk, life cycle etcetera; by assuming it as a part of transformer assessment and indexing strategies'
                'Using THI for fleet management, is like having an alarm bulb on your control panel.')
    
    
def main():
    
    
    # Age
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">The Age of the transformer</p>'
    Age = st.slider('Age', 0, 50, 15)
    st.write("Age ", Age, 'years old transformer')
    
        

    # InfraredScanResults
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Infrared Scan Results of the transformer is in the range of 0 to 1</p>'
    InfraredScanResults = st.number_input('Infrared Scan Results Enter your Value from 0 to 1 {eg 0.01, 0.1, 0.4, 0.76, 1}')
    st.write("Infrared Scan Results ", InfraredScanResults )
    
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Visual Conditions of the Transformer : Moderate Defects = 0 , Minor Defects = 1,Significant Defects = 2, Serious Defects = 3 </p>'
    st.markdown(title, unsafe_allow_html=True)
    VisualConditions = st.selectbox('VisualConditions',[0,1,2,3])
    st.write("VisualConditions", VisualConditions )
    
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">Sex of the patient : Significant Defects = 0 ,Moderate Defects = 1,Serious Defects = 2 </p>'
    st.markdown(title, unsafe_allow_html=True)
    Pad = st.selectbox('Pad',[0,1,2])
    st.write("Pad", Pad )
    
    title = '<p style="font-family:Times new roman; color:Brown; font-size: 20px;">The Loading of the transformer is KVA </p>'
    Loading = st.slider('Loading', 0, 60, 15)
    st.write("Loading", Loading)
    
    query = np.array([Age,InfraredScanResults,VisualConditions,Pad,Loading])
    
    query = query.reshape(1,5)
    st.title("The predicted health index of Transformer is " + str(float(np.exp(pipe.predict(query)[0].round(2)))))
      
    
    
if __name__ == '__main__':
    main()

st.write("  \n")
st.write("""The range of transformer health index is between [ 0 to 5 ]""")

st.write("  \n")
st.write("""You can find the theory and explanation about transformer health index  [here](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/hve2.12074).""")