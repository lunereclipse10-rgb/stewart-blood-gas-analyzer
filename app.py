import streamlit as st
st.set_page_config(page_title="Stewart Blood Gas Analyzer", layout="wide")
st.title("Stewart Blood Gas Analyzer")
# Basic UI and calculation logic
with st.expander("Input Data", expanded=True):
      ph = st.number_input("pH", 6.8, 7.8, 7.4)
      paco2 = st.number_input("PaCO2", 10.0, 120.0, 40.0)
      na = st.number_input("Na", 100.0, 180.0, 140.0)
      cl = st.number_input("Cl", 70.0, 140.0, 100.0)
      alb = st.number_input("Alb", 0.5, 8.0, 4.5)
      p = st.number_input("P", 0.5, 12.0, 3.0)
      lac = st.number_input("Lac", 0.0, 30.0, 1.0)
      k = st.number_input("K", 1.0, 10.0, 4.0)
      hco3 = st.number_input("HCO3", 5.0, 50.0, 24.0)
  sid = na + k -cl
gap = sid - (hco3 + 2.5 * alb + 0.5 * p + lac)
st.metric("SID", f"{sid:.1f}")
st.metric("SIG (Gap)", f"{gap:.1f}")
if ph < 7.35: st.error("Acidosis")
elif ph > 7.45: st.info("Alkalosis")
else: st.success("Normal pH")
  
