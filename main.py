import pandas as pd
import openai

openai.api_key = "Pratham@2305"  # Replace with your real key

def ask_gpt(text):
    prompt = f"""Classify this requirement as either 'Functional' or 'Non-Functional' and give a short summary:\n\n"{text}"\n\nReturn format: [Type] - Summary"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# Load data
df = pd.read_csv("requirements.csv")
results = []

# Process each requirement
for req in df['requirement']:
    gpt_response = ask_gpt(req)
    results.append(gpt_response)

# Add results to DataFrame
df['gpt_output'] = results
df[['type', 'summary']] = df['gpt_output'].str.extract(r"\[(.*?)\] - (.*)")

# Save output
df.to_csv("classified_requirements.csv", index=False)
print("Done! Output saved to classified_requirements.csv")