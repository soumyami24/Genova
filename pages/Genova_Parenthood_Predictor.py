import streamlit as st
import re
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page


# Initialize scores
score = score_b = score_f = score_l = score_e = score_total = 0
genetic_max, rh_max = 30, 10
fertility_max, lifestyle_max, emotions_max = 25, 15, 15

# 🧬 Genova DNA Theme Configuration
st.set_page_config(
    page_title="Genova Parenthood Predictor", 
    page_icon="🧬",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
""", unsafe_allow_html=True)
# Custom DNA-inspired CSS
def inject_dna_theme():
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Exo+2:wght@300;400;600;700&display=swap');
    
    :root {{
        --dna-primary: #00f3ff;
        --dna-secondary: #7d12ff;
        --dna-tertiary: #00ff9d;
        --dna-dark: #0a0e17;
        --dna-card: rgba(19, 28, 46, 0.8);
        --dna-border: rgba(0, 243, 255, 0.3);
    }}
    
    * {{
        font-family: 'Exo 2', sans-serif;
    }}
    
    body {{
        background: linear-gradient(135deg, var(--dna-dark) 0%, #0c1220 100%);
        color: #e0f7ff;
    }}
    
    .stApp {{
        background-image: 
            radial-gradient(circle at 10% 20%, rgba(0, 243, 255, 0.05) 0%, transparent 15%),
            radial-gradient(circle at 90% 80%, rgba(125, 18, 255, 0.05) 0%, transparent 15%);
        background-attachment: fixed;
    }}
    
    .genova-header {{
        text-align: center;
        padding: 1rem 0 2rem;
        position: relative;
    }}
    
    .feature-intro {{
        margin: 4rem 0 2rem;
        font-size: 1.3rem;
        text-align: center;
        color: var(--dna-tertiary);
        position: relative;
    }}
    
    .genova-title {{
        font-size: 3rem;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
        background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }}
    
    .genova-tagline {{
    color: var(--dna-tertiary);
    font-size: 1.2rem;
    text-transform: uppercase;
    letter-spacing: 3px;
    margin-bottom: 1.5rem;
    font-weight: 300;
    position: relative;
    display: inline-block;
}}

.genova-tagline::after {{
    content: "";
    position: absolute;
    bottom: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--dna-primary), transparent);
}}
    
    .genova-description {{
        font-size: 1.15rem;
        line-height: 1.8;
        max-width: 800px;
        margin: 2rem auto;
        text-align: center;
        color: #b0e0ee;
        font-weight: 300;
    }}
    .dna-highlight {{
    background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 600;
}}
    
    .dna-section {{
        background: linear-gradient(135deg, rgba(19, 28, 46, 0.8) 0%, rgba(10, 14, 23, 0.8) 100%);
        color: #e0f7ff;
        border-radius: 16px;
        border: 1px solid var(--dna-border);
        padding: 1.5rem;
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        transition: all 0.4s ease;
    }}

    .dna-section:hover {{
        border-color: rgba(0, 243, 255, 0.5);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 243, 255, 0.15);
    }}
    
    .stButton > button {{
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
    }}
    
    .stButton > button::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 0%;
        height: 100%;
        background: linear-gradient(90deg, var(--dna-primary) 0%, var(--dna-tertiary) 100%);
        transition: all 0.4s ease;
        z-index: -1;
    }}
    
    .stButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0, 243, 255, 0.4);
    }}
    
    .stButton > button:hover::before {{
        width: 100%;
    }}
    
    .stTextInput>div>div>input,
    .stSelectbox>div>div>select,
    .stNumberInput>div>div>input,
    .stSlider>div>div>div>div {{
        background-color: var(--dna-card) !important;
        color: #e0f7ff !important;
        border: 1px solid var(--dna-border) !important;
        border-radius: 12px !important;
        padding: 0.75rem 1rem !important;
    }}
    
    .stCheckbox>label {{
        color: #e0f7ff !important;
        background: rgba(19, 28, 46, 0.5);
        padding: 0.8rem 1.2rem;
        border-radius: 12px;
        border-left: 3px solid var(--dna-tertiary);
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }}
    
    .stCheckbox>label:hover {{
        background: rgba(19, 28, 46, 0.7);
        transform: translateX(5px);
    }}
    
    .stCheckbox>input:checked + label {{
        border-left-color: var(--dna-primary);
        background: rgba(0, 243, 255, 0.1);
    }}
    
    .dna-result {{
        padding: 1.5rem;
        border-radius: 16px;
        background: rgba(10, 14, 23, 0.7);
        border-left: 5px solid var(--dna-primary);
        margin: 1.5rem 0;
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.1);
    }}
    
    .dna-footer {{
        text-align: center;
        font-size: 0.9rem;
        color: #6a89a7;
        margin-top: 5rem;
        padding-top: 2rem;
        position: relative;
    }}
    
    .dna-footer::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 200px;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(0, 243, 255, 0.3), transparent);
    }}
    
    .dna-icon {{
        display: inline-block;
        margin: 0 5px;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0% {{ opacity: 0.7; transform: scale(1); }}
        50% {{ opacity: 1; transform: scale(1.1); }}
        100% {{ opacity: 0.7; transform: scale(1); }}
    }}
    
    .dna-divider {{
        height: 3px;
        background: linear-gradient(90deg, transparent, var(--dna-primary), transparent);
        border: none;
        margin: 2rem 0;
    }}
    
    .dna-helix {{
        display: flex;
        justify-content: center;
        margin: 2rem 0;
    }}
    
    .dna-helix svg {{
        width: 80px;
        height: 80px;
        opacity: 0.7;
    }}
    
    .section-header {{
        font-size: 1.8rem;
        padding: 12px 20px;
        border-radius: 12px;
        background: linear-gradient(90deg, rgba(0,243,255,0.1) 0%, rgba(125,18,255,0.1) 100%);
        margin: 30px 0 20px 0;
        border-left: 4px solid var(--dna-primary);
    }}
    
    .compatibility-score {{
        background: linear-gradient(135deg, rgba(0, 243, 255, 0.1), rgba(125, 18, 255, 0.1));
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(0, 243, 255, 0.3);
        margin: 1rem 0;
        text-align: center;
    }}
    
    .score-value {{
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }}
    
    .partner-card {{
        display: flex;
        gap: 32px;
        justify-content: center;
        align-items: center;
        background: rgba(166,220,239,0.10);
        border-radius: 16px;
        border: 1.5px solid #A6DCEF77;
        padding: 18px 32px;
        margin: 18px 0 28px 0;
        box-shadow: 0 2px 12px rgba(166,220,239,0.07);
    }}
    
    .recommendation-box {{
        background-color: #2D2D34;
        padding: 1em;
        border-left: 5px solid #A6DCEF;
        border-radius: 10px;
        margin: 1rem 0;
    }}
    
    .warning-box {{
        background-color: #332E31;
        padding: 1em;
        border-left: 5px solid #FF6584;
        border-radius: 10px;
        margin: 1rem 0;
    }}
    </style>
    """, unsafe_allow_html=True)

