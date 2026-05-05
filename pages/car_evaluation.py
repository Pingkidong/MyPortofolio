import streamlit as st
import joblib
import pandas as pd

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.back-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    color: #c9a96e;
    font-size: 0.88rem;
    cursor: pointer;
    margin-bottom: 2rem;
    text-decoration: none;
}

.proj-header {
    margin-bottom: 2.5rem;
}

.proj-badge {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    background: rgba(126,184,164,0.15);
    color: #7eb8a4;
    border: 1px solid rgba(126,184,164,0.3);
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}

.proj-title {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: #e8e3db;
    margin-bottom: 0.6rem;
}

.proj-subtitle {
    color: #6b6560;
    font-size: 1rem;
    max-width: 600px;
}

.divider {
    border: none;
    border-top: 1px solid #1f2937;
    margin: 2rem 0;
}

.section-label {
    font-size: 0.75rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #c9a96e;
    margin-bottom: 1rem;
    font-weight: 500;
}

.section-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: #e8e3db;
    margin-bottom: 1rem;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
}

.info-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 1rem 1.2rem;
}

.info-card-label {
    font-size: 0.75rem;
    color: #4b5563;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}

.info-card-value {
    font-size: 1rem;
    color: #e8e3db;
    font-weight: 500;
}

.tech-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin: 1rem 0;
}

.tech-tag {
    padding: 0.3rem 0.85rem;
    border-radius: 6px;
    background: #1e1e2e;
    border: 1px solid #2a2a3a;
    color: #a09890;
    font-size: 0.82rem;
    font-family: 'DM Mono', monospace;
}

.step-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.2rem;
    align-items: flex-start;
}

.step-num {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(201,169,110,0.15);
    border: 1px solid #c9a96e;
    color: #c9a96e;
    font-size: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 0.15rem;
}

.step-text {
    color: #9ca3af;
    font-size: 0.93rem;
    line-height: 1.7;
}

