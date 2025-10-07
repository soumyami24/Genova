import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# Set page config with DNA theme
st.set_page_config(
    page_title="Genova Polygenic Risk Predictor",
    layout="centered",
    page_icon="🧬",
    initial_sidebar_state="collapsed"
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
    font-size: 4.5rem;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 3px;
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
.stSelectbox>div>div>select {
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
    POLYGENIC RISK PREDICTOR
</div>
""", unsafe_allow_html=True)

# Main layout
with st.container():
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Genomic Profile Section
        with st.container():
            st.markdown("#### 🧬 GENOMIC PROFILE")
            name = st.text_input("**Enter genomic identifier:**", placeholder="e.g., Subject-42", key="dna_id")
            
            st.markdown("#### 🧪 DISEASE RISK ANALYSIS")
            disease = st.selectbox(
                "**Select target disease for genomic profiling:**",
                options=[
                    'Select',
                    'Type 2 Diabetes',
                    'Prostate Cancer',
                    'Coronary Heart Disease',
                    'Asthma',
                    'Depression',
                    'Breast Cancer',
                    'Hypertension',
                    'Osteoporosis',
                    'COPD',
                    'Cervical Cancer',
                    'Thyroid Disorders',
                    'Lung Cancer',
                    'Stroke',
                    'Liver Disease',
                    'PCOD'
                ],
                key="dna_disease"
            )
    
    with col2:

            with st.expander(" ⚠️ NON-DIAGNOSTIC DISCLAIMER", expanded=False):
                st.markdown("""
                    <div class="dna-section">
                        This tool simulates polygenic risk scoring and does not replace clinical evaluation. 
                    </div>
                """, unsafe_allow_html=True) 
            with st.expander(" 🔬 ABOUT GENOVA POLYGENIC RISK PREDICTOR", expanded=False):
                st.markdown("""
                    <div class="dna-section">
                        Advanced AI-driven polygenic risk modeling for disease susceptibility estimation.
                    </div>
                """, unsafe_allow_html=True) 
            with st.expander(" 🧬 WHAT IS A PRS?", expanded=False):
                st.markdown("""
                    <div class="dna-section">
                        Polygenic Risk Scores (PRS) aggregate genetic variants to estimate disease risk.
                        This tool provides insights into your genomic predisposition across various diseases.
                    </div>
                """, unsafe_allow_html=True)        

# Helper Functions
def section_header(title):
    st.markdown(f"""
        <div class="disease-header">{title}</div>
    """, unsafe_allow_html=True)

def result_box(level, score, message):
    color_map = {
        "Low": "#00ff9d",
        "Moderate": "#ffd66b",
        "High": "#ff6b6b"
    }
    
    st.markdown(f"""
        <div class="dna-result" style="border-left-color: {color_map[level]};">
            <h4 style='color: {color_map[level]}; margin-top: 0;'>🧬 {level} RISK (SCORE: {score})</h4>
            <p>{message}</p>
        </div>
    """, unsafe_allow_html=True)

def check_name():
    if not name or name.strip() == "":
        st.markdown("""
            <div class="dna-result" style="border-left-color: #ff6b6b;">
                <h4 style='color: #ff6b6b; margin-top: 0;'>⚠️ INPUT REQUIRED</h4>
                <p>Please enter your genomic identifier before proceeding.</p>
            </div>
        """, unsafe_allow_html=True)
        return False
    return True

# Disease Sections
if disease != 'Select':
    st.markdown("---")
    
    # Type 2 Diabetes
    if disease == 'Type 2 Diabetes':
        section_header("TYPE 2 DIABETES RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            parent = st.checkbox("Parent with Diabetes")
            gparent = st.checkbox("Grandparent with Diabetes")
            bmi = st.checkbox("BMI > 30")
            sedentary = st.checkbox("Sedentary lifestyle (>6 hrs/day)")
        
        with col2:
            bp = st.checkbox("High Blood Pressure")
            cholesterol = st.checkbox("High Cholesterol")
            age = st.checkbox("Age > 45")
            smoker = st.checkbox("Active Smoker")

        score = sum([
            2 if parent else 0,
            1 if gparent else 0,
            2 if bmi else 0,
            1 if sedentary else 0,
            1 if bp else 0,
            1 if cholesterol else 0,
            1 if age else 0,
            1 if smoker else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="diabetes_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Your genomic profile indicates low susceptibility to Type 2 Diabetes. Maintain healthy lifestyle habits.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Consider lifestyle modifications and regular monitoring.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors identified. Consult with a genetic counselor for personalized management.")

    # Coronary Heart Disease
    elif disease == 'Coronary Heart Disease':
        section_header("CORONARY HEART DISEASE RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            parent = st.checkbox("Parent/sibling with heart disease")
            diabetes = st.checkbox("Diagnosed with Diabetes")
            sedentary = st.checkbox("Sedentary lifestyle (>6 hrs/day)")
            bp = st.checkbox("High Blood Pressure")
        
        with col2:
            cholesterol = st.checkbox("High Cholesterol")
            age = st.checkbox("Male > 45 or Female > 55")
            smoker = st.checkbox("Active Smoker")

        score = sum([
            2 if parent else 0,
            1 if diabetes else 0,
            1 if sedentary else 0,
            1 if bp else 0,
            2 if cholesterol else 0,
            1 if age else 0,
            2 if smoker else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="heart_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genetic risk factors detected for coronary heart disease. Continue cardiovascular health practices.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate polygenic risk profile. Implement preventive strategies and regular cardiac screenings.")
                else:
                    result_box("High", score, "🚨 Elevated genomic risk markers identified. Seek comprehensive cardiovascular evaluation.")

    # Asthma
    elif disease == 'Asthma':
        section_header("ASTHMA RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            parent = st.checkbox("Parent/sibling with asthma")
            allergies = st.checkbox("Allergies to dust, pollen, etc.")
            pollution = st.checkbox("Live in high pollution area")
        
        with col2:
            infection = st.checkbox("Childhood respiratory infections")
            obesity = st.checkbox("Obesity")

        score = sum([
            2 if parent else 0,
            1 if allergies else 0,
            1 if pollution else 0,
            1 if infection else 0,
            1 if obesity else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="asthma_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic susceptibility to asthma detected. Maintain respiratory health awareness.")
                elif score < 5:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition identified. Monitor respiratory symptoms regularly.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors present. Consult with a pulmonologist for evaluation.")

    # Depression
    elif disease == 'Depression':
        section_header("DEPRESSION RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            family = st.checkbox("Family history of depression")
            stress = st.checkbox("Chronic stress or trauma")
            sleep = st.checkbox("Sleep disturbances")
        
        with col2:
            sedentary = st.checkbox("Sedentary lifestyle (>6 hrs/day)")
            female = st.checkbox("Female")
            substances = st.checkbox("Use of tobacco, alcohol, or drugs")

        score = sum([
            2 if family else 0,
            2 if stress else 0,
            1 if sleep else 0,
            1 if sedentary else 0,
            1 if female else 0,
            1 if substances else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="depression_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genetic risk factors for depression. Maintain mental wellness practices.")
                elif score < 5:
                    result_box("Moderate", score, "⚠️ Moderate genomic predisposition detected. Prioritize mental health awareness.")
                else:
                    result_box("High", score, "🚨 Significant genetic susceptibility identified. Seek professional mental health support.")

    # Breast Cancer
    elif disease == 'Breast Cancer':
        section_header("BREAST CANCER RISK ASSESSMENT (FEMALES)")
        col1, col2 = st.columns(2)
        
        with col1:
            family = st.checkbox("Mother/sister with breast cancer")
            menstruation = st.checkbox("Early menstruation (<12) or late menopause (>55)")
            alcohol = st.checkbox("Alcohol consumption")
        
        with col2:
            obesity = st.checkbox("Obesity")
            brca = st.checkbox("BRCA gene family history")
            childbirth = st.checkbox("No childbirth or after age 30")

        score = sum([
            3 if family else 0,
            1 if menstruation else 0,
            1 if alcohol else 0,
            1 if obesity else 0,
            3 if brca else 0,
            1 if childbirth else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="breast_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic risk profile for breast cancer. Continue regular screenings.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Increase surveillance frequency.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk factors present. Consult with an oncologist for personalized management.")

    # Prostate Cancer
    elif disease == 'Prostate Cancer':
        section_header("PROSTATE CANCER RISK ASSESSMENT (MALES)")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.checkbox("Age above 50")
            parent = st.checkbox("Father/brother with prostate cancer")
        
        with col2:
            ancestry = st.checkbox("African ancestry")
            urine = st.checkbox("Urinary symptoms (weak stream, frequent urination)")

        score = sum([
            1 if age else 0,
            3 if parent else 0,
            2 if ancestry else 0,
            1 if urine else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="prostate_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genetic risk factors for prostate cancer. Maintain regular screenings.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genomic predisposition detected. Increase surveillance frequency.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk profile. Consult with a urologist for comprehensive evaluation.")

    # Hypertension
    elif disease == 'Hypertension':
        section_header("HYPERTENSION RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            parent = st.checkbox("Parent/sibling with high BP")
            bmi = st.checkbox("BMI > 30")
            salt = st.checkbox("High-salt diet")
        
        with col2:
            stress = st.checkbox("Frequent stress or anxiety")
            exercise = st.checkbox("Exercise less than 3 times/week")
            age = st.checkbox("Age over 45")

        score = sum([
            2 if parent else 0,
            2 if bmi else 0,
            1 if salt else 0,
            1 if stress else 0,
            1 if exercise else 0,
            1 if age else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="hypertension_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic risk for hypertension. Maintain cardiovascular health practices.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Monitor blood pressure regularly.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors identified. Implement preventive strategies with medical guidance.")

    # Osteoporosis
    elif disease == 'Osteoporosis':
        section_header("OSTEOPOROSIS RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.checkbox("Female above age 50")
            family = st.checkbox("Family history of osteoporosis or fractures")
            calcium = st.checkbox("Low calcium or vitamin D intake")
        
        with col2:
            alcohol = st.checkbox("Regular smoking or alcohol use")
            inactive = st.checkbox("Physically inactive")
            menopause = st.checkbox("Early menopause (before 45)")

        score = sum([
            2 if age else 0,
            2 if family else 0,
            1 if calcium else 0,
            1 if alcohol else 0,
            1 if inactive else 0,
            1 if menopause else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="osteoporosis_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genetic risk for osteoporosis. Maintain bone health through nutrition and exercise.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genomic predisposition detected. Consider bone density screening.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk profile. Consult with an endocrinologist for comprehensive bone health management.")

    # COPD
    elif disease == 'COPD':
        section_header("COPD RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            smoke = st.checkbox("Current or past smoker")
            pollution = st.checkbox("Exposure to air pollution or dust")
        
        with col2:
            cough = st.checkbox("Chronic cough or shortness of breath")
            family = st.checkbox("Family history of lung disease")

        score = sum([
            3 if smoke else 0,
            2 if pollution else 0,
            1 if cough else 0,
            1 if family else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="copd_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic susceptibility to COPD. Maintain respiratory health awareness.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Monitor respiratory symptoms.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors present. Consult with a pulmonologist for evaluation.")

    # Cervical Cancer
    elif disease == 'Cervical Cancer':
        section_header("CERVICAL CANCER RISK ASSESSMENT (FEMALES)")
        col1, col2 = st.columns(2)
        
        with col1:
            vaccine = st.checkbox("Received HPV vaccine")
            partners = st.checkbox("Multiple sexual partners")
        
        with col2:
            smoke = st.checkbox("Smoker")
            pap = st.checkbox("Abnormal Pap smear history")
            age = st.checkbox("Over age 30 and not regularly screened")

        score = 0
        if vaccine: score -= 1
        if partners: score += 1
        if smoke: score += 1
        if pap: score += 2
        if age: score += 1

        if st.button("🧬 CALCULATE RISK", key="cervical_btn"):
            if check_name():
                if score <= 0:
                    result_box("Low", score, "✅ Minimal genomic risk for cervical cancer. Continue regular screenings.")
                elif score < 3:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Increase surveillance frequency.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk profile. Consult with a gynecologist for comprehensive evaluation.")

    # Thyroid Disorders
    elif disease == 'Thyroid Disorders':
        section_header("THYROID DISORDERS RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            family = st.checkbox("Family history of thyroid problems")
            female = st.checkbox("Female")
        
        with col2:
            symptoms = st.checkbox("Fatigue, weight changes, or mood swings")
            autoimmune = st.checkbox("Other autoimmune condition (e.g., diabetes, lupus)")
            surgery = st.checkbox("Thyroid surgery or radiation exposure")

        score = sum([
            2 if family else 0,
            1 if female else 0,
            1 if symptoms else 0,
            1 if autoimmune else 0,
            1 if surgery else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="thyroid_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic risk for thyroid disorders. Maintain regular check-ups.")
                elif score < 5:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Monitor thyroid function.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors present. Consult with an endocrinologist for evaluation.")

    # Lung Cancer
    elif disease == 'Lung Cancer':
        section_header("LUNG CANCER RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            smoke = st.checkbox("Current or past smoker")
            exposure = st.checkbox("Exposed to secondhand smoke or radon")
        
        with col2:
            family = st.checkbox("Family history of lung cancer")
            age = st.checkbox("Over age 50")

        score = sum([
            3 if smoke else 0,
            2 if exposure else 0,
            1 if family else 0,
            1 if age else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="lung_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genomic risk for lung cancer. Avoid tobacco and environmental carcinogens.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Consider low-dose CT screening.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk profile. Consult with an oncologist for comprehensive evaluation.")

    # Stroke
    elif disease == 'Stroke':
        section_header("STROKE RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            bp = st.checkbox("High blood pressure")
            diabetes = st.checkbox("Diabetes or heart disease")
        
        with col2:
            smoke = st.checkbox("Smoker")
            age = st.checkbox("Over age 55")
            family = st.checkbox("Family history of stroke")

        score = sum([
            2 if bp else 0,
            2 if diabetes else 0,
            1 if smoke else 0,
            1 if age else 0,
            1 if family else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="stroke_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Low genomic risk for stroke. Maintain cardiovascular health practices.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Implement stroke prevention strategies.")
                else:
                    result_box("High", score, "🚨 Significant genetic risk factors identified. Consult with a neurologist for comprehensive evaluation.")

    # Liver Disease
    elif disease == 'Liver Disease':
        section_header("LIVER DISEASE RISK ASSESSMENT")
        col1, col2 = st.columns(2)
        
        with col1:
            alcohol = st.checkbox("Regular alcohol consumption (>2 drinks/day)")
            obese = st.checkbox("Overweight or obese")
        
        with col2:
            diabetes = st.checkbox("Diabetes or high cholesterol")
            hepatitis = st.checkbox("Diagnosed with hepatitis B or C")
            meds = st.checkbox("Medications affecting liver")

        score = sum([
            2 if alcohol else 0,
            2 if obese else 0,
            1 if diabetes else 0,
            2 if hepatitis else 0,
            1 if meds else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="liver_btn"):
            if check_name():
                if score <= 2:
                    result_box("Low", score, "✅ Minimal genomic risk for liver disease. Maintain liver health through lifestyle.")
                elif score < 6:
                    result_box("Moderate", score, "⚠️ Moderate genetic predisposition detected. Monitor liver enzymes regularly.")
                else:
                    result_box("High", score, "🚨 Elevated genetic risk profile. Consult with a hepatologist for comprehensive evaluation.")

    # PCOD
    elif disease == 'PCOD':
        section_header("PCOD RISK ASSESSMENT")
        
        st.markdown("##### 🧬 MENSTRUAL IRREGULARITIES")
        col1, col2 = st.columns(2)
        with col1:
            A1 = st.checkbox("Irregular cycles (<8/year)")
        with col2:
            A2 = st.checkbox("Periods >7 days or >35 days apart")
            A3 = st.checkbox("No menstruation for 3+ months")
        
        st.markdown("##### 🧬 HYPERANDROGENISM")
        col1, col2 = st.columns(2)
        with col1:
            B1 = st.checkbox("Excess facial/body hair")
            B2 = st.checkbox("Frequent acne or oily skin")
        with col2:
            B3 = st.checkbox("Hair thinning or male-pattern baldness")
            B4 = st.checkbox("Hair removal more than once/week")
        
        st.markdown("##### 🧬 METABOLIC SYMPTOMS")
        col1, col2 = st.columns(2)
        with col1:
            C1 = st.checkbox("Overweight/obese (BMI > 25)")
            C2 = st.checkbox("Difficulty losing weight")
        with col2:
            C3 = st.checkbox("Sugar cravings/fatigue after eating")
            C4 = st.checkbox("Insulin resistance or prediabetes")
        
        st.markdown("##### 🧬 REPRODUCTIVE HEALTH")
        col1, col2 = st.columns(2)
        with col1:
            D1 = st.checkbox("Difficulty getting pregnant (1+ year)")
        with col2:
            D2 = st.checkbox("Infertility diagnosis/treatment")
        
        st.markdown("##### 🧬 EMOTIONAL SYMPTOMS")
        col1, col2 = st.columns(2)
        with col1:
            E1 = st.checkbox("Mood swings, anxiety, or depression")
        with col2:
            E2 = st.checkbox("Self-conscious about symptoms")

        score = sum([
            2 if A1 else 0, 1 if A2 else 0, 2 if A3 else 0,
            2 if B1 else 0, 1 if B2 else 0, 1 if B3 else 0, 1 if B4 else 0,
            2 if C1 else 0, 1 if C2 else 0, 1 if C3 else 0, 2 if C4 else 0,
            2 if D1 else 0, 1 if D2 else 0,
            1 if E1 else 0, 1 if E2 else 0
        ])

        if st.button("🧬 CALCULATE RISK", key="pcod_btn"):
            if check_name():
                if score <= 4:
                    result_box("Low", score, "✅ Minimal indicators for PCOD in your genomic profile. Maintain hormonal balance through lifestyle.")
                elif score < 9:
                    result_box("Moderate", score, "⚠️ Moderate risk markers detected. Consider endocrine evaluation and metabolic screening.")
                else:
                    result_box("High", score, "🚨 Strong genomic predisposition to PCOD. Consult with an endocrinologist for comprehensive management.")

# Footer with DNA animation
if st.button("Back to Home", key="back_to_home", on_click=lambda: st.session_state.update({"open_assessments": {}, "patient_info_complete": False, "form_errors": {}}) ):
    switch_page("home")
st.markdown("---")
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
         