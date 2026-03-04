import pandas as pd
import streamlit as st
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="ProductPulse Decision Dashboard", layout="wide")

st.title("ProductPulse — Product Decision Dashboard")
st.caption("Funnel • Retention • Feature Adoption • Churn Risk • A/B Experiments • Recommendations")

def load_csv(path):
    p = Path(path)
    if not p.exists():
        st.warning(f"Missing file: {path}. Run pipeline steps first.")
        return None
    return pd.read_csv(p)

funnel = load_csv("reports/funnel_daily.csv")
ret = load_csv("reports/retention_weekly.csv")
adopt = load_csv("reports/adoption_retention.csv")
ab = load_csv("experiments/ab_results.csv")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Funnel", "Retention", "Feature Adoption", "A/B Testing", "AI/Strategy"
])

with tab1:
    st.subheader("Conversion Funnel (Daily)")
    if funnel is not None:
        c1, c2 = st.columns(2)
        with c1:
            fig = px.line(funnel, x="event_date", y=["viewers","carters","purchasers"])
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            fig2 = px.line(funnel, x="event_date", y="view_to_purchase_rate")
            st.plotly_chart(fig2, use_container_width=True)

with tab2:
    st.subheader("Retention (Weekly Cohorts)")
    if ret is not None:
        # Simple chart: active users over active_week (not full heatmap)
        fig = px.line(ret, x="active_week", y="active_users", color="cohort_week")
        st.plotly_chart(fig, use_container_width=True)
        st.info("Tip: Add a cohort heatmap later for an even more advanced visual.")

with tab3:
    st.subheader("Feature Adoption vs Retention Proxy")
    if adopt is not None:
        fig = px.bar(adopt, x="feature", y="retention_rate", hover_data=["users"])
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("A/B Test Results (Statistical Decision)")
    if ab is not None:
        st.dataframe(ab, use_container_width=True)
        decision = ab.loc[0, "decision"]
        st.success(f"Decision: {decision}")

with tab5:
    st.subheader("AI Recommendations")
    rec_path = Path("reports/ai_recommendations.txt")
    if rec_path.exists():
        st.text(rec_path.read_text())
    else:
        st.warning("Missing reports/ai_recommendations.txt. Run: python -m src.insights")

    st.subheader("Product Strategy (PRD + Roadmap)")
    prd = Path("strategy/PRD.md")
    road = Path("strategy/Roadmap.md")
    if prd.exists():
        st.markdown(prd.read_text())
    if road.exists():
        st.markdown(road.read_text())