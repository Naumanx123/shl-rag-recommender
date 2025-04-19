import streamlit as st
import requests

st.title("🧠 SHL Assessment Recommender")

query = st.text_input("Enter job description, skill, or requirement")

if st.button("Get Recommendations") and query:
    res = requests.get("http://localhost:8000/recommend", params={"query": query})
    output = res.json()

    st.subheader("🤖 AI Recommendation:")
    st.write(output["response"])

    st.subheader("🔍 Top Matches:")
    for item in output["results"]:
        st.markdown(f"### [{item['name']}]({item['url']})")
        st.write(f"🧪 Type: {item['test_type']}, ⏱ Duration: {item['duration']} min")
        st.write(f"💻 Remote: {item['remote_testing']}, IRT: {item['adaptive_irt']}")
        st.markdown("---")
