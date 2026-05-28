import streamlit as st

# CSS — same design system
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500&family=DM+Mono:wght@400&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

.proj-header { margin-bottom: 2.5rem; }

.proj-badge {
    display: inline-block;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    background: rgba(201,169,110,0.15);
    color: #c9a96e;
    border: 1px solid rgba(201,169,110,0.3);
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
    max-width: 650px;
    line-height: 1.7;
}

.divider {
    border: none;
    border-top: 1px solid #1f2937;
    margin: 2rem 0;
}

.info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
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

.info-card-value.down { color: #e07070; }
.info-card-value.up   { color: #7eb8a4; }

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

.finding-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    display: flex;
    gap: 0.8rem;
    align-items: flex-start;
}

.finding-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 0.1rem; }

.finding-text {
    font-size: 0.9rem;
    color: #9ca3af;
    line-height: 1.6;
}

.finding-text strong { color: #e8e3db; }

.limitation-box {
    background: rgba(201,169,110,0.05);
    border: 1px solid rgba(201,169,110,0.2);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-size: 0.88rem;
    color: #9ca3af;
    line-height: 1.7;
    margin-top: 1rem;
}

.limitation-box strong { color: #c9a96e; }

.ext-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
    margin-top: 0.5rem;
}

.ext-table th {
    font-size: 0.72rem;
    font-weight: 500;
    color: #4b5563;
    text-align: left;
    padding: 0.5rem 0.8rem;
    border-bottom: 1px solid #1f2937;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

.ext-table td {
    padding: 0.7rem 0.8rem;
    border-bottom: 1px solid #111827;
    color: #9ca3af;
    vertical-align: middle;
}

.ext-table tr:last-child td { border-bottom: none; }

.verdict {
    font-size: 0.72rem;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    font-weight: 500;
    white-space: nowrap;
}

.type-tag {
    font-size: 0.72rem;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    font-weight: 500;
    white-space: nowrap;
}

.verdict-out  { background: rgba(224,112,112,0.1); color: #c9a96e; }
.verdict-bg   { background: rgba(201,169,110,0.1); color: #c9a96e; }

.int  { background: rgba(224, 112, 112, 0.1); color: #e07070; }
.string   { background: rgba(201, 169, 110, 0.1); color: #c9a96e; }
.float  { background: rgba(74, 144, 226, 0.1); color: #4a90e2; }
.bool   { background: rgba(46, 204, 113, 0.1); color: #2ecc71; }

.rec-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-left: 3px solid #c9a96e;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
}

.rec-title {
    font-size: 0.88rem;
    font-weight: 500;
    color: #e8e3db;
    margin-bottom: 0.3rem;
}

.rec-desc {
    font-size: 0.83rem;
    color: #6b6560;
    line-height: 1.6;
}

.tableau-embed {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    margin-top: 0.5rem;
    margin-bottom: 1rem;
}

.tableau-label {
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4b5563;
    margin-bottom: 0.5rem;
}

.tableau-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.1rem;
    color: #e8e3db;
    margin-bottom: 0.3rem;
}

.tableau-sub {
    font-size: 0.82rem;
    color: #6b6560;
}

.context-box {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: #9ca3af;
    line-height: 1.7;
}

.context-box strong { color: #e8e3db; }

.justification-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1rem;
    align-items: flex-start;
}

.just-icon {
    font-size: 1.4rem;
    flex-shrink: 0;
    margin-top: 0.1rem;
}

.just-text {
    font-size: 0.9rem;
    color: #9ca3af;
    line-height: 1.7;
}

.just-text strong { color: #e8e3db; }

.just-title {
    font-size: 0.95rem;
    font-weight: 600;
    color: #e8e3db;
    margin-bottom: 0.25rem;
}

.interp-box {
    background: #111827;
    border: 1px solid #1f2937;
    border-left: 2px solid #374151;
    border-radius: 0 10px 10px 0;
    padding: 0.8rem 1rem;
    font-size: 0.88rem;
    color: #9ca3af;
    line-height: 1.6;
    margin-top: 0.8rem;
    margin-bottom: 0.8rem;
}
 
.interp-box strong { color: #e8e3db; }
 
.step-inv-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 1.5rem 0 0.8rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid #1f2937;
}

.step-inv-badge {
    width: 26px;
    height: 26px;
    border-radius: 50%;
    background: rgba(201,169,110,0.1);
    border: 1px solid rgba(201,169,110,0.3);
    color: #c9a96e;
    font-size: 0.78rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
 
.step-inv-label {
    font-size: 0.95rem;
    font-weight: 500;
    color: #e8e3db;
    flex: 1;
}

.step-inv-q {
    font-size: 0.78rem;
    color: #4b5563;
    font-style: italic;
}

.md-compare {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
    margin-top: 0.5rem;
}
 
.md-compare th {
    font-size: 0.72rem;
    color: #4b5563;
    text-align: left;
    padding: 0.4rem 0.7rem;
    border-bottom: 1px solid #1f2937;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
 
.md-compare td {
    padding: 0.6rem 0.7rem;
    border-bottom: 1px solid #111827;
    color: #9ca3af;
}
 
.md-compare tr:last-child td {
    color: #e8e3db;
    font-weight: 500;
    border-bottom: none;
}
 
.dept-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0.8rem;
    background: #111827;
    border-radius: 8px;
    margin-bottom: 0.4rem;
    font-size: 0.85rem;
}
 
.dept-name { color: #e8e3db; font-weight: 500; }
.dept-decline { color: #e07070; font-family: 'DM Mono', monospace; font-size: 0.82rem; }
.dept-note { color: #4b5563; font-size: 0.78rem; }
.priority-badge {
    font-size: 0.7rem;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    background: rgba(224,112,112,0.1);
    color: #e07070;
    margin-left: 6px;
}
 
.summary-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
    margin-top: 1rem;
}
 
.summary-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 1rem 1.2rem;
}
 
.summary-title {
    font-size: 0.88rem;
    font-weight: 500;
    color: #e8e3db;
    margin: 0 0 4px;
}
 
.summary-desc {
    font-size: 0.8rem;
    color: #6b6560;
    line-height: 1.5;
    margin: 0;
}
</style>
""", unsafe_allow_html=True)


# BACK BUTTON 
if st.button("← Kembali ke Portfolio", key="back"):
    st.switch_page("pages/home.py")


# HEADER 
st.markdown("""
<div class="proj-header">
  <div class="proj-badge">Data Analysis Project</div>
  <div class="proj-title">Diagnosing a Q4 Sales Anomaly Before Peak Season</div>
  <div class="proj-subtitle">
    During routine Q4 weekly monitoring, sales in weeks 42–43 of 2012 were flagged as tracking below the same period in 2011, an unusual pattern ahead of peak holiday season. This analysis investigates the root cause and identifies where corrective action is needed before Thanksgiving and Christmas.
  </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<hr class="divider"/>', unsafe_allow_html=True)


# 5 TABS 
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Problem & Dataset",
    "🔍 Approach",
    "🐍 Analytical Findings",
    "📊 Business Dashboard",
    "✅ Conclusion & Recommendation",
])



# TAB 1 — Problem & Dataset

with tab1:

    st.markdown("#### Business Context")
    st.markdown("""
    <div class="context-box">
        Walmart operates 45 retail stores across the United States and conducts routine weekly sales monitoring throughout Q4 (the most critical quarter of the retail calendar). During the week 42–43 monitoring cycle of Q4 2012, the analytics team flagged an anomaly: sales were tracking below the same weeks in 2011, an unusual pattern given that Q4 typically shows YoY growth driven by holiday demand buildup ahead of Thanksgiving and Christmas. With peak season approaching, management needed to determine whether this dip was an isolated fluctuation or an early signal of a broader demand problem, and whether corrective action was needed before the holiday rush.
    </div>
    
    """, unsafe_allow_html=True)
    # try:
    #     st.image("asset/q4_ws.png", use_container_width=True)
    # except:
    #     st.info("📌 Tambahkan screenshot grafic ke folder asset/ dengan nama q4_ws.png")

    st.markdown("#### Business Questions")
    questions = [
        "Is the week 42–43 decline statistically meaningful or within normal variation?",
        "Which stores are driving the underperformance and is it isolated to specific store types?",
        "Is the decline caused by external macroeconomic conditions, promotional strategy, or weaker organic demand?",
        "Which departments should be prioritized for recovery before peak season?"
    ]
    for i, q in enumerate(questions, 1):
        st.markdown(f"""
        <div class="step-row">
          <div class="step-num">{i}</div>
          <div class="step-text">{q}</div>
        </div>
        """, unsafe_allow_html=True)

    # st.markdown("#### Snapshot: Week 42–43 YoY Comparison")
    # st.markdown("""
    # <div class="info-grid">
    #   <div class="info-card">
    #     <div class="info-card-label">Total Sales W42–43, 2011</div>
    #     <div class="info-card-value">$91,674,774</div>
    #   </div>
    #   <div class="info-card">
    #     <div class="info-card-label">Total Sales W42–43, 2012</div>
    #     <div class="info-card-value">$90,666,527</div>
    #   </div>
    #   <div class="info-card">
    #     <div class="info-card-label">Decline</div>
    #     <div class="info-card-value down">−$1,008,247</div>
    #   </div>
    #   <div class="info-card">
    #     <div class="info-card-label">YoY Decline</div>
    #     <div class="info-card-value down">−1.10%</div>
    #   </div>
    # </div>
    # """, unsafe_allow_html=True)

    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

    st.markdown("#### Dataset")
    st.markdown("""
    <div class="info-grid">
    <div class="info-card">
        <div class="info-card-label">Source</div>
        <div class="info-card-value" style="font-size:14px">
            <a href="https://www.kaggle.com/datasets/manjeetsingh/retaildataset/data" 
            target="_blank" style="color:#c9a96e;text-decoration:none;">Kaggle ↗</a>
        </div>
        <div class="info-card-label">Retail Data Analytics</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Stores</div>
        <div class="info-card-value">45 stores</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Period</div>
        <div class="info-card-value">2010–2012</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Total Rows (Sales)</div>
        <div class="info-card-value">421,570</div>
        <div class="info-card-label">After merge</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Departments</div>
        <div class="info-card-value">99</div>
        <div class="info-card-label">Per store</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Tables</div>
        <div class="info-card-value">3</div>
        <div class="info-card-label">sales, stores, and features</div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# tabel 1 - sales data-set.csv

    st.markdown("""
    <div class="info-card-label">Table 1 — sales data-set.csv</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <table class="ext-table">
      <thead>
        <tr>
          <th>Column</th>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#e8e3db">Store</strong></td>
          <td><span class="type-tag int">int</span></td>
          <td>Store ID (1-45)</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Dept</strong></td>
          <td><span class="type-tag int">int</span></td>
          <td>Department number within the store (1–99). Each store has up to 99 departments representing different product categories
          </td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Date</strong></td>
          <td><span class="type-tag string">string</span></td>
          <td>Week end date (Friday), format MM/DD/YYYY. Data is recorded weekly
          </td>
        </tr>
        <tr>
         <td><strong style="color:#e8e3db">Weekly_Sales</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Sales for the given department in the given store</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">IsHoliday</strong></td>
          <td><span class="type-tag bool">bool</span></td>
          <td>Whether the week contains a major US holiday: Super Bowl, Labor Day, Thanksgiving, or Christmas</td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

# Table 2 — stores data-set.csv

    st.markdown("""
    <div class="info-card-label">Table 2 — stores data-set.csv</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <table class="ext-table">
      <thead>
        <tr>
          <th>Column</th>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#e8e3db">Store</strong></td>
          <td><span class="type-tag int">int</span></td>
          <td>Store ID (1-45), join key to sales table</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Type</strong></td>
          <td><span class="type-tag string">string</span></td>
          <td>Store format category. Type A = largest, Type B = medium, Type C = smallest.
          </td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Size</strong></td>
          <td><span class="type-tag int">int</span></td>
          <td>Total store area in square feet. Directly correlates with store type, used as a continuous proxy for store capacity
          </td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

# Table 3 — Features data set.csv

    st.markdown("""
    <div class="info-card-label">Table 3 — Features data set.csv</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <table class="ext-table">
      <thead>
        <tr>
          <th>Column</th>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#e8e3db">Store</strong></td>
          <td><span class="type-tag int">int</span></td>
          <td>Store ID (1-45), join key</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Date</strong></td>
          <td><span class="type-tag string">string</span></td>
          <td>Week end date (Friday), format MM/DD/YYYY. Data is recorded weekly, join key.
          </td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Temperature</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Temperature in the store area (in Fahrenheit)</td>
        </tr>
        <tr>
         <td><strong style="color:#e8e3db">Fuel_Price</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Fuel price in the region (in USD per gallon)</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">MarkDown1-5</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Anonymized data related to promotional markdowns. MarkDown data is only available after Nov 2011, and is not available for all stores all the time. Any missing value is marked with an NA</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">CPI</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Consumer Price Index for the region</td>
        </tr>
        <tr>
         <td><strong style="color:#e8e3db">Unemployment</strong></td>
          <td><span class="type-tag float">float</span></td>
          <td>Unemployment rate in the region</td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">IsHoliday</strong></td>
          <td><span class="type-tag bool">bool</span></td>
          <td>Whether the week is a special holiday week</td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)

    # Store Type Breakdown
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.markdown("""
        <div style="background:#111827;border-radius:10px;padding:1rem 1.2rem;
                    border-left:3px solid #185FA5;height:100%">
        <div style="font-size:0.85rem;font-weight:500;color:#e8e3db;margin-bottom:6px;">Type A — Large</div>
        <div style="font-size:0.82rem;color:#6b6560;line-height:1.7;">
            22 stores<br>Highest revenue contributor
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div style="background:#111827;border-radius:10px;padding:1rem 1.2rem;
                    border-left:3px solid #1D9E75;height:100%">
        <div style="font-size:0.85rem;font-weight:500;color:#e8e3db;margin-bottom:6px;">Type B — Medium</div>
        <div style="font-size:0.82rem;color:#6b6560;line-height:1.7;">
            17 stores<br>Mid-range revenue
        </div>
        """, unsafe_allow_html=True)

    with col_c:
        st.markdown("""
        <div style="background:#111827;border-radius:10px;padding:1rem 1.2rem;
                    border-left:3px solid #4b5563;height:100%">
        <div style="font-size:0.85rem;font-weight:500;color:#e8e3db;margin-bottom:6px;">Type C — Small</div>
        <div style="font-size:0.82rem;color:#6b6560;line-height:1.7;">
            6 stores<br>Lowest revenue contributor
        </div>
        </div>
        """, unsafe_allow_html=True)    


    st.markdown("#### Tools & Technologies")
    st.markdown("""
    <div class="tech-list">
      <span class="tech-tag">Python</span>
      <span class="tech-tag">Pandas</span>
      <span class="tech-tag">Matplotlib</span>
      <span class="tech-tag">Seaborn</span>
      <span class="tech-tag">Tableau</span>
      <span class="tech-tag">Visual Studio Code</span>
    </div>
    """, unsafe_allow_html=True)


# TAB 2 — Pendekatan & Limitation

# with tab2:

    # st.markdown("#### Why YoY?")
    # st.markdown("""
    # <div class="justification-row">
    #   <div class="just-icon">📅</div>
    #   <div class="just-text">
    #     <div class="just-title">Retail punya seasonality yang kuat</div>
    #     Q4 selalu lebih tinggi dari Q3 karena holiday demand — bukan karena performa bisnis lebih baik.
    #     Kalau kita bandingkan Q4 vs Q3, hasilnya akan selalu menunjukkan kenaikan setiap tahun,
    #     sehingga tidak informatif untuk mendeteksi masalah.
    #   </div>
    # </div>
    # <div class="justification-row">
    #   <div class="just-icon">📊</div>
    #   <div class="just-text">
    #     <div class="just-title">YoY mengontrol efek musiman</div>
    #     Dengan membandingkan <strong>Q4 2012 vs Q4 2011</strong>, kita mengisolasi apakah bisnis
    #     benar-benar underperform relatif terhadap baseline yang comparable — bukan sekadar fluktuasi musiman biasa.
    #   </div>
    # </div>
    # """, unsafe_allow_html=True)

    # st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

    # st.markdown("#### Why YoY?")
    # st.markdown("""
    # <div class="context-box">
    #     Sales data is highly seasonal, Q4 always outperforms Q3 due to holiday demand, independent of actual business performance. Comparing Q4 2012 against Q3 2012 would show a decline every year regardless of what happened, making it meaningless for diagnosis. YoY comparison isolates whether the business genuinely underperformed by controlling for seasonality, weeks 42–43 of 2012 are measured against the same weeks in 2011, the most valid baseline available.
    # </div>
    # """, unsafe_allow_html=True)

    # st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

    # st.markdown("#### Investigation roadmap")
    # st.markdown("""
    # <div class="context-box">
    #     Inventory and operational data are not available in this dataset. If the root cause points toward stock issues or store-level execution problems, additional data from operations would be needed to confirm and act on those hypotheses.
    # </div>
    # """, unsafe_allow_html=True)

with tab2:
 
    st.markdown("""
    <div class="context-box">
        <strong>Why year-over-year (YoY)?</strong><br/>
        Sales data is highly seasonal, Q4 always outperforms Q3 due to holiday demand,
        independent of actual business performance. Comparing Q4 2012 against Q3 2012 would
        show a decline every year regardless of what happened, making it meaningless for
        diagnosis. YoY comparison isolates whether the business genuinely underperformed
        by controlling for seasonality, weeks 42–43 of 2012 are measured against the same
        weeks in 2011, the most valid baseline available.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
    st.markdown("#### Investigation Roadmap")
 
    steps = [
        ("Confirm the anomaly",
         "Compare weekly sales trend 2011 vs 2012 across weeks 40–43 to confirm the dip is specific to weeks 42–43, not a general Q4 pattern.",
         "Is the decline real and localized?"),
        ("Identify who is affected",
         "Break down the decline by store and store type to pinpoint which stores are driving the underperformance and whether it's isolated to a specific format.",
         "Which stores contributed most?"),
        ("Rule out external causes",
         "Analyze CPI, unemployment, fuel price, and temperature trends across weeks 40–43 for both years. Check correlation between external features and weekly sales to assess statistical relationship.",
         "Is macroeconomics to blame?"),
        ("Investigate promotional activity",
         "Compare MarkDown presence and value between 2011 and 2012 to determine whether the difference in promotional strategy explains the sales gap.",
         "Did promotions make a difference?"),
        ("Identify recovery opportunities",
         "Drill down to department level, find which departments contributed most to the decline and which have strong historical demand that can be targeted before peak season.",
         "Where should we act before Christmas?"),
    ]
 
    for i, (title, desc, q) in enumerate(steps, 1):
        st.markdown(f"""
        <div class="step-row">
          <div class="step-num">{i}</div>
          <div class="step-text">
            <strong>{title}</strong> — {desc}<br/>
            <span style="font-size:0.78rem;color:#4b5563;font-style:italic;">→ {q}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
    st.markdown("#### What Falls Outside This Investigation")
 
    limitations = [
        ("Inventory data", "Not available in this dataset. Hypotheses around stock shortages cannot be confirmed or ruled out without operational data."),
        ("Operational factors", "Staffing, store hours, and fulfillment rate are outside the dataset scope."),
        ("Competitor activity", "No data on promotional moves from Target, Costco, or other retailers in the same period."),
    ]
 
    for title, desc in limitations:
        st.markdown(f"""
        <div class="finding-card">
          <div class="finding-text">
            <strong>{title}</strong> — {desc}
          </div>
        </div>
        """, unsafe_allow_html=True)

# TAB 3 — Analytical Findings (Python)

# with tab3:

#     st.markdown("""
#     <div class="context-box">
#         Bagian ini menunjukkan <strong>proses investigasi analitik</strong> menggunakan Python —
#         bukan hasil akhir untuk stakeholder, tapi langkah-langkah yang dilakukan untuk
#         menemukan akar masalah. Setiap chart menjawab satu pertanyaan investigasi spesifik.
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("#### 🛠️ Langkah Investigasi")
#     steps = [
#         ("Data Preparation",
#          "Merge 3 tabel (sales, stores, features) menggunakan Store dan Date sebagai join key. Handle duplicate kolom IsHoliday post-merge. Tambah kolom year dan week dari datetime."),
#         ("Scope Definition",
#          "Filter ke Q4 2011 dan 2012, lalu sempitkan ke weeks 40–43 untuk perbandingan yang fair. Identifikasi weeks 42–43 sebagai window spesifik terjadinya underperformance."),
#         ("Store-Level Analysis",
#          "Identifikasi top stores berdasarkan nominal decline. Analisis apakah penurunan terkonsentrasi di store type tertentu (A, B, atau C)."),
#         ("External Factors Investigation",
#          "Analisis tren CPI, Unemployment, Fuel Price, dan Temperature di weeks 40–43 untuk kedua tahun guna menyingkirkan faktor makroekonomi."),
#         ("Promotional Analysis (MarkDown)",
#          "Bandingkan aktivitas markdown antara 2011 dan 2012. Temuan kunci: 100% null MarkDown di 2011 vs active promotions di 2012."),
#         ("Department-Level Analysis",
#          "Identifikasi top 10 departments berdasarkan nominal decline. Cross-reference dengan historical sales untuk menemukan kandidat recovery paling berdampak."),
#     ]
#     for i, (title, desc) in enumerate(steps, 1):
#         st.markdown(f"""
#         <div class="step-row">
#           <div class="step-num">{i}</div>
#           <div class="step-text"><strong>{title}</strong><br/>{desc}</div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

#     st.markdown("#### 🔑 Key Findings")
#     findings = [
#         ("📉", "Marginal decline, bukan structural breakdown.",
#          "Selisih total sales di weeks 42–43 hanya −$1.0M (−1.1%) dari 45 stores — dalam range variasi normal. Nyata tapi tidak dramatis."),
#         ("🏪", "Penurunan terkonsentrasi di Store Type A dan B.",
#          "Top 5 stores dengan nominal decline terbesar (Store 14, 11, 21, 20, 23) semuanya Type A atau B. Store 14 berkontribusi paling besar: −$771K (−19% YoY)."),
#         ("🏷️", "Promosi tidak mendorong gap.",
#          "Di weeks 42–43 tahun 2011, zero markdown activity tercatat — namun 2011 tetap outperform 2012 yang menjalankan active promotions. Ini mengindikasikan organic demand yang lebih lemah di 2012, bukan kurangnya upaya promosi."),
#         ("🌍", "External factors ruled out sebagai primary driver.",
#          "CPI, unemployment, fuel price, dan temperature diinvestigasi. Tidak ada yang menunjukkan pola yang memburuk spesifik di weeks 42–43. Unemployment bahkan lebih rendah di 2012 vs 2011."),
#         ("🔴", "Department 72 adalah prioritas recovery utama.",
#          "Ranking ke-4 terbesar secara historis (~$306M total revenue) tapi turun −22.8% di weeks 42–43 2012. Kombinasi demand historis tinggi dan penurunan tajam menjadikannya target paling actionable."),
#     ]
#     for icon, title, desc in findings:
#         st.markdown(f"""
#         <div class="finding-card">
#           <div class="finding-icon">{icon}</div>
#           <div class="finding-text">
#             <strong>{title}</strong> {desc}
#           </div>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown('<hr class="divider"/>', unsafe_allow_html=True)

#     st.markdown("#### 🌍 External Factors — Detail")
#     st.markdown("""
#     <table class="ext-table">
#       <thead>
#         <tr>
#           <th>Factor</th>
#           <th>2011 Avg</th>
#           <th>2012 Avg</th>
#           <th>Change</th>
#           <th>Pattern at Week 42–43</th>
#           <th>Verdict</th>
#         </tr>
#       </thead>
#       <tbody>
#         <tr>
#           <td><strong style="color:#e8e3db">CPI</strong></td>
#           <td>172.3</td>
#           <td>176.0</td>
#           <td>+2.1%</td>
#           <td>Flat — no spike at 42–43</td>
#           <td><span class="verdict verdict-out">Ruled out</span></td>
#         </tr>
#         <tr>
#           <td><strong style="color:#e8e3db">Unemployment</strong></td>
#           <td>7.8%</td>
#           <td>6.9%</td>
#           <td>−0.9%</td>
#           <td>2012 lebih rendah — improving</td>
#           <td><span class="verdict verdict-out">Ruled out</span></td>
#         </tr>
#         <tr>
#           <td><strong style="color:#e8e3db">Fuel Price</strong></td>
#           <td>$3.40</td>
#           <td>$3.80</td>
#           <td>+11.8%</td>
#           <td>Lebih tinggi tapi flat — no spike</td>
#           <td><span class="verdict verdict-bg">Background pressure</span></td>
#         </tr>
#         <tr>
#           <td><strong style="color:#e8e3db">Temperature</strong></td>
#           <td>62°F</td>
#           <td>63°F</td>
#           <td>+1°F</td>
#           <td>No consistent pattern</td>
#           <td><span class="verdict verdict-out">Ruled out</span></td>
#         </tr>
#         <tr>
#           <td><strong style="color:#e8e3db">Holiday Effect</strong></td>
#           <td>None</td>
#           <td>None</td>
#           <td>—</td>
#           <td>Both years: no holiday in W42–43</td>
#           <td><span class="verdict verdict-out">Ruled out</span></td>
#         </tr>
#       </tbody>
#     </table>
#     """, unsafe_allow_html=True)

with tab3:
 
    st.markdown("""
    <div class="context-box">
        This section shows the <strong>analytical investigation process</strong> using Python,
        step-by-step findings that answer each business question. Charts from the investigation
        are embedded alongside interpretations.
    </div>
    """, unsafe_allow_html=True)
 
    # STEP 1
    st.markdown("""
    <div class="step-inv-header">
      <div class="step-inv-badge">1</div>
      <span class="step-inv-label">Confirm the anomaly</span>
      <span class="step-inv-q">Is the decline real and localized?</span>
    </div>
    """, unsafe_allow_html=True)
 
    try:
        st.image("asset/q4_ws.png", use_container_width=True)
    except:
        st.info("📌 Tambahkan chart ke asset/q4_ws.png")
 
    st.markdown("""
    <div class="interp-box">
      <strong>Finding:</strong> Weeks 40–41 show 2012 performing comparably or above 2011.
      The gap only emerges at weeks 42–43, confirming the decline is localized, not a general Q4 pattern.
      Total difference: <strong>−$1.0M (−1.1%)</strong> across all 45 stores.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
 
    # STEP 2
    st.markdown("""
    <div class="step-inv-header">
      <div class="step-inv-badge">2</div>
      <span class="step-inv-label">Identify who is affected</span>
      <span class="step-inv-q">Which stores drove the underperformance?</span>
    </div>
    """, unsafe_allow_html=True)
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Top stores — nominal decline**")
        stores = [
            ("Store 14", "−$771K", "Type A · −19%"),
            ("Store 11", "−$203K", "Type A · −7.7%"),
            ("Store 21", "−$151K", "Type B · −10.3%"),
            ("Store 20", "−$139K", "Type A · −3.2%"),
            ("Store 23", "−$138K", "Type B · −4.7%"),
        ]
        for name, decline, note in stores:
            st.markdown(f"""
            <div class="dept-item">
              <span class="dept-name">{name}</span>
              <span class="dept-decline">{decline}</span>
              <span class="dept-note">{note}</span>
            </div>
            """, unsafe_allow_html=True)
 
    with col2:
        st.markdown("**Sales by store type — week 42–43**")
        types = [
            ("Type A", "$116.9M", "−1.55%", "#185FA5", 72),
            ("Type B", "$54.2M",  "−1.26%", "#1D9E75", 33),
            ("Type C", "$11.3M",  "+4.60%", "#888780", 7),
        ]
        for t, sales, pct, color, w in types:
            st.markdown(f"""
            <div class="dept-item" style="flex-direction:column;align-items:flex-start;gap:5px">
              <div style="display:flex;justify-content:space-between;width:100%">
                <span class="dept-name">{t}</span>
                <span style="font-size:0.82rem;color:#9ca3af">{sales} · {pct}</span>
              </div>
              <div style="width:100%;height:5px;background:#1f2937;border-radius:3px">
                <div style="width:{w}%;height:100%;background:{color};border-radius:3px"></div>
              </div>
            </div>
            """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="interp-box">
      <strong>Finding:</strong> Decline is concentrated in Type A and B stores.
      Type C actually grew +4.6%. Store 14 alone accounts for ~77% of the total nominal decline.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
 
    # STEP 3
    st.markdown("""
    <div class="step-inv-header">
      <div class="step-inv-badge">3</div>
      <span class="step-inv-label">Rule out external causes</span>
      <span class="step-inv-q">Is macroeconomics to blame?</span>
    </div>
    """, unsafe_allow_html=True)
 
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.image("asset/external.png", use_container_width=True)
        except:
            st.info("📌 Tambahkan chart ke asset/external.png")
    with col2:
        try:
            st.image("asset/corr.png", use_container_width=True)
        except:
            st.info("📌 Tambahkan chart ke asset/corr.png")
 
    st.markdown("""
    <table class="ext-table">
      <thead>
        <tr><th>Factor</th><th>2011 Avg</th><th>2012 Avg</th><th>Correlation vs Sales</th><th>Verdict</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#e8e3db">CPI</strong></td>
          <td>172.3</td><td>176.0</td><td>−0.02</td>
          <td><span class="verdict verdict-out">Ruled out</span></td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Unemployment</strong></td>
          <td>7.8%</td><td>6.9%</td><td>−0.03</td>
          <td><span class="verdict verdict-out">Ruled out</span></td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Fuel Price</strong></td>
          <td>$3.40</td><td>$3.80</td><td>−0.03</td>
          <td><span class="verdict verdict-bg">Background pressure</span></td>
        </tr>
        <tr>
          <td><strong style="color:#e8e3db">Temperature</strong></td>
          <td>62°F</td><td>63°F</td><td>−0.04</td>
          <td><span class="verdict verdict-out">Ruled out</span></td>
        </tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="interp-box">
      <strong>Finding:</strong> All external factors show near-zero correlation with weekly sales.
      None showed a pattern that specifically deteriorated at weeks 42–43.
      External causes are ruled out as the primary driver.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
 
    # STEP 4
    st.markdown("""
    <div class="step-inv-header">
      <div class="step-inv-badge">4</div>
      <span class="step-inv-label">Investigate promotional activity</span>
      <span class="step-inv-q">Did promotions make a difference?</span>
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <table class="md-compare">
      <thead>
        <tr><th>MarkDown</th><th>2011 (week 42–43)</th><th>2012 (week 42–43)</th><th>Observation</th></tr>
      </thead>
      <tbody>
        <tr><td>MarkDown1</td><td>100% missing</td><td>0.9% missing</td><td>Active in 2012</td></tr>
        <tr><td>MarkDown2</td><td>100% missing</td><td>49.9% missing</td><td>Partial in 2012</td></tr>
        <tr><td>MarkDown3</td><td>100% missing</td><td>14.2% missing</td><td>Active in 2012</td></tr>
        <tr><td>MarkDown4</td><td>100% missing</td><td>16.8% missing</td><td>Active in 2012</td></tr>
        <tr><td>MarkDown5</td><td>100% missing</td><td>0% missing</td><td>Fully active in 2012</td></tr>
        <tr><td>Total Sales</td><td>$91,674,774</td><td>$90,666,527</td><td>2011 higher despite zero promo</td></tr>
      </tbody>
    </table>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="interp-box">
      <strong>Finding:</strong> 2011 had zero markdown activity yet outperformed 2012 which ran
      active promotions across all stores. This indicates the sales gap is driven by
      <strong>weaker organic demand in 2012</strong>, not the absence of promotional effort.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
 
    # STEP 5
    st.markdown("""
    <div class="step-inv-header">
      <div class="step-inv-badge">5</div>
      <span class="step-inv-label">Identify recovery opportunities</span>
      <span class="step-inv-q">Where should we act before peak season?</span>
    </div>
    """, unsafe_allow_html=True)
 
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Top departments — YoY decline (week 42–43)**")
        depts = [
            ("Dept 72", "−22.8%", True),
            ("Dept 5",  "−14.2%", False),
            ("Dept 7",  "−13.1%", False),
            ("Dept 1",  "−9.4%",  False),
            ("Dept 55", "−23.9%", False)
        ]
        for name, dec, priority in depts:
            badge = '<span class="priority-badge">Priority</span>' if priority else ""
            st.markdown(f"""
            <div class="dept-item">
              <span class="dept-name">{name}{badge}</span>
              <span class="dept-decline">{dec}</span>
            </div>
            """, unsafe_allow_html=True)
 
    with col2:
        st.markdown("**Historical rank — all years**")
        hist = [
            ("#1 Dept 92", "$484M", "stable ✓",  "#9ca3af"),
            ("#2 Dept 95", "$449M", "stable ✓",  "#9ca3af"),
            ("#3 Dept 38", "$393M", "−1.7% ✓",   "#9ca3af"),
            ("#4 Dept 90", "$291M", "stable ✓",  "#9ca3af"),
            ("#5 Dept 72", "$306M", "−22.8% ⚠",  "#e07070")
        ]
        for rank, rev, status, color in hist:
            st.markdown(f"""
            <div class="dept-item">
              <span class="dept-name" style="color:{color}">{rank}</span>
              <span style="font-size:0.78rem;color:{color}">{rev} · {status}</span>
            </div>
            """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="interp-box">
      <strong>Finding:</strong> Dept 72 ranks 5th historically (~$306M total revenue) but dropped
  −22.8% in weeks 42–43. High historical demand + sharp recent decline = highest priority
  for recovery action before Thanksgiving and Christmas.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
 
    st.markdown("#### Key Findings Summary")
    st.markdown("""
    <div class="summary-grid">
      <div class="summary-card">
        <p class="summary-title">Marginal but real decline</p>
        <p class="summary-desc">−$1.0M (−1.1%) at weeks 42–43. Within normal variation but warrants attention before peak season.</p>
      </div>
      <div class="summary-card">
        <p class="summary-title">Type A & B stores most affected</p>
        <p class="summary-desc">Store 14 alone = ~77% of total nominal decline. Type C stores actually grew +4.6%.</p>
      </div>
      <div class="summary-card">
        <p class="summary-title">External factors ruled out</p>
        <p class="summary-desc">All macroeconomic factors show near-zero correlation with weekly sales across Q4 2011–2012.</p>
      </div>
      <div class="summary-card">
        <p class="summary-title">Dept 72 — top recovery priority</p>
        <p class="summary-desc">4th largest historically, −22.8% decline. Most actionable target before Christmas.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

# TAB 4 — Business Dashboard (Tableau)

with tab4:
 
    st.markdown("""
    <div class="context-box">
        Tableau dashboards are designed for stakeholder presentations, presenting the final results of an analysis in an easy-to-read visual format without needing to understand the underlying code or technical processes. They consist of two dashboards with a sequential storyline.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown("""
    <div class="tableau-embed">
      <div class="tableau-label">Dashboard 1 of 2</div>
      <div class="tableau-title">Q4 2012 Sales Decline — What Happened?</div>
      <div class="tableau-sub">Metric cards · Weekly sales trend · Top 7 stores · Sales by store type</div>
    </div>
    """, unsafe_allow_html=True)
 
    try:
        st.image("asset/dashboard1.png", use_container_width=True)
    except:
        st.info("📌 Tambahkan screenshot Dashboard 1 ke asset/dashboard1.png")
 
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
 
    st.markdown("""
    <div class="tableau-embed">
      <div class="tableau-label">Dashboard 2 of 2</div>
      <div class="tableau-title">Q4 2012 Sales Decline — Why & What To Do?</div>
      <div class="tableau-sub">Promo vs no promo · Top 10 department decline · Historical dept sales · Key findings</div>
    </div>
    """, unsafe_allow_html=True)
 
    try:
        st.image("asset/dashboard2.png", use_container_width=True)
    except:
        st.info("📌 Tambahkan screenshot Dashboard 2 ke asset/dashboard2.png")

# TAB 5 — Conclusion & Recommendation

with tab5:
 
    st.markdown("#### Conclusion")
    st.markdown("""
    <div class="context-box">
        The week 42–43 2012 underperformance was driven by <strong>weaker organic consumer
        demand</strong>, not by macroeconomic conditions or promotional strategy. The −1.1%
        decline is marginal in absolute terms but signals a demand shift that warrants proactive
        intervention, particularly at the department level and in Type A/B stores, before
        Thanksgiving and Christmas weeks.
    </div>
    """, unsafe_allow_html=True)
 
    st.markdown('<hr class="divider"/>', unsafe_allow_html=True)
    st.markdown("#### Recommendations")
 
    recs = [
        ("🔴 Investigate Department 72",
         "Dept 72 is the 4th largest historically (~$306M) but dropped −22.8% in weeks 42–43. Conduct a deep-dive into inventory levels, pricing strategy, and competitive positioning for this department specifically before peak season."),
        ("✅ Maintain strategy for Dept 92 and 95",
         "These are the two largest departments by historical revenue and remained stable or grew in 2012. No intervention needed, avoid disrupting what is working."),
        ("🏷️ Evaluate markdown efficiency by department",
         "Since broad promotions in 2012 did not outperform 2011 with zero promotions, future markdown allocation should be targeted, prioritize high-demand departments like Dept 72 rather than blanket store-wide promotions."),
        ("🏪 Monitor Type A and B stores closely",
         "The decline was concentrated in the largest store formats. Consider whether these stores require operational review, inventory adjustments, or localized promotional strategies."),
        ("📋 Await complete Q4 2012 data",
         "The dataset only covers through week 43. A full-quarter assessment, including Thanksgiving and Christmas weeks, is needed before drawing conclusions about overall Q4 performance."),
    ]
 
    for title, desc in recs:
        st.markdown(f"""
        <div class="rec-card">
          <div class="rec-title">{title}</div>
          <div class="rec-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)