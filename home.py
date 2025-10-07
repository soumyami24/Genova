import streamlit as st
from streamlit_extras.switch_page_button import switch_page



# Set page config
st.set_page_config(page_title="Genova", layout="centered", page_icon="🧬")
# Custom CSS with genetic-inspired theme
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;600;700&display=swap');

:root {
    --dna-primary: #00f3ff;
    --dna-secondary: #7d12ff;
    --dna-tertiary: #00ff9d;
    --dna-dark: #0a0e17;
    --dna-card: rgba(19, 28, 46, 0.8);
}

* {
    font-family: 'Exo 2', sans-serif;
}

body {
    background: linear-gradient(135deg, var(--dna-dark) 0%, #0c1220 100%);
    color: #e0f7ff;
    overflow-x: hidden;
}

.stApp {
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(0, 243, 255, 0.05) 0%, transparent 15%),
        radial-gradient(circle at 90% 80%, rgba(125, 18, 255, 0.05) 0%, transparent 15%);
    background-attachment: fixed;
}

h1, h2, h3, h4, h5, h6 {
    font-weight: 700;
    letter-spacing: 0.5px;
}

.genova-header {
    text-align: center;
    padding: 2rem 0 3rem;
    position: relative;
}

.genova-title {
    font-size: 4.5rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
    background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
}

.genova-tagline {
    color: var(--dna-tertiary);
    font-size: 1.2rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 1.5rem;
    font-weight: 300;
    position: relative;
    display: inline-block;
}

.genova-tagline::after {
    content: "";
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--dna-primary), transparent);
}

.genova-description {
    font-size: 1.15rem;
    line-height: 1.8;
    max-width: 800px;
    margin: 2rem auto;
    text-align: center;
    color: #b0e0ee;
    font-weight: 300;
}
.dna-helix {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.dna-helix svg {
    width: 110px;
    height: 110px;
    opacity: 0.7;
}
.dna-highlight {
    background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}

.feature-intro {
    margin: 4rem 0 2rem;
    font-size: 1.3rem;
    text-align: center;
    color: var(--dna-tertiary);
    position: relative;
}

.stExpander {
    background: var(--dna-card);
    border-radius: 12px !important;
    border: 1px solid rgba(0, 243, 255, 0.2) !important;
    margin-bottom: 1.5rem;
    backdrop-filter: blur(10px);
    transition: all 0.4s ease;
    overflow: hidden;
}

.stExpander:hover {
    border-color: rgba(0, 243, 255, 0.5) !important;
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 243, 255, 0.15);
}

.st-expanderHeader {
    font-size: 1.3rem !important;
    padding: 1.2rem 2rem !important;
    background: rgba(19, 28, 46, 0.6) !important;
}

.st-expanderContent {
    padding: 1.5rem 2rem !important;
    background: rgba(10, 14, 23, 0.6) !important;
}

.stButton > button {
    background: linear-gradient(90deg, var(--dna-secondary) 0%, #5d00ff 100%);
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    font-size: 1.1rem;
    border-radius: 30px;
    margin: 1rem 0 0.5rem;
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    z-index: 1;
    width: auto;
    display: inline-block;
}

.stButton > button::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 0%;
    height: 100%;
    background: linear-gradient(90deg, var(--dna-primary) 0%, var(--dna-tertiary) 100%);
    transition: all 0.4s ease;
    z-index: -1;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 243, 255, 0.4);
}

.stButton > button:hover::before {
    width: 100%;
}

.dna-footer {
    text-align: center;
    font-size: 0.9rem;
    color: #6a89a7;
    margin-top: 5rem;
    padding-top: 2rem;
    position: relative;
}

.dna-footer::before {
    content: "";
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 243, 255, 0.3), transparent);
}

.dna-icon {
    display: inline-block;
    margin: 0 5px;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { opacity: 0.7; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.1); }
    100% { opacity: 0.7; transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Header with DNA elements
st.markdown("""
<div class="genova-header">
    <h1 class="genova-title">GENOVA</h1>
    <div class="genova-tagline">Genes in Sync. Futures Aligned.</div>
</div>

<div class="genova-description">
    Welcome to <span class="dna-highlight">Genova</span>, the next-generation genomic analysis platform where science meets insight. 
    Leverage our advanced algorithms to unlock personalized genetic interpretations across multiple dimensions of your biology.
    
<br><br>
    
From <span class="dna-highlight">inherited risk assessment</span> to <span class="dna-highlight">polygenic trait analysis</span>, 
our platform transforms complex genetic data into actionable knowledge—all within an intuitive, research-grade environment.
</div>
<div class="dna-helix">
    <svg viewBox="0 0 100 100">
        <path d="M30,10 Q50,5 70,10 Q90,15 70,30 Q50,45 30,30 Q10,15 30,10Z" 
              stroke="#00f3ff" fill="none" stroke-width="2"/>
        <path d="M30,40 Q50,35 70,40 Q90,45 70,60 Q50,75 30,60 Q10,45 30,40Z" 
              stroke="#7d12ff" fill="none" stroke-width="2"/>
        <path d="M30,70 Q50,65 70,70 Q90,75 70,90 Q50,95 30,90 Q10,75 30,70Z" 
              stroke="#00ff9d" fill="none" stroke-width="2"/>
    </svg>
</div>

<div class="feature-intro">
    EXPLORE OUR GENOMIC TOOLKIT
</div>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)
# Feature Modules with enhanced design
with st.expander("GENOVA PREDICTIVE COUNSELING INTELLIGENCE SUITE", expanded=False):
    st.markdown("""
    <div style="line-height:1.7">
    ▸ Predictive inheritance modeling for 200+ conditions  
    ▸ Multi-generational risk analysis  
    ▸ Carrier probability visualization  
    ▸ Clinical-grade variant interpretation  
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Genova Predictive Counseling Intelligence Suite",key="launch_pc")==True:
        switch_page("Genova_Predictive_Counselling_Suite")

with st.expander("GENOVA PARENTHOOD PREDICTOR"):
    st.markdown("""
    <div style="line-height:1.7">
    ▸ Emotional Ccompatibility 
    ▸ Blood type incompatibility detection  
    ▸ Genetic disorder pairing analysis  
    ▸ Fertility compatibility scoring  
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Genova Parenthood Predictor",key="launch_pp")==True:
        switch_page("Genova_Parenthood_Predictor")

with st.expander("GENOVA POLYGENIC RISK PREDICTOR"):
    st.markdown("""
    <div style="line-height:1.7">
    ▸  Parental diagnosis and family history of the condition
    ▸  Substance use patterns (alcohol, tobacco, drugs)
     ▸ Age and developmental stage
    ▸ Gender and hormonal context 
    ▸ Chronic stress exposure and trauma history
    ▸
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Genova Polygenic Risk Predictor",key="launch_prs")==True:
        switch_page("Genova_Polygenic_Risk_Predictor")

# Footer with DNA animation
st.markdown("""
<div class="dna-footer">
    <div style="margin-bottom:10px">
        <span class="dna-icon">🧬</span>
        <span class="dna-icon">🧬</span>
        <span class="dna-icon">🧬</span>
    </div>
    © 2025 GENOVA GENOMICS | <span class="dna-highlight">Made with ❤️ by Soumya</span>
</div>
""", unsafe_allow_html=True)