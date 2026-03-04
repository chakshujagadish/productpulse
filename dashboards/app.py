import streamlit as st
import pandas as pd
import plotly.express as px

st.title("ProductPulse – Product Analytics Dashboard")

# Load metrics
funnel = pd.read_csv("reports/funnel_daily.csv")

st.subheader("Daily Funnel Metrics")

fig = px.line(
    funnel,
    x="event_date",
    y=["viewers", "carters", "purchasers"],
    title="User Funnel Activity"
)

st.plotly_chart(fig)

st.subheader("Conversion Rate")

fig2 = px.line(
    funnel,
    x="event_date",
    y="view_to_purchase_rate",
    title="View to Purchase Conversion Rate"
)

st.plotly_chart(fig2)

st.subheader("AI Product Recommendations")

with open("reports/ai_recommendations.txt") as f:
    st.text(f.read())