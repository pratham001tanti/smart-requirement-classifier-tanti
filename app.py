import openai
import streamlit as st
import pandas as pd
from azure.core.credentials import AzureKeyCredential

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_type = "azure"
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
openai.api_key = os.getenv("AZURE_OPENAI_KEY")

deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")


st.title("📋 Smart Requirement Classifier")
st.write("Upload a CSV file of requirements to classify and summarize using GPT-4.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'requirement' not in df.columns:
        st.error("The CSV must have a column named 'requirement'.")
    else:
        if st.button("Classify Requirements"):
            with st.spinner("Asking GPT... this might take a moment ⏳"):
                results = []
                print("----- Starting classification -----")
                for req in df['requirement']:
                    print(f"\n🔍 Requirement: {req}")

                    prompt = f"""
                    You are a helpful assistant that classifies software requirements.

                    Your task:
                    - Identify whether the following is a [Functional] or [Non-Functional] requirement.
                    - Provide a short, clear summary.

                    Respond ONLY in this format:
                    [Functional] - summary here
                    OR
                    [Non-Functional] - summary here

                    Requirement:
                    \"\"\"{req}\"\"\"
                    """

                    try:
                        response = openai.ChatCompletion.create(
                            engine="gpt-4o",
                            messages=[{"role": "user", "content": prompt}]
                        )
                        output = response.choices[0].message['content']
                        results.append(output)
                        print(f"🤖 GPT Output: {output}")

                        if "[" not in output or "]" not in output:
                            output = "[Unknown] - Format not matched"



                    except Exception as e:
                        print("❌ Error calling GPT:", str(e))
                        results.append("Error")

                if len(results) == len(df):
                    df['gpt_output'] = results
                    df[['type', 'summary']] = df['gpt_output'].str.extract(r"\[(.*?)\] - (.*)")

                    st.success("🎉 Classification complete!")
                    st.dataframe(df[['requirement', 'type', 'summary']])

                    # Download button
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button("📥 Download Result CSV", data=csv, file_name='classified_requirements.csv',
                                       mime='text/csv')
                else:
                    st.error("⚠️ Error: Mismatch in result lengths. Please try again or check your input.")


#1!