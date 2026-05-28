import streamlit as st
from PIL import Image
import base64, io

# CSS Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.hero {
    display: flex;
    align-items: center;
    gap: 2.5rem;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 16px;
    margin-bottom: 2rem;
}

.hero-photo {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    object-fit: cover;
    border: 3px solid #c9a96e;
    flex-shrink: 0;
}

.hero-photo-placeholder {
    width: 130px;
    height: 130px;
    border-radius: 50%;
    background: #2a2a4a;
    border: 3px solid #c9a96e;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3rem;
    flex-shrink: 0;
}

.hero-name {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: #e8e3db;
    margin-bottom: 0.3rem;
}

.hero-role {
    font-size: 1rem;
    color: #c9a96e;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}

.hero-bio {
    font-size: 0.95rem;
    color: #a09890;
    line-height: 1.7;
    max-width: 520px;
    margin-bottom: 1.2rem;
}

.socials {
    display: flex;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.social-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.07);
    color: #e8e3db;
    font-size: 0.82rem;
    text-decoration: none;
    border: 1px solid rgba(255,255,255,0.12);
    transition: background 0.2s;
}

.social-pill:hover {
    background: rgba(201,169,110,0.2);
    border-color: #c9a96e;
    color: #c9a96e;
}

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    color: #e8e3db;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #2a2a2a;
}

.skills-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 2.5rem;
}

.skill-tag {
    padding: 0.3rem 0.85rem;
    border-radius: 6px;
    background: #1e1e2e;
    border: 1px solid #2a2a3a;
    color: #a09890;
    font-size: 0.82rem;
    font-family: 'DM Mono', monospace;
}

.card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
    display: flex;
    flex-direction: column;
    height: 100%;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #c9a96e;
}

.card-img {
    width: 100%;
    height: 180px;
    object-fit: cover;
    background: #1a2332;
    flex-shrink: 0;
}

.card-img-placeholder {
    width: 100%;
    height: 180px;
    background: linear-gradient(135deg, #1a2332, #0f3460);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 3.5rem;
    flex-shrink: 0;
}

.card-body {
    padding: 1.2rem 1.4rem 1.4rem;
    
}

.card-badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: rgba(126,184,164,0.15);
    color: #7eb8a4;
    border: 1px solid rgba(126,184,164,0.3);
    margin-bottom: 0.7rem;
}

.card-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: #e8e3db;
    margin-bottom: 0.5rem;
}

.card-desc {
    font-size: 0.87rem;
    color: #7a7570;
    line-height: 1.6;
    margin-bottom: 1rem;
    flex-grow: 1;
}

.card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 1rem;
}

.card-tag {
    font-size: 0.75rem;
    padding: 0.15rem 0.6rem;
    border-radius: 4px;
    background: #1e1e2e;
    color: #5a5560;
    font-family: 'DM Mono', monospace;
}

/* Force equal height columns */
[data-testid="column"] {
    display: flex;
    flex-direction: column;
}

[data-testid="column"] > div:first-child {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}
</style>
""", unsafe_allow_html=True)


# PROFILE 
try:
    img = Image.open("asset/foto.jpeg")
    buf = io.BytesIO()
    img.save(buf, format="JPEG")
    b64 = base64.b64encode(buf.getvalue()).decode()
    photo_html = f'<img src="data:image/jpeg;base64,{b64}" class="hero-photo"/>'
except:
    photo_html = '<div class="hero-photo-placeholder">👤</div>'

st.markdown(f"""
<div class="hero">
  {photo_html}
  <div>
    <div class="hero-name">Silvia Naada Kamilia</div>
    <div class="hero-role">Data Enthusiast</div>
    <div class="hero-bio">
      I am a passionate data enthusiast with a strong foundation in Python and data analysis. I enjoy exploring datasets, building predictive models, and sharing insights through interactive applications.
    </div>
    <div class="socials">
      <a class="social-pill" href="mailto:silvia.kamilia55@gmail.com">✉️ silvia.kamilia55@gmail.com</a>
      <a class="social-pill" href="https://github.com/Pingkidong" target="_blank">🐙 GitHub</a>
      <a class="social-pill" href="https://www.linkedin.com/in/silvia-kamilia-profile/" target="_blank">💼 LinkedIn</a>
      <a class="social-pill" href="https://instagram.com/slvnkm_" target="_blank">📸 Instagram</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# TECH STACK 
st.markdown('<div class="section-title">Tech Stack</div>', unsafe_allow_html=True)
st.markdown("""
<div class="skills-row">
  <span class="skill-tag">Python</span>
  <span class="skill-tag">Scikit-learn</span>
  <span class="skill-tag">Pandas</span>
  <span class="skill-tag">NumPy</span>
  <span class="skill-tag">Matplotlib</span>
  <span class="skill-tag">Seaborn</span>
  <span class="skill-tag">Streamlit</span>
  <span class="skill-tag">Tableau</span>
  <span class="skill-tag">Jupyter Notebook</span>
  <span class="skill-tag">Visual Studio Code</span>
  <span class="skill-tag">Looker Studio</span>
  <span class="skill-tag">MySQL</span>
</div>
""", unsafe_allow_html=True)


# PROJECTS ──
st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

# Load images
def load_img_b64(path, fmt="JPEG"):
    try:
        img = Image.open(path)
        buf = io.BytesIO()
        img.save(buf, format=fmt)
        return base64.b64encode(buf.getvalue()).decode()
    except:
        return None

b64_market = load_img_b64("asset/market.jpg")
b64_mobil  = load_img_b64("asset/mobil.jpg")

card_img_walmart = (
    f'<img src="data:image/jpeg;base64,{b64_market}" class="card-img"/>'
    if b64_market else
    '<div class="card-img-placeholder">📊</div>'
)

card_img_car = (
    f'<img src="data:image/jpeg;base64,{b64_mobil}" class="card-img"/>'
    if b64_mobil else
    '<div class="card-img-placeholder">🚗</div>'
)

col1, col2, col3 = st.columns([1, 1, 1])

# Project 1: Walmart ──
with col1:
    st.markdown(f"""
    <div class="card">
      {card_img_walmart}
      <div class="card-body">
        <div class="card-badge">Data Analysis</div>
        <div class="card-title">Diagnosing a Q4 Sales Anomaly Before Peak Season</div>
        <div class="card-desc">
          During routine Q4 weekly monitoring, sales in weeks 42–43 of 2012 were flagged as tracking below the same period in 2011.
        </div>
        <div class="card-tags" style="display:flex; flex-direction:column; gap:0.5rem;">
        <div style="display:flex; align-items:center; gap:0.4rem; flex-wrap:wrap;">
            <span style="font-size:0.72rem; color:#5a5560;">Tools:</span>
            <span class="card-tag">Python</span>
            <span class="card-tag">Tableau</span>
        </div>
        <div style="display:flex; align-items:center; gap:0.4rem; flex-wrap:wrap;">
            <span style="font-size:0.72rem; color:#5a5560;">Techniques:</span>
            <span class="card-tag">EDA</span>
            <span class="card-tag">Visualization</span>
        </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
    if st.button("Lihat Project →", key="btn_ws", use_container_width=True):
        st.switch_page("pages/decline_sales.py")

# Project 2: Car Spec ──
with col2:
    st.markdown(f"""
    <div class="card">
      {card_img_car}
      <div class="card-body">
        <div class="card-badge">Classification</div>
        <div class="card-title">Car Spec Evaluator</div>
        <div class="card-desc">
          A classification model that evaluates car specifications and determines whether the combination meets an acceptable standard, built end-to-end ML workflow from EDA to deployment.
        </div>
        <div class="card-tags" style="display:flex; flex-direction:column; gap:0.5rem;">
          <div style="display:flex; align-items:center; gap:0.4rem; flex-wrap:wrap;">
            <span style="font-size:0.72rem; color:#5a5560;">Tools:</span>
            <span class="card-tag">VS Code</span>
          </div>
          <div style="display:flex; align-items:center; gap:0.4rem; flex-wrap:wrap;">
            <span style="font-size:0.72rem; color:#5a5560;">Techniques:</span>
            <span class="card-tag">EDA</span>
            <span class="card-tag">SMOTE</span>
            <span class="card-tag">GradientBoosting</span>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
    if st.button("Lihat Project →", key="btn_car", use_container_width=True):
        st.switch_page("pages/car_evaluation.py")