inject_dna_theme()

# 🌌 App Header with DNA Theme
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
    Genova Parenthood Predictor
</div>
""", unsafe_allow_html=True)

# 📊 Main Content Layout
main_col, sidebar_col = st.columns([8, 4])

with main_col:
    # 👨‍👩‍👧‍👦 Partner Information Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">👫 BASIC INFORMATION</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 👨 Male Partner")
        name_male = st.text_input("Full Name", key="name_male")
        age_male = st.number_input("Age", min_value=18, max_value=80, key="age_male", value=30)
        
    with col2:
        st.markdown("#### 👩 Female Partner")
        name_female = st.text_input("Full Name", key="name_female")
        age_female = st.number_input("Age", min_value=18, max_value=80, key="age_female", value=30)
    
    st.markdown('<div class="dna-divider"></div>', unsafe_allow_html=True)
    
    trying = st.selectbox("Are you currently trying to conceive?", ['Select...', 'Yes', 'No'], key="trying")
    had_children = st.selectbox("Have either of you had children before?", ['Select...', 'Yes', 'No'], key="had_children")
    
    st.markdown("</div>", unsafe_allow_html=True)

    # 🧬 Genetic Compatibility Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">🧬 GENETIC HISTORY</div>
    """, unsafe_allow_html=True)
    
    p_genetic = st.selectbox("Known genetic condition in either partner?", 
                           ['Select...', 'None', 'Self', 'Partner', 'Both'])
    f_genetic = st.selectbox("Family history of inherited disorders?", 
                           ['Select...', 'Yes both partners side', 'Yes but only from one side', 'None'])
    
    st.markdown("</div>", unsafe_allow_html=True)

    # 🩸 Blood Group Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">🩸 BLOOD COMPATIBILITY</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Male")
        bg_male = st.selectbox("Blood Group:", ['Select...', 'A', 'B', 'O', 'AB'], key="bg_male")
        rh_male = st.selectbox("Rh factor:", ['Select...', 'Positive', 'Negative'], key="rh_male")
        
    with col2:
        st.markdown("#### Female")
        bg_female = st.selectbox("Blood Group:", ['Select...', 'A', 'B', 'O', 'AB'], key="bg_female")
        rh_female = st.selectbox("Rh factor:", ['Select...', 'Positive', 'Negative'], key="rh_female")
    
    st.markdown("</div>", unsafe_allow_html=True)

    # 🌱 Fertility Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">🌱 FERTILITY HEALTH</div>
    """, unsafe_allow_html=True)
    
    concieve = st.selectbox("Experienced difficulty conceiving?", ['Select...', 'Yes', 'No'])
    col1, col2 = st.columns(2)
    with col1:
        infertility_issue = st.selectbox("Female fertility issues:", 
                                      ['Select...', 'None', 'PCOS', 'PCOD', 'Blocked Fallopian tubes', 
                                       'Endometriosis', 'Hormonal Imbalance', 'Other'])
    with col2:
        infertility_issue2 = st.selectbox("Male fertility issues:", 
                                       ['Select...', 'None', 'Low Sperm Count', 'Poor quality sperm', 
                                        'Blockages', 'Hormonal Imbalance', 'Other'])
    
    menstrual_cycles = st.selectbox("Are menstrual cycles regular?", ['Select...', 'Yes', 'No'])
    fertility_treatment = st.selectbox("Undergone fertility treatments?", ['Select...', 'Yes', 'No'])
    
    st.markdown("</div>", unsafe_allow_html=True)

    # ⚡ Lifestyle Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">⚡ LIFESTYLE FACTORS</div>
    """, unsafe_allow_html=True)
    
    smoke = st.selectbox("Smoking or vaping habits?", ['Select...', 'None', 'Both', 'Self', 'Partner'])
    alcohol = st.selectbox("Alcohol consumption?", ['Select...', 'Never', 'Occasionally', 'Weekly', 'Daily'])
    diet = st.selectbox("Diet quality?", ['Select...', 'Poor', 'Average', 'Balanced', 'Excellent'])
    med = st.selectbox("Regular supplements or medications?", ['Select...', 'Yes', 'No'])
    sleep = st.number_input("Average hours of sleep per day?", min_value=1, max_value=24, value=7)
    pollution = st.selectbox("Exposure to pollution or high-stress lifestyle?", ['Select...', 'Yes', 'No'])
    part = st.selectbox("Would you say your partner's lifestyle feels health-conscious?", ['Select...', 'Yes', 'No'])
    
    st.markdown("</div>", unsafe_allow_html=True)

    # 💞 Emotional Compatibility Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">💞 EMOTIONAL CONNECTION</div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        y_believe = st.selectbox("Your parenting style:", [
            'Select...',
            'A. Clear rules with consistent consequences',
            'B. Letting children explore freely',
            'C. Strict discipline and high expectations'
        ])
        
        parenting = st.selectbox("Parenting decisions are usually made:", [
            'Select...',
            'A. We discuss and decide together',
            'B. One of us usually decides',
            'C. We often disagree or avoid',
            'D. We have not discussed it yet'
        ])
        
        stress = st.selectbox("Your stress response:", [
            'Select...',
            'A. Stay calm and talk it through',
            'B. Handle it myself',
            'C. Get overwhelmed and withdraw',
            'D. React emotionally and need space'
        ])
        
    with col2:
        p_believe = st.selectbox("Partner's parenting style:", [
            'Select...',
            'A. Clear rules with consistent consequences',
            'B. Letting children explore freely',
            'C. Strict discipline and high expectations'
        ])
        
        partner = st.selectbox("When stressed, partner responds by:", [
            'Select...',
            'A. Listening and supporting me',
            'B. Trying to help but not always understanding',
            'C. Often not noticing or responding',
            'D. I prefer not to share stress'
        ])
        
        disagree = st.selectbox("Conflict resolution style:", [
            'Select...',
            'A. Talk it out calmly',
            'B. One gives in to avoid conflict',
            'C. Argue and take time to resolve',
            'D. Avoid the topic altogether'
        ])
    
    connect = st.slider("Daily emotional connection (1-5):", 1, 5, 3)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # 📬 Submission Section
    st.markdown("""
    <div class="dna-section">
        <div class="section-header">📬 SHARE YOUR DETAILS</div>
    """, unsafe_allow_html=True)
    
    consent = st.checkbox("I consent to genetic compatibility analysis", key="consent")
    email_sent = st.checkbox("Share E-mail for further updates", key="email_sent")
    email = st.text_input("E-mail address", key="email")
    
    submit = st.button("Generate Compatibility Report", key="submit", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

with sidebar_col:
    with st.container():
        st.markdown("""
            <h4 style="
                background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
                font-weight: 700;
            ">⚠️ NON-DIAGNOSTIC DISCLAIMER</h4>
            <div class="dna-section" style="color: #e0f7ff;">
                This tool simulates couple compatibility scoring and does not replace clinical evaluation. 
                Results should be interpreted as informational only, not as medical advice.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <h4 style="
                background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
                font-weight: 700;
            ">🔬 ABOUT GENOVA PARENTHOOD PREDICTOR</h4>
            <div class="dna-section" style="color: #e0f7ff;">
                Advanced AI-driven compatibility analysis across genetic, lifestyle, and emotional dimensions. 
                Our algorithm evaluates 50+ factors to predict relationship synergy and reproductive wellness.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <h4 style="
                background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
                font-weight: 700;
            ">🔧 HOW TO USE</h4>
            <div class="dna-section" style="color: #e0f7ff;">
                
          Start Filling : Begin by entering details for yourself and your partner</li>
          
          Tell everything : Tell us about your genetic history,medical information,daily habits. These help paint a fuller wellness picture.</li>
          
          Receive Your Score : You’ll get a Couple Compatibility Score based on your answers.</li>
          
        </ul>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <h4 style="
                background: linear-gradient(90deg, var(--dna-primary), var(--dna-tertiary));
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0.5rem;
                font-weight: 700;
            ">🔍 HOW IS THIS CALCULATED?</h4>
            <div class="dna-section" style="color: #e0f7ff;">
                <p>Your compatibility scores are based on a multi-factor framework.
        <p>Genetic Health Overview : 30 points
        <p>
        <p> Blood Group Compatibility : 10 points
        <p> 
        <p>Fertility : 25 points
        <p>
        <p>Lifestyle & Environment Compatibility : 15 points
        <p>
        <p>Mental & Emotional Alignment : 15 points
        <p>
        <p>Genova Compatibility Score  : [(Sum of values scored by you)/(Sum of maximum values)]*100
        <p>
        </div>
        """, unsafe_allow_html=True)
            
# Validation and Scoring Logic
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

if submit:
    select_fields = [
        trying, had_children, p_genetic, f_genetic,
        bg_male, rh_male, bg_female, rh_female,
        concieve, infertility_issue, infertility_issue2, menstrual_cycles, fertility_treatment,
        smoke, alcohol, diet, med, pollution, part,
        y_believe, p_believe, parenting, partner, disagree, stress
    ]

    if any(field == 'Select...' for field in select_fields):
        st.error("❌ Please make a selection for all dropdown fields.")
    elif not all([name_male.strip(), name_female.strip(), email.strip()]):
        st.error("❌ Please fill in all required text fields.")
    elif not is_valid_email(email):
        st.error("❌ Invalid email format. Please enter a valid email (e.g., name@example.com).")
    elif not consent or not email_sent:
        st.error("❌ Consent and email agreement are required to proceed.")
    elif connect < 1 or sleep < 1:
        st.error("❌ Please provide valid numeric inputs for emotional connection and sleep.")
    else:
        st.success("✅ All inputs are valid. Your Genova Report is ready!")
        st.markdown("---")
        
        # Calculate scores
        # Genetic Compatibility
        if p_genetic == 'None': score += 20
        elif p_genetic in ['Self', 'Partner']: score += 12
        elif p_genetic == 'Both': score += 2
        
        if f_genetic == 'None': score += 10
        elif f_genetic == 'Yes but only from one side': score += 6
        elif f_genetic == 'Yes both partners side': score += 0.1
        
        # Blood Compatibility
        if rh_male == 'Positive' and rh_female == 'Negative': score_b += 0.6
        elif rh_female == 'Positive' and rh_male == 'Negative': score_b += 6
        elif rh_male == 'Positive' and rh_female == 'Positive': score_b += 6
        elif rh_male == 'Negative' and rh_female == 'Negative': score_b += 6
        
        if bg_male in ['A', 'B', 'AB'] and bg_female == 'O': score_b += 0.4
        else: score_b += 4
        
        # Fertility
        if concieve == 'Yes': score_f += 0.4
        elif concieve == 'No': score_f += 4
        
        if infertility_issue in ['PCOS', 'PCOD', 'Blocked Fallopian tubes', 'Endometriosis', 'Hormonal Imbalance', 'Other']: score_f += 0.5
        elif infertility_issue == 'None': score_f += 5
        
        if infertility_issue2 in ['Low Sperm Count', 'Poor quality sperm', 'Blockages', 'Hormonal Imbalance', 'Other']: score_f += 0.5
        elif infertility_issue2 == 'None': score_f += 5
        
        if menstrual_cycles == 'Yes': score_f += 6
        elif menstrual_cycles == 'No': score_f += 0.6
        
        if fertility_treatment == 'Yes': score_f += 0.5
        elif fertility_treatment == 'No': score_f += 5
        
        # Lifestyle
        if smoke == 'None': score_l += 3
        elif smoke in ['Self', 'Partner']: score_l += 1.7
        elif smoke == 'Both': score_l += 0.3
        
        if alcohol == 'Never': score_l += 3
        elif alcohol == 'Occasionally': score_l += 2.3
        elif alcohol == 'Weekly': score_l += 1.3
        elif alcohol == 'Daily': score_l += 0.3
        
        if diet == 'Poor': score_l += 0.2
        elif diet == 'Average': score_l += 0.8
        elif diet == 'Balanced': score_l += 1.4
        elif diet == 'Excellent': score_l += 2
        
        if med == 'No': score_l += 0.2
        elif med == 'Yes': score_l += 2
        
        if 1 <= sleep <= 5: score_l += 0.2
        elif 5 < sleep <= 7: score_l += 1
        elif sleep >= 8: score_l += 2
        
        if pollution == 'Yes': score_l += 0.2
        elif pollution == 'No': score_l += 2
        
        if part == 'Yes': score_l += 1
        elif part == 'No': score_l += 0.1
        
        # Emotional
        if (y_believe == 'A. Clear rules with consistent consequences' and 
            p_believe == 'A. Clear rules with consistent consequences'): score_e += 3
        elif (y_believe == 'B. Letting children explore freely' and 
              p_believe == 'B. Letting children explore freely'): score_e += 3
        elif (y_believe == 'C. Strict discipline and high expectations' and 
              p_believe == 'C. Strict discipline and high expectations'): score_e += 3
        else: score_e += 0.3
        
        if parenting == 'A. We discuss and decide together': score_e += 3
        elif parenting == 'B. One of us usually decides': score_e += 2.1
        elif parenting == 'C. We often disagree or avoid': score_e += 1.2
        elif parenting == 'D. We have not discussed it yet': score_e += 0.3
        
        if partner == 'A. Listening and supporting me': score_e += 3
        elif partner == 'B. Trying to help but not always understanding': score_e += 2.1
        elif partner == 'C. Often not noticing or responding': score_e += 1.2
        elif partner == 'D. I prefer not to share stress': score_e += 0.3
        
        if stress == 'A. Stay calm and talk it through': score_e += 3
        elif stress == 'B. Handle it myself': score_e += 2.1
        elif stress == 'C. Get overwhelmed and withdraw': score_e += 1.2
        elif stress == 'D. React emotionally and need space': score_e += 0.3
        
        if 4 <= connect <= 5: score_e += 3
        elif 3 <= connect < 4: score_e += 2.1
        elif 2 <= connect < 3: score_e += 1.2
        elif 1 <= connect < 2: score_e += 0.3
        
        if disagree == 'A. Talk it out calmly': score_e += 3
        elif disagree == 'B. One gives in to avoid conflict': score_e += 2.1
        elif disagree == 'C. Argue and take time to resolve': score_e += 1.2
        elif disagree == 'D. Avoid the topic altogether': score_e += 0.3
        
        # Calculate total score
        score_total = score + score_b + score_f + score_l + score_e
        score_per = (score_total / 95) * 100
        
        # Display Results
        st.markdown("""
        <div class="section-header">
            🧬 Couple Compatibility Test Report
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f'''
        <div class="partner-card">
            <div style="text-align:center;">
                <div style="font-size:2.1rem;">👨</div>
                <div style="font-size:1.18rem; font-weight:600; color:#A6DCEF;">{name_male}</div>
                <div style="font-size:1rem; color:#EDEDED;">Age: {age_male}</div>
            </div>
            <div style="font-size:2.2rem; color:#A6DCEF;">&amp;</div>
            <div style="text-align:center;">
                <div style="font-size:2.1rem;">👩</div>
                <div style="font-size:1.18rem; font-weight:600; color:#A6DCEF;">{name_female}</div>
                <div style="font-size:1rem; color:#EDEDED;">Age: {age_female}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Final Score Display
        st.markdown(f"""
        <div class="compatibility-score">
            <h3>YOUR COMPATIBILITY SCORE</h3>
            <div class="score-value">{score_per:.1f}%</div>
            <p>Genetic • Lifestyle • Emotional Alignment</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Compatibility Outcomes
        if 95 <= score_per <= 100:
            st.success("✨ Genova Prime Match")
            st.markdown("""
            <div class="dna-section">
                This match reflects <strong>exceptional synergy</strong> across genetic wellness, lifestyle alignment, and emotional support.
                It forms a <strong>resilient foundation</strong> for healthy offspring and empowering parenting dynamics.
            </div>
            """, unsafe_allow_html=True)
        elif 80 <= score_per < 95:
            st.success("💞 Genova Strong Match")
            st.markdown("""
            <div class="dna-section">
                You show a <strong>high degree of compatibility</strong>, with minimal genetic risk and strong behavioral harmony.
                This pairing promotes <strong>reproductive health</strong> and shared wellness values.
            </div>
            """, unsafe_allow_html=True)
        elif 65 <= score_per < 80:
            st.info("🌻 Genova Vital Match")
            st.markdown("""
            <div class="dna-section">
                There's <strong>meaningful alignment</strong> across core relationship traits.
                Lifestyle or emotional differences may influence outcomes, but are <strong>manageable with collaborative effort</strong> and proactive planning.
            </div>
            """, unsafe_allow_html=True)
        elif 45 <= score_per < 65:
            st.info("🔆 Genova Moderate Match")
            st.markdown("""
            <div class="dna-section">
                Your match shows <strong>moderate compatibility</strong>, with visible differences in genetic or behavioral aspects.
                With support and clear communication, your pairing can be <strong>nurtured into long-term stability</strong>.
            </div>
            """, unsafe_allow_html=True)
        elif 30 <= score_per < 45:
            st.warning("⚠️ Genova Challenging Match")
            st.markdown("""
            <div class="dna-section">
                There are <strong>marked challenges</strong> that may impact child wellness or relational ease.
                Open dialogue and clinical guidance are advised for a <strong>balanced future</strong>.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("🚨 Genova Divergent Match")
            st.markdown("""
            <div class="dna-section">
                Significant divergences in genetic markers and lifestyle habits suggest <strong>elevated risks</strong> to shared health goals.
                This pairing may benefit from <strong>specialized medical consultation</strong> and a strong emotional commitment.
            </div>
            """, unsafe_allow_html=True)
        
        # Score Table
        st.markdown("""
        <div class="section-header">
            📊 Compatibility Breakdown
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="dna-section">
            <table style="width:100%; border-collapse: collapse; margin-top:20px;">
                <tr style="border-bottom: 1px solid rgba(0, 243, 255, 0.3);">
                    <th style="text-align:left; padding:10px; color:#00f3ff;">Section</th>
                    <th style="text-align:right; padding:10px; color:#00f3ff;">Score</th>
                </tr>
                <tr>
                    <td style="padding:10px;">🧪 Genetic Health</td>
                    <td style="text-align:right; padding:10px;">{score} / {genetic_max}</td>
                </tr>
                <tr>
                    <td style="padding:10px;">🩸 Blood Compatibility</td>
                    <td style="text-align:right; padding:10px;">{score_b} / {rh_max}</td>
                </tr>
                <tr>
                    <td style="padding:10px;">🌱 Fertility</td>
                    <td style="text-align:right; padding:10px;">{score_f} / {fertility_max}</td>
                </tr>
                <tr>
                    <td style="padding:10px;">⚡ Lifestyle</td>
                    <td style="text-align:right; padding:10px;">{score_l} / {lifestyle_max}</td>
                </tr>
                <tr>
                    <td style="padding:10px;">💞 Emotional</td>
                    <td style="text-align:right; padding:10px;">{score_e} / {emotions_max}</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
        # Section Recommendations
        st.markdown("""
        <div class="section-header">
            🔍 Detailed Recommendations
        </div>
        """, unsafe_allow_html=True)
        
        # Genetic Compatibility
        st.markdown("### 🧬 Genetic Compatibility")
        if score == 30:
            st.markdown("""
            <div class="dna-section">
                <div class="recommendation-box">
                ✅ <strong>Excellent compatibility</strong>: Low risk of hereditary disorders.<br>
                🔍 <em>Recommendation:</em> Routine prenatal screening advised.
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif 10 < score < 30:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ⚠️ <strong>Moderate concern</strong>: Family or partner risk detected.<br>
                🔍 <em>Recommendation:</em> Full-panel genetic screening & counseling.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ <strong>High concern</strong>: Inherited risk strongly suggested.<br>
                🔍 <em>Recommendation:</em> Genetic counselor guidance + PGT discussion recommended.
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Blood Compatibility
        st.markdown("### 🩸 Blood Compatibility")
        if rh_male == 'Positive' and rh_female == 'Negative':
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ Potential Rh incompatibility risk detected.<br>
                If the baby inherits Rh-positive blood, the mother's immune system may produce antibodies against fetal red cells.
                🔍 <em>Recommendation:</em> Rh immunoglobulin (RhoGAM) shots at 28 weeks and postpartum can prevent sensitization.
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif bg_male in ['A', 'B', 'AB'] and bg_female == 'O':
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ Mild ABO incompatibility potential.<br>
                Since the mother is type O and the father carries A, B, or AB, the baby may inherit a different antigen — potentially causing mild neonatal jaundice.
                🔍 <em>Recommendation:</em> Postnatal monitoring of bilirubin levels; no prenatal intervention required.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dna-section">
                <div class="recommendation-box">
                ✅ Blood types are biologically compatible.<br>
                🔍 <em>Recommendation:</em> Follow standard prenatal checkups.
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Fertility
        st.markdown("### 🌱 Fertility Health")
        if score_f == 25:
            st.markdown("""
            <div class="dna-section">
                <div class="recommendation-box">
                ✅ <strong>Fertility Health</strong>: No current concerns; natural conception likely.<br>
                🔍 <em>Recommendation:</em> Continue regular checkups and healthy routine.
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif 15 < score_f < 25:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ⚠️ <strong>Moderate concern</strong>: Potential factors affecting success rates.<br>
                🔍 <em>Recommendation:</em> Fertility evaluation may offer clarity.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ <strong>High concern</strong>: Fertility challenges suggested.<br>
                🔍 <em>Recommendation:</em> Early expert support may improve outcomes (IVF, ART).
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Lifestyle
        st.markdown("### ⚡ Lifestyle Factors")
        if score_l >= 13:
            st.markdown("""
            <div class="dna-section">
                <div class="recommendation-box">
                ✅ <strong>Healthy lifestyle</strong>: Habits support fertility and well-being.<br>
                🔍 <em>Recommendation:</em> Stay consistent — sleep, nutrition, and stress balance matter.
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif 7 <= score_l < 13:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ⚠️ <strong>Mixed lifestyle habits</strong>: Consider sleep, diet, and stress optimization.<br>
                🔍 <em>Recommendation:</em> Wellness guidance could strengthen overall health.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ <strong>Lifestyle concerns</strong>: Habits may be affecting preconception health.<br>
                🔍 <em>Recommendation:</em> Consult a lifestyle physician or health coach.
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Emotional
        st.markdown("### 💞 Emotional Connection")
        if score_e >= 20:
            st.markdown("""
            <div class="dna-section">
                <div class="recommendation-box">
                ✅ <strong>Emotional harmony</strong>: Support, empathy, and connection appear strong.<br>
                🔍 <em>Recommendation:</em> Deepen intimacy through rituals and shared experiences.
                </div>
            </div>
            """, unsafe_allow_html=True)
        elif 10 <= score_e < 20:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ⚠️ <strong>Partial alignment</strong>: Room for better communication and emotional safety.<br>
                🔍 <em>Recommendation:</em> Consider couple reflection or therapy to build trust.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="dna-section">
                <div class="warning-box">
                ❗ <strong>Emotional disconnect</strong>: Challenges may affect relationship wellness.<br>
                🔍 <em>Recommendation:</em> Professional support is encouraged to strengthen your bond.
                </div>
            </div>
            """, unsafe_allow_html=True)
if st.button("Back to Home", key="back_to_home", on_click=lambda: st.session_state.update({"open_assessments": {}, "patient_info_complete": False, "form_errors": {}}) ):
    switch_page("home")
# Footer with DNA animation
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
