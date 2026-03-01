import streamlit as st
from summarizer import summarize_policy
from generator import generate_policy

# Page config
st.set_page_config(page_title="Policy AI System", layout="wide")

st.title("AI-Assisted Policy Summarization and Scenario Generator")

# Create two columns
col1, col2 = st.columns(2)

# LEFT PANEL — SUMMARIZER
with col1:
    st.header("Policy Summarization")

    policy_text = st.text_area(
        "Paste policy text here:",
        height=300
    )

    if st.button("Summarize Policy"):

        if policy_text.strip() == "":
            st.warning("Please paste policy text first.")
        else:
            summary = summarize_policy(policy_text)
            st.session_state.summary = summary

            st.success("Summary generated successfully!")
            st.write(summary)


# RIGHT PANEL — GENERATOR
with col2:
    st.header("Scenario-Based Policy Generator")

    scenario = st.text_input(
        "Enter scenario:",
        placeholder="Example: Adapt for rural communities"
    )

    if st.button("Generate Policy Draft"):

        if "summary" not in st.session_state:
            st.warning("Please generate summary first.")
        elif scenario.strip() == "":
            st.warning("Please enter scenario.")
        else:
            generated = generate_policy(
                st.session_state.summary,
                scenario
            )

            st.success("Policy draft generated!")
            st.write(generated)


# Default message
if "summary" not in st.session_state:
    st.info("Enter policy text on the left and click Summarize.")

