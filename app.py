import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="CaptureNow - Photography Price Prediction",
    page_icon="📸",
    layout="wide"
)

# Title
st.title("📸 CaptureNow - Photography Price Prediction")
st.markdown("### Estimate Your Photography Package Price")

st.markdown("---")

# Customer Details
st.subheader("📋 Enter Booking Details")

col1, col2 = st.columns(2)

with col1:
    event = st.selectbox(
        "Event Type",
        ["Wedding", "Pre-Wedding", "Birthday", "Baby Shoot", "Engagement", "Corporate Event"]
    )

    hours = st.slider("Photography Hours", 1, 15, 5)

    photographers = st.selectbox(
        "Number of Photographers",
        [1,2,3,4]
    )

    videographers = st.selectbox(
        "Number of Videographers",
        [0,1,2,3]
    )

with col2:
    drone = st.selectbox(
        "Drone Required?",
        ["No","Yes"]
    )

    album = st.selectbox(
        "Album Required?",
        ["No","Yes"]
    )

    distance = st.number_input(
        "Travel Distance (KM)",
        min_value=0,
        max_value=500,
        value=20
    )

    edited_photos = st.slider(
        "Edited Photos",
        50,
        1000,
        250
    )

st.markdown("---")

if st.button("💰 Estimate Package Price"):

    # Temporary Formula
    price = (
        hours * 2500
        + photographers * 4000
        + videographers * 3000
        + distance * 20
        + edited_photos * 15
    )

    if drone == "Yes":
        price += 6000

    if album == "Yes":
        price += 4000

    if event == "Wedding":
        price += 12000
    elif event == "Pre-Wedding":
        price += 7000
    elif event == "Engagement":
        price += 5000
    elif event == "Birthday":
        price += 3000
    elif event == "Corporate Event":
        price += 8000

    st.success("✅ Estimated Photography Package Price")

    st.metric(
        label="Estimated Price",
        value=f"₹ {price:,.0f}"
    )

    st.balloons()

st.markdown("---")

st.info(
    "📌 This is a demo estimation. "
    "In the next step, we will replace this formula with a Machine Learning Linear Regression model."
)