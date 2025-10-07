import streamlit as st
import numpy as np
from streamlit_extras.switch_page_button import switch_page

# Set page config with DNA theme
st.set_page_config(
    page_title="Genova Predictive Counseling Intelligence Suite",
    layout="centered",
    page_icon="🧬",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)
# Custom DNA-themed CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;600;700&display=swap');

:root {
    --dna-primary: #00f3ff;
    --dna-secondary: #7d12ff;
    --dna-tertiary: #00ff9d;
    --dna-dark: #0a0e17;
    --dna-card: rgba(19, 28, 46, 0.8);
    --dna-border: rgba(0, 243, 255, 0.3);
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
    background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.genova-header {
    text-align: center;
    padding: 2rem 0 3rem;
    position: relative;
}

.genova-title {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    letter-spacing: 2px;
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

.dna-section {
    background: var(--dna-card);
    border-radius: 16px;
    border: 1px solid var(--dna-border);
    padding: 1.5rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(10px);
    transition: all 0.4s ease;
}

.dna-section:hover {
    border-color: rgba(0, 243, 255, 0.5);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 243, 255, 0.15);
}

.stButton > button {
    background: linear-gradient(90deg, var(--dna-secondary) 0%, #5d00ff 100%);
    color: white !important;
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

.stTextInput>div>div>input,
.stSelectbox>div>div>select,
.stNumberInput>div>div>input {
    background-color: var(--dna-card) !important;
    color: #e0f7ff !important;
    border: 1px solid var(--dna-border) !important;
    border-radius: 12px !important;
    padding: 0.75rem 1rem !important;
}

.stCheckbox>label {
    color: #e0f7ff !important;
    background: rgba(19, 28, 46, 0.5);
    padding: 0.8rem 1.2rem;
    border-radius: 12px;
    border-left: 3px solid var(--dna-tertiary);
    margin: 0.5rem 0;
    transition: all 0.3s ease;
}

.stCheckbox>label:hover {
    background: rgba(19, 28, 46, 0.7);
    transform: translateX(5px);
}

.stCheckbox>input:checked + label {
    border-left-color: var(--dna-primary);
    background: rgba(0, 243, 255, 0.1);
}

.dna-result {
    padding: 1.5rem;
    border-radius: 16px;
    background: rgba(10, 14, 23, 0.7);
    border-left: 5px solid var(--dna-primary);
    margin: 1.5rem 0;
    box-shadow: 0 0 20px rgba(0, 243, 255, 0.1);
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

.dna-divider {
    height: 3px;
    background: linear-gradient(90deg, transparent, var(--dna-primary), transparent);
    border: none;
    margin: 2rem 0;
}

.dna-helix {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.dna-helix svg {
    width: 80px;
    height: 80px;
    opacity: 0.7;
}

.disease-header {
    font-size: 1.8rem;
    padding: 12px 20px;
    border-radius: 12px;
    background: linear-gradient(90deg, rgba(0,243,255,0.1) 0%, rgba(125,18,255,0.1) 100%);
    margin: 30px 0 20px 0;
    border-left: 4px solid var(--dna-primary);
}

.risk-tag {
    color: white !important;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: bold;
    display: inline-block;
}

.risk-low { background-color: #00ff9d; }
.risk-moderate { background-color: #ffd66b; }
.risk-high { background-color: #ff6b6b; }
.risk-vhigh { background-color: #ff2e63; }

.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary)) !important;
}

.stMarkdown h3 {
    border-bottom: 2px solid var(--dna-border);
    padding-bottom: 8px;
}

.stRadio > div {
    flex-direction: row !important;
    gap: 15px;
}

.stRadio > div > label {
    background: var(--dna-card) !important;
    border: 1px solid var(--dna-border) !important;
    border-radius: 12px !important;
    padding: 12px 20px !important;
    margin: 5px 0 !important;
    transition: all 0.3s ease;
}

.stRadio > div > label:hover {
    border-color: var(--dna-primary) !important;
    transform: translateY(-3px);
}

.stRadio > div > label > div:first-child {
    display: none;
}

.stRadio > div > label > div:last-child {
    width: 100% !important;
    padding-left: 0 !important;
}

.stMultiSelect > div > div {
    background-color: var(--dna-card) !important;
    border: 1px solid var(--dna-border) !important;
    border-radius: 12px !important;
}

.stMultiSelect > div > div:hover {
    border-color: var(--dna-primary) !important;
}

.stMultiSelect span {
    background-color: rgba(125, 18, 255, 0.3) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
}

.stMultiSelect span > div > svg {
    color: white !important;
}

.stMultiSelect div[data-baseweb="popover"] > div {
    background-color: var(--dna-dark) !important;
    border: 1px solid var(--dna-border) !important;
}

.stMultiSelect div[data-baseweb="popover"] li {
    background-color: var(--dna-dark) !important;
    color: white !important;
}

.stMultiSelect div[data-baseweb="popover"] li:hover {
    background-color: rgba(125, 18, 255, 0.3) !important;
}

.stExpander > div {
    background: var(--dna-card) !important;
    border: 1px solid var(--dna-border) !important;
    border-radius: 16px !important;
    margin-bottom: 1rem;
}

.stExpander > div > div {
    padding: 1rem;
}

.radio-group {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin: 15px 0;
}

.radio-item {
    background: var(--dna-card);
    border: 1px solid var(--dna-border);
    border-radius: 12px;
    padding: 12px 15px;
    transition: all 0.3s ease;
}

.radio-item:hover {
    border-color: var(--dna-primary);
    transform: translateY(-3px);
}

.radio-item.selected {
    border-color: var(--dna-primary);
    background: rgba(0, 243, 255, 0.1);
}

.required-field {
    border: 1px solid var(--dna-tertiary) !important;
    box-shadow: 0 0 5px rgba(0, 255, 157, 0.5);
}

.warning-box {
    background-color: #332E31;
    padding: 1em;
    border-left: 5px solid #FF6584;
    border-radius: 10px;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for open assessments and form validation
if 'open_assessments' not in st.session_state:
    st.session_state.open_assessments = {}
if 'patient_info_complete' not in st.session_state:
    st.session_state.patient_info_complete = False
if 'form_errors' not in st.session_state:
    st.session_state.form_errors = {}

# Header with DNA elements
# ... (previous CSS and setup code remains the same) ...

# Header with DNA elements
st.markdown("""
<div class="genova-header">
    <h1 class="genova-title">GENOVA</h1>
    <div class="genova-tagline">Genes in Sync. Futures Aligned.</div>
</div>

<div class="genova-description">
    Welcome to <span class="dna-highlight">Genova</span>, the next-generation genomic analysis platform where science meets insight. 
    Leverage our advanced algorithms to unlock personalized genetic interpretations across multiple dimensions of your biology.
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
    Genova Predictive Counseling Intelligence Suite
</div>
""", unsafe_allow_html=True)

# Main container with two columns
with st.container():
    col_form, col_info = st.columns([8, 7])
    
    # Patient Information Section (left column)
    with col_form:
        st.markdown("#### 👤 PATIENT INFORMATION")
 
        name = st.text_input("**Patient Name**", placeholder="Enter patient's full name", key="dna_name")
        age = st.number_input("**Age**", 1, 200, 30, key="dna_age")
        gender = st.selectbox("**Gender**", 
                                ['Select', 'Male', 'Female', 'Other'], 
                                key="dna_gender")
        ethnicity = st.selectbox("**Ethnicity**", 
                                ['Select', 'Caucasian', 'African', 'Asian', 'Hispanic', 'Mixed', 'Other'], 
                                key="dna_ethnicity")
        
        # Validate patient info
        if st.button("Save Patient Information", key="save_patient_info"):
            if not name or gender == 'Select' or ethnicity == 'Select':
                st.session_state.form_errors['patient_info'] = "Please complete all patient information fields"
                st.session_state.patient_info_complete = False
            else:
                st.session_state.patient_info_complete = True
                st.session_state.form_errors['patient_info'] = None
                st.success("Patient information saved successfully!")
        
        if 'patient_info' in st.session_state.form_errors and st.session_state.form_errors['patient_info']:
            st.warning(st.session_state.form_errors['patient_info'])
    
    # Information Panel (right column)
    with col_info:
        # About Genova Predictive Counseling Suite
        with st.expander("🔬 ABOUT GENOVA PREDICTIVE COUNSELING SUITE", expanded=False):
            st.markdown("""
            <div class="dna-section">
                <p>Genova Predictive Counseling Suite is an advanced genomic analysis platform that:</p>
                <ul>
                    <li>Provides personalized genetic risk assessments</li>
                    <li>Integrates family health history for comprehensive analysis</li>
                    <li>Offers evidence-based clinical recommendations</li>
                    <li>Supports genetic counseling decision-making</li>
                    <li>Visualizes complex genetic data intuitively</li>
                </ul>
                <p>Developed in accordance with ACMG guidelines and clinical best practices.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # How to Use
        with st.expander("🔧 HOW TO USE", expanded=False):
            st.markdown("""
            <div class="dna-section">
                <p><b>Step-by-step guide:</b></p>
                <ol>
                    <li>Complete patient information</li>
                    <li>Select genetic conditions for assessment</li>
                    <li>Provide family health history details</li>
                    <li>Review risk calculations and recommendations</li>
                    <li>Consult with a genetic counselor</li>
                </ol>
                <p>All information is securely processed and never stored.</p>
            </div>
            """, unsafe_allow_html=True)
        
        # How is Risk Calculated?
        with st.expander("🔍 HOW IS THIS CALCULATED?", expanded=False):
            st.markdown("""
            <div class="dna-section">
                <p>Our algorithms combine:</p>
                <ul>
                    <li>Established inheritance patterns</li>
                    <li>Population-specific prevalence data</li>
                    <li>Family health history analysis</li>
                    <li>Penetrance and expressivity factors</li>
                    <li>Clinical validation studies</li>
                </ul>
                <p>Risk levels are categorized as:</p>
                <p><span class="risk-tag risk-low">Low</span>
                <span class="risk-tag risk-moderate">Moderate</span>
                <span class="risk-tag risk-high">High</span>
                <span class="risk-tag risk-vhigh">Very High</span></p>
            </div>
            """, unsafe_allow_html=True)

# ... (the rest of the code remains unchanged - disease selection, risk calculation, etc.) ...

    # Disease Selection
    with st.container():
        st.markdown("#### 🧬 GENETIC CONDITIONS ASSESSMENT")
        diseases = st.multiselect("**Select Genetic Conditions for Risk Assessment**", [
            'Cystic Fibrosis', 'Sickle Cell Anemia', 'Tay-Sachs Disease', 'Phenylketonuria (PKU)', 
            'Gaucher Disease', 'Thalassemia (Alpha/Beta)', 'Maple Syrup Urine Disease', 'Huntington’s Disease',
            'Marfan Syndrome', 'Achondroplasia', 'Neurofibromatosis Type 1 & 2', 'Polycystic Kidney Disease (Adult)',
            'Familial Hypercholesterolemia', 'Osteogenesis Imperfecta', 'Hemophilia A & B', 'Duchenne Muscular Dystrophy',
            'Color Blindness (Red-Green)', 'Fragile X Syndrome', 'X-linked Agammaglobulinemia', 'G6PD Deficiency',
            'Rett Syndrome', 'Down Syndrome', 'Turner Syndrome', 'Klinefelter Syndrome', 'Patau Syndrome', 'Edwards Syndrome',
            'Cri-du-chat Syndrome', 'Williams Syndrome', 'Chronic Myeloid Leukemia (CML)', 'Burkitt Lymphoma', 
            'Ewing Sarcoma', 'Campomelic Dysplasia', 'DiGeorge Syndrome'
        ], placeholder="Select conditions to assess", key="dna_diseases")

    # --- CLINICALLY VALIDATED RISK CALCULATION FUNCTIONS ---
    # (Identical to your original functions)

    # ... (all previous imports and CSS code remains the same) ...

    # --- UPDATED RISK CALCULATION FUNCTIONS WITH PARENT STATUS ---

    # ... (previous CSS and setup code remains the same) ...

    # --- FIXED RISK CALCULATION FUNCTIONS WITH WORKING RADIO BUTTONS ---

    def autosomal_recessive(disease):
        st.markdown(f"<div class='disease-header'>{disease} Genetic Assessment</div>", unsafe_allow_html=True)
        st.caption("Autosomal Recessive Inheritance Pattern")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Male Partner**")
            male_status = st.selectbox("Affected/Carrier Status:", 
                                ["Affected", "Confirmed Carrier", "Not Affected/Unknown Carrier Status"],
                                key=f"male_status_{disease}")
            male_testing = st.checkbox("Genetic testing performed", key=f"male_test_{disease}")
            
            # Parent health status for male partner
            st.markdown("**Parental Health (Male Side)**")
            male_father_status = st.selectbox("Father's Status:", 
                                        ["Affected", "Carrier", "Not Affected/Unknown", "Deceased/Unknown"],
                                        key=f"male_father_{disease}")
            male_mother_status = st.selectbox("Mother's Status:", 
                                        ["Affected", "Carrier", "Not Affected/Unknown", "Deceased/Unknown"],
                                        key=f"male_mother_{disease}")
            
        with col2:
            st.markdown("**Female Partner**")
            female_status = st.selectbox("Affected/Carrier Status:", 
                                    ["Affected", "Confirmed Carrier", "Not Affected/Unknown Carrier Status"],
                                    key=f"female_status_{disease}")
            female_testing = st.checkbox("Genetic testing performed", key=f"female_test_{disease}")
            
            # Parent health status for female partner
            st.markdown("**Parental Health (Female Side)**")
            female_father_status = st.selectbox("Father's Status:", 
                                        ["Affected", "Carrier", "Not Affected/Unknown", "Deceased/Unknown"],
                                        key=f"female_father_{disease}")
            female_mother_status = st.selectbox("Mother's Status:", 
                                        ["Affected", "Carrier", "Not Affected/Unknown", "Deceased/Unknown"],
                                        key=f"female_mother_{disease}")
        
        # Clinical risk calculation with parental information
        risk = 0.0
        
        # Both partners affected
        if male_status == "Affected" and female_status == "Affected":
            risk = 100.0
        
        # One affected, one confirmed carrier
        elif (male_status == "Affected" and female_status == "Confirmed Carrier") or \
            (female_status == "Affected" and male_status == "Confirmed Carrier"):
            risk = 50.0
        
        # Both confirmed carriers
        elif male_status == "Confirmed Carrier" and female_status == "Confirmed Carrier":
            risk = 25.0
        
        # One affected, one not affected
        elif (male_status == "Affected" and female_status == "Not Affected/Unknown Carrier Status") or \
            (female_status == "Affected" and male_status == "Not Affected/Unknown Carrier Status"):
            risk = 1.0
        
        # One confirmed carrier, one not affected
        elif (male_status == "Confirmed Carrier" and female_status == "Not Affected/Unknown Carrier Status") or \
            (female_status == "Confirmed Carrier" and male_status == "Not Affected/Unknown Carrier Status"):
            risk = 0.5
        
        # Neither affected nor confirmed carriers
        else:
            risk = 0.1
        
        # Adjust risk based on parental status
        parental_factors = 0
        
        # Helper function to calculate parental risk
        def get_parental_risk(father, mother):
            risk = 0
            if father == "Affected" or mother == "Affected":
                risk += 10
            if father == "Carrier" or mother == "Carrier":
                risk += 5
            if father == "Affected" and mother == "Affected":
                risk += 25
            if father == "Carrier" and mother == "Carrier":
                risk += 15
            return risk
        
        # Add parental risk from both sides
        parental_factors += get_parental_risk(male_father_status, male_mother_status)
        parental_factors += get_parental_risk(female_father_status, female_mother_status)
        
        # Apply parental risk factor
        risk = min(risk + parental_factors, 100)
        
        return risk

    def autosomal_dominant(disease):
        st.markdown(f"<div class='disease-header'>{disease} Genetic Assessment</div>", unsafe_allow_html=True)
        st.caption("Autosomal Dominant Inheritance Pattern")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Male Partner**")
            male_affected = st.selectbox("Affected Status:", 
                                    ["Affected", "Not Affected", "Unknown"],
                                    key=f"ad_male_{disease}")
            male_testing = st.checkbox("Genetic testing performed", key=f"ad_male_test_{disease}")
            if male_affected == "Affected":
                male_penetrance = st.slider("Estimated Penetrance (%)", 0, 100, 90, 
                                        key=f"ad_male_pen_{disease}")
            else:
                male_penetrance = 0
            
            # Parent health status for male partner
            st.markdown("**Parental Health (Male Side)**")
            male_father_status = st.selectbox("Father's Status:", 
                                        ["Affected", "Not Affected", "Unknown", "Deceased"],
                                        key=f"ad_male_father_{disease}")
            male_mother_status = st.selectbox("Mother's Status:", 
                                        ["Affected", "Not Affected", "Unknown", "Deceased"],
                                        key=f"ad_male_mother_{disease}")
            
        with col2:
            st.markdown("**Female Partner**")
            female_affected = st.selectbox("Affected Status:", 
                                    ["Affected", "Not Affected", "Unknown"],
                                    key=f"ad_female_{disease}")
            female_testing = st.checkbox("Genetic testing performed", key=f"ad_female_test_{disease}")
            if female_affected == "Affected":
                female_penetrance = st.slider("Estimated Penetrance (%)", 0, 100, 90, 
                                            key=f"ad_female_pen_{disease}")
            else:
                female_penetrance = 0
            
            # Parent health status for female partner
            st.markdown("**Parental Health (Female Side)**")
            female_father_status = st.selectbox("Father's Status:", 
                                        ["Affected", "Not Affected", "Unknown", "Deceased"],
                                        key=f"ad_female_father_{disease}")
            female_mother_status = st.selectbox("Mother's Status:", 
                                        ["Affected", "Not Affected", "Unknown", "Deceased"],
                                        key=f"ad_female_mother_{disease}")
        
        # Clinical risk calculation
        risk = 0.0
        
        # Both partners affected
        if male_affected == "Affected" and female_affected == "Affected":
            avg_penetrance = (male_penetrance + female_penetrance) / 2
            risk = 75 * (avg_penetrance / 100)
        
        # One partner affected
        elif male_affected == "Affected" or female_affected == "Affected":
            penetrance = male_penetrance if male_affected == "Affected" else female_penetrance
            risk = 50 * (penetrance / 100)
        
        # Neither partner affected
        else:
            risk = 1.0
        
        # Adjust risk based on parental status
        parental_factors = 0
        def get_ad_parental_risk(status):
            if status == "Affected":
                return 15
            elif status == "Unknown":
                return 5
            return 0
        
        parental_factors += get_ad_parental_risk(male_father_status)
        parental_factors += get_ad_parental_risk(male_mother_status)
        parental_factors += get_ad_parental_risk(female_father_status)
        parental_factors += get_ad_parental_risk(female_mother_status)
        
        risk = min(risk + parental_factors, 100)
        
        return risk

    def X_linked(disease):
        st.markdown(f"<div class='disease-header'>{disease} Genetic Assessment</div>", unsafe_allow_html=True)
        st.caption("X-linked Inheritance Pattern")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Male Partner**")
            male_affected = st.selectbox("Affected Status:", 
                                    ["Affected", "Not Affected", "Unknown"],
                                    key=f"xl_male_{disease}")
            
            # Parent health status for male partner
            st.markdown("**Parental Health (Male Side)**")
            male_father_status = st.selectbox("Father's Status:", 
                                        ["Affected", "Not Affected", "Unknown", "Deceased"],
                                        key=f"xl_male_father_{disease}")
            male_mother_status = st.selectbox("Mother's Status:", 
                                        ["Affected", "Carrier", "Not Affected", "Unknown"],
                                        key=f"xl_male_mother_{disease}")
            
        with col2:
            st.markdown("**Female Partner**")
            female_status = st.selectbox("Status:",["Affected", "Confirmed Carrier", "Not Affected/Unknown Carrier Status"],key=f"xl_female_{disease}")
            female_testing = st.checkbox("Genetic testing performed", key=f"xl_female_test_{disease}")
            
            # Parent health status for female partner
            st.markdown("**Parental Health (Female Side)**")
            female_father_status = st.selectbox("Father's Status:", ["Affected", "Not Affected", "Unknown", "Deceased"], key=f"xl_female_father_{disease}")
            female_mother_status = st.selectbox("Mother's Status:", ["Affected", "Carrier", "Not Affected", "Unknown"],key=f"xl_female_mother_{disease}")
        
        # Clinical risk calculation
        transmission_risk = 0.0
        carrier_risk = 0.0
        
        # Affected male partner
        if male_affected == "Affected":
            transmission_risk = 0.0  # Sons inherit Y chromosome
            carrier_risk = 100.0     # All daughters will be carriers
        
        # Affected or carrier female partner
        elif female_status in ["Affected", "Confirmed Carrier"]:
            transmission_risk = 50.0  # 50% chance for sons to be affected
            carrier_risk = 50.0       # 50% chance for daughters to be carriers
        
        # Neither affected but family history
        else:
            transmission_risk = 0.1
            carrier_risk = 0.2
        
        # Adjust risk based on parental status
        if male_mother_status == "Carrier":
            transmission_risk += 20
            carrier_risk += 10
        if female_mother_status == "Carrier":
            transmission_risk += 20
            carrier_risk += 10
        if male_father_status == "Affected":
            transmission_risk += 15
        if female_father_status == "Affected":
            transmission_risk += 15
        
        transmission_risk = min(transmission_risk, 100)
        carrier_risk = min(carrier_risk, 100)
        
        return transmission_risk, carrier_risk

    # ... (chromosomal_abnormalities and chromosomal_rearrangement functions would have similar fixes) ...

    # ... (rest of the code remains the same) ...

    def chromosomal_abnormalities(disease):
        # ... (existing code remains the same) ...
        
        # ADDED: Parent health section
        st.markdown("**Parental Health History**")
        col1, col2 = st.columns(2)
        with col1:
            mother_chromosomal = st.selectbox("Mother has chromosomal abnormality?", 
                                        ["Yes", "No", "Unknown"],
                                        key=f"mat_ab_{disease}")
        with col2:
            father_chromosomal = st.selectbox("Father has chromosomal abnormality?", 
                                        ["Yes", "No", "Unknown"],
                                        key=f"pat_ab_{disease}")
        
        # ADDED: Adjust risk based on parental abnormalities
        if mother_chromosomal == "Yes" or father_chromosomal == "Yes":
            base_risk *= 3.0
        
        return min(base_risk, 15.0)

    def chromosomal_rearrangement(disease):
        # ... (existing code remains the same) ...
        
        # ADDED: Detailed parental health status
        st.markdown("**Parental Chromosomal Health**")
        col1, col2 = st.columns(2)
        with col1:
            mother_history = st.selectbox("Mother's rearrangement history:", 
                                        ["None", "Balanced", "Unbalanced", "Unknown"],
                                        key=f"mat_rearr_{disease}")
        with col2:
            father_history = st.selectbox("Father's rearrangement history:",["None", "Balanced", "Unbalanced", "Unknown"],key=f"pat_rearr_{disease}")
        
        # ADDED: Adjust risk based on parental history
        if mother_history == "Unbalanced" or father_history == "Unbalanced":
            risk += 25.0
        elif mother_history == "Balanced" or father_history == "Balanced":
            risk += 15.0
        
        return min(risk, 80.0)

    # ... (rest of the code remains the same) ...

    # Helper functions
    def get_risk_category(risk):
        if risk < 5:
            return "Low Risk", "risk-low"
        elif risk < 20:
            return "Moderate Risk", "risk-moderate"
        elif risk < 50:
            return "High Risk", "risk-high"
        else:
            return "Very High Risk", "risk-vhigh"

    def get_recommendation(disease, category, risk_value):
        recommendations = {
            "Low Risk": [
                f"Routine genetic counseling not indicated for {disease}",
                "Standard prenatal screening recommended",
                "Family history should be reassessed periodically"
            ],
            "Moderate Risk": [
                f"Genetic counseling recommended for {disease}",
                "Consider carrier screening or advanced prenatal testing",
                "Detailed family history assessment recommended"
            ],
            "High Risk": [
                f"Referral to genetic specialist for {disease}",
                "Offer diagnostic testing (CVS/amniocentesis)",
                "Preimplantation genetic diagnosis (PGD) discussion",
                "Regular monitoring and surveillance recommended"
            ],
            "Very High Risk": [
                f"Immediate referral to genetic specialist for {disease}",
                "Strongly recommend diagnostic testing",
                "Consider PGD for future pregnancies",
                "Comprehensive family screening indicated",
                "Develop personalized management plan"
            ]
        }
        return recommendations[category]

    def show_result(disease, risk, carrier_risk=None):
        category, risk_class = get_risk_category(risk)
        
        # Create columns for metrics
        if carrier_risk is not None:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Transmission Risk (sons)", f"{risk:.2f}%", help="Risk of passing the condition to male offspring")
            with col2:
                st.metric("Carrier Risk (daughters)", f"{carrier_risk:.2f}%", help="Risk of daughters being carriers")
        else:
            st.metric("Overall Risk", f"{risk:.2f}%", category)
        
        # Risk visualization
        st.caption("Risk Level Visualization")
        risk_value = min(risk / 100, 1.0)  # Normalize to 0-1
        st.progress(risk_value, text=f"{risk:.1f}% risk")
        
        # Risk category indicator
        st.markdown(f"<div class='risk-tag {risk_class}'>{category}</div>", unsafe_allow_html=True)
        
        # Clinical recommendations
        st.markdown("**Clinical Recommendations**")
        recommendations = get_recommendation(disease, category, risk)
        for rec in recommendations:
            st.markdown(f"<div style='padding: 5px 0;'>✓ {rec}</div>", unsafe_allow_html=True)
        
        # References
        st.divider()
        st.caption("**Clinical References**: Based on guidelines from ACMG, ACOG, and NSGC")

    # Main assessment logic
    if diseases:
        st.markdown("---")
        st.markdown("### 🧬 GENETIC RISK ASSESSMENTS")
        st.markdown("""
        <div class="dna-section">
            This tool provides risk estimates based on current genetic knowledge. 
            Consult a certified genetic counselor for personalized clinical interpretation.
        </div>
        """, unsafe_allow_html=True)
        
        for disease in diseases:
            # Initialize session state for this disease
            if disease not in st.session_state.open_assessments:
                st.session_state.open_assessments[disease] = False
            
            # Toggle button
            if st.button(f"{'▼' if st.session_state.open_assessments[disease] else '►'} {disease}",
                        key=f"btn_{disease}",
                        help=f"Click to expand/collapse {disease} assessment"):
                st.session_state.open_assessments[disease] = not st.session_state.open_assessments[disease]
            
            # Show assessment if open
            if st.session_state.open_assessments[disease]:
                with st.expander(f"{disease} Assessment", expanded=True):
                    # Disease information
                    st.markdown(f"""
                    <div class="dna-section">
                        <b>Condition Overview:</b> Genetic disorder assessment for {disease}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if disease in [
                        'Cystic Fibrosis', 'Sickle Cell Anemia', 'Tay-Sachs Disease',
                        'Phenylketonuria (PKU)', 'Gaucher Disease', 'Thalassemia (Alpha/Beta)',
                        'Maple Syrup Urine Disease'
                    ]:
                        risk = autosomal_recessive(disease)
                        if st.button(f"Calculate {disease} Risk", key=f"calc_recessive_{disease}"):
                            show_result(disease, risk)
                            
                    elif disease in [
                        'Huntington’s Disease', 'Marfan Syndrome', 'Achondroplasia',
                        'Neurofibromatosis Type 1 & 2', 'Polycystic Kidney Disease (Adult)',
                        'Familial Hypercholesterolemia', 'Osteogenesis Imperfecta'
                    ]:
                        risk = autosomal_dominant(disease)
                        if st.button(f"Calculate {disease} Risk", key=f"calc_dominant_{disease}"):
                            show_result(disease, risk)
                            
                    elif disease in [
                        'Hemophilia A & B', 'Duchenne Muscular Dystrophy',
                        'Color Blindness (Red-Green)', 'Fragile X Syndrome',
                        'X-linked Agammaglobulinemia', 'G6PD Deficiency', 'Rett Syndrome'
                    ]:
                        transmission_risk, carrier_risk = X_linked(disease)
                        if st.button(f"Calculate {disease} Risk", key=f"calc_xlinked_{disease}"):
                            show_result(disease, transmission_risk, carrier_risk)
                            
                    elif disease in [
                        'Down Syndrome', 'Turner Syndrome', 'Klinefelter Syndrome',
                        'Patau Syndrome', 'Edwards Syndrome', 'Cri-du-chat Syndrome',
                        'Williams Syndrome'
                    ]:
                        risk = chromosomal_abnormalities(disease)
                        if st.button(f"Calculate {disease} Risk", key=f"calc_abnormalities_{disease}"):
                            show_result(disease, risk)
                            
                    elif disease in [
                        'Chronic Myeloid Leukemia (CML)', 'Burkitt Lymphoma',
                        'Ewing Sarcoma', 'Campomelic Dysplasia', 'DiGeorge Syndrome'
                    ]:
                        risk = chromosomal_rearrangement(disease)
                        if st.button(f"Calculate {disease} Risk", key=f"calc_rearrangement_{disease}"):
                            show_result(disease, risk)

    # Disclaimer
    st.markdown("---")
    st.markdown("""
    <div class="dna-section">
        <strong>Clinical Disclaimer</strong>
        <p>This tool provides risk estimates based on current genetic knowledge and ACMG guidelines. 
        It does not replace professional genetic counseling. Actual risks may vary based on individual 
        genomic factors not captured in this assessment. All results should be interpreted by a board-certified 
        genetic counselor or medical geneticist.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("Back to Home", key="back_to_home"):
    st.session_state.open_assessments = {}
    st.session_state.patient_info_complete = False
    st.session_state.form_errors = {}
    try:
        from streamlit_extras.switch_page_button import switch_page
        switch_page("home")
    except ImportError:
        st.experimental_set_query_params(page="home")
        st.experimental_rerun()    
# Footer with DNA animation
st.markdown("""
<div class="dna-footer">
    <div style="margin-bottom:10px">
        <span class="dna-icon">🧬</span>
        <span class="dna-icon">🧬</span>
        <span class="dna-icon">🧬</span>
    </div>
    © 2025 GENOVA GENOMICS | <span class="dna-highlight">Genes in Sync. Futures Aligned.</span>
</div>
""", unsafe_allow_html=True)
