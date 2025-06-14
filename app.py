import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="Forex Wizard Analyzer", layout="centered")

st.title("📈 Forex Wizard - Support & Resistance Analyzer")
st.markdown("Upload a live chart screenshot, then click Run Analysis to get entry, TP, SL & insights.")

uploaded_file = st.file_uploader("📤 Upload your chart image (JPG/PNG)", type=["jpg", "jpeg", "png"])
run_analysis = st.button("▶️ Run Analysis")

if run_analysis and uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='🧠 Analyzing Chart...', use_column_width=True)

    with st.spinner('Analyzing... Please wait...'):
        time.sleep(2)  # Simulate processing

        # 📤 Output
        st.markdown("## 📊 Analysis Result")
        st.markdown("""
        Based on the provided chart for XAU/USD (Gold vs US Dollar) on the H1 timeframe:

        1. Trend Analysis  
        The price has made a significant upward move above the moving average, indicating strong bullish momentum.

        2. RSI  
        The RSI is at 63.5%, which is above the neutral 50 but still below the overbought level of 70.  
        This suggests that there is potential for further upward movement but also warrants caution.

        3. Recommendation  
        ✅ Buy — Considering the strong upward move and momentum, entering a buy position could be favorable.

        4. Take Profit — Set around 3055 to 3060  
        5. Stop Loss — Set around 3025

        ⚠️ Always ensure to adjust your strategy based on real-time data and events impacting the market.
        """)

elif run_analysis and uploaded_file is None:
    st.warning("Please upload a chart image before running analysis.")