.step-text strong { color: #e8e3db; }

.predict-section {
    background: #0d1117;
    border: 1px solid #1f2937;
    border-radius: 16px;
    padding: 2rem 2rem;
    margin-top: 1rem;
}

.result-box {
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    margin-top: 1.5rem;
}

.result-box.sell {
    background: rgba(126,184,164,0.08);
    border: 1px solid rgba(126,184,164,0.3);
}

.result-box.review {
    background: rgba(224,184,112,0.08);
    border: 1px solid rgba(224,184,112,0.3);
}

.result-box.repair {
    background: rgba(224,112,112,0.08);
    border: 1px solid rgba(224,112,112,0.3);
}

.result-emoji { font-size: 2.5rem; margin-bottom: 0.5rem; }

.result-status {
    font-family: 'Playfair Display', serif;
    font-size: 1.4rem;
    margin-bottom: 0.4rem;
}

.result-status.sell  { color: #7eb8a4; }
.result-status.review { color: #e0b870; }
.result-status.repair { color: #e07070; }

.result-desc { color: #6b6560; font-size: 0.88rem; }

.prob-bar-wrap { margin-top: 1rem; }
.prob-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.8rem;
    color: #6b6560;
    margin-bottom: 0.3rem;
}
.prob-bar-bg {
    background: #1f2937;
    border-radius: 999px;
    height: 8px;
    overflow: hidden;
}
.prob-bar-fill {
    height: 100%;
    border-radius: 999px;
    transition: width 0.6s ease;
}
</style>
""", unsafe_allow_html=True)


# BACK BUTTON 
if st.button("← Kembali ke Portfolio", key="back"):
    st.switch_page("pages/home.py")

# HEADER 
st.markdown("""
<div class="proj-header">
  <div class="proj-badge">ML Classification Project</div>
  <div class="proj-title">Car Spec Evaluator</div>
  <div class="proj-subtitle">
  A classification model that evaluates car specifications and determines whether the combination meets an acceptable standard, built end-to-end ML workflow from EDA to deployment.
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

# SECTION 1 — PROJECT OVERVIEW

st.markdown('<div class="section-label">Section 01</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Project Overview</div>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["🎯 Problem", "🔍 Approach", "🛠️ Build Process", "📊 Results"])

with tab1:
    st.markdown("""

    #### Overview
    Not all cars are built equal. With so many spec combinations available in the market, it can be hard to tell whether a particular configuration is genuinely worth considering. This tool evaluates a car's specification objectively based on purchase price, maintenance cost, number of doors, seating capacity, luggage space, and safety rating. It tells you whether the overall combination meets an acceptable standard.

    #### Model Performance
    - Trained on 1,594 real car specification combinations
    - SMOTE applied on training set only to prevent data leakage
    - Zero false negatives, every acceptable spec was correctly identified
    - Only 4 misclassifications out of 319 test samples
    - Safety rating and seating capacity are the most decisive features

    #### Real-World Impact
    - Quickly screen whether a car's spec combination meets acceptable standards
    - Useful for comparing two car options before making a final decision
    - Identifies spec combinations that are objectively weak regardless of brand
    - Safety and capacity are the most decisive factors in the evaluation
    - Backed by 1,594 real spec combinations with 98.75% accuracy
    """)

with tab2:
    st.markdown("""
    #### Business-Driven Metric
    Since the goal is accurate spec evaluation, the model is optimized for overall accuracy rather than favoring a specific class. A balanced 0.50 threshold is used. If the acceptable probability exceeds 50%, the spec combination is classified 
    as acceptable. This ensures the model focuses on correctly identifying both acceptable and unacceptable combinations, which is crucial for providing reliable recommendations to users.

    #### Imbalanced Data
    The dataset has an imbalanced class distribution (~90% unacceptable vs ~1-% acceptable). 
    Without handling this, the model would be biased toward the majority class. 
    **SMOTE** (Synthetic Minority Over-sampling Technique) was applied on the training 
    set only to avoid data leakage.
    """)

with tab3:
    st.markdown("""<div style='height:0.5rem'></div>""", unsafe_allow_html=True)
    steps = [
        ("Exploratory Data Analysis", "Analyzed feature distributions, checked for missing values, visualized class imbalance, and computed VIF for multicollinearity."),
        ("Encoding", "Manual ordinal encoding following semantic order (low → med → high → vhigh) to preserve category rankings."),
        ("Train-Test Split", "80/20 split with random_state=42 for reproducibility."),
        ("SMOTE Oversampling", "Applied only on the training set (sampling_strategy=0.5) to prevent data leakage."),
        ("Model Training", "Gradient Boosting Classifier selected for its ability to handle ordinal features and non-linear interactions."),
        ("Pipeline Export", "Model exported as .pkl using joblib for Streamlit deployment."),
    ]

    for i, (title, desc) in enumerate(steps, 1):
        st.markdown(f"""
        <div class="step-row">
          <div class="step-num">{i}</div>
          <div class="step-text"><strong>{title}</strong><br/>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("""<div style='height:0.5rem'></div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="info-grid">
      <div class="info-card">
        <div class="info-card-label">Train Accuracy</div>
        <div class="info-card-value">99.14%</div>
      </div>
      <div class="info-card">
        <div class="info-card-label">Test Accuracy</div>
        <div class="info-card-value">98.75%</div>
      </div>
      <div class="info-card">
        <div class="info-card-label">Precision (ACC)</div>
        <div class="info-card-value">0.94</div>
      </div>
      <div class="info-card">
        <div class="info-card-label">Recall (ACC)</div>
        <div class="info-card-value">1.00</div>
      </div>
      <div class="info-card">
        <div class="info-card-label">False Positive (Test)</div>
        <div class="info-card-value">4 kasus</div>
      </div>
      <div class="info-card">
        <div class="info-card-label">False Negative (Test)</div>
        <div class="info-card-value">0 kasus</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tech-list">
      <span class="tech-tag">Python 3.x</span>
      <span class="tech-tag">Scikit-learn</span>
      <span class="tech-tag">imbalanced-learn</span>
      <span class="tech-tag">Pandas</span>
      <span class="tech-tag">Joblib</span>
      <span class="tech-tag">Streamlit</span>
      <span class="tech-tag">GradientBoostingClassifier</span>
      <span class="tech-tag">SMOTE</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<hr class="divider"/>', unsafe_allow_html=True)



# SECTION 2 — PREDICTION

st.markdown('<div class="section-label">Section 02</div>', unsafe_allow_html=True)
st.markdown('<div class="section-heading">Try the Model</div>', unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load('car/car_model.pkl')

try:
    model = load_model()
    model_loaded = True
except:
    model_loaded = False
    st.warning("⚠️ `car_model.pkl` tidak ditemukan. Jalankan `pipeline_export.py` dulu ya.")

# st.markdown('<div class="predict-section">', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    buying   = st.selectbox("Price",       ['low', 'med', 'high', 'vhigh'])
    maint    = st.selectbox("Maintenance Cost",   ['low', 'med', 'high', 'vhigh'])
    doors    = st.selectbox("Number of Doors",      [2, 4, 6])
with col2:
    persons  = st.selectbox("Person Capacity",   [2, 3, 4, 5,  6])
    lug_boot = st.selectbox("Luggage Boot Size",     ['small', 'med', 'big'])
    safety   = st.selectbox("Safety Level",  ['low', 'med', 'high', 'vhigh'])



if st.button("🔍 Predict", use_container_width=True, type="primary", disabled=not model_loaded):

    low_high  = {'low': 0, 'med': 1, 'high': 2, 'vhigh': 3}
    small_big = {'small': 0, 'med': 1, 'big': 2}

    input_data = pd.DataFrame([{
        'buying':   low_high[buying],
        'maint':    low_high[maint],
        'doors':    doors,
        'persons':  persons,
        'lug_boot': small_big[lug_boot],
        'safety':   low_high[safety],
    }])


    # st.write("Input:", input_data)
    
    THRESHOLD   = 0.50
    prob_acc    = model.predict_proba(input_data)[0][1]
    prob_nonacc = 1 - prob_acc

    if prob_acc >= THRESHOLD:
        cls, emoji, status, desc = (
            "sell", "✅", "Acceptable",
            f"This car scores {prob_acc:.1%}. It meets the acceptability threshold and looks like a solid buy."
        )

    else:
        cls, emoji, status, desc = (
            "repair", "🔧", "Not Recommended",
            f"This car only scores {prob_acc:.1%}. Based on the given specs, it does not meet the acceptability standard."
        )

    # INI harus di dalam if st.button, jangan di luar
    st.markdown(f"""
    <div class="result-box {cls}">
      <div class="result-emoji">{emoji}</div>
      <div class="result-status {cls}">{status}</div>
      <div class="result-desc">{desc}</div>
    </div>
    """, unsafe_allow_html=True)

    # st.write("Prob:", model.predict_proba(input_data))


    # st.write("Prob:", model.predict_proba(input_data))

    # st.markdown(f"""
    # <div class="prob-bar-wrap" style="margin-top:1.5rem">
    #   <div class="prob-label"><span>Acceptable Probability</span><span>{prob_acc:.1%}</span></div>
    #   <div class="prob-bar-bg">
    #     <div class="prob-bar-fill" style="width:{prob_acc*100:.1f}%; background:#7eb8a4;"></div>
    #   </div>
    # </div>
    # <div class="prob-bar-wrap" style="margin-top:0.8rem">
    #   <div class="prob-label"><span>Not Acceptable Probability</span><span>{prob_nonacc:.1%}</span></div>
    #   <div class="prob-bar-bg">
    #     <div class="prob-bar-fill" style="width:{prob_nonacc*100:.1f}%; background:#e07070;"></div>
    #   </div>
    # </div>
    # """, unsafe_allow_html=True)

