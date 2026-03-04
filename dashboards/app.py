import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="ProductPulse", layout="wide")

st.title("ProductPulse — Product Growth & Retention Dashboard")

funnel = pd.read_csv("reports/funnel_daily.csv")
ret = pd.read_csv("reports/retention_weekly.csv")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Funnel (Daily)")
    fig = px.line(funnel, x="event_date", y=["viewers","carters","purchasers"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("View → Purchase Conversion")
    fig2 = px.line(funnel, x="event_date", y="view_to_purchase_rate")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("AI Recommendations")
with open("reports/ai_recommendations.txt") as f:
    st.text(f.read())