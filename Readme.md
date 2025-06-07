# 📋 Smart Requirement Classifier using GPT

This Streamlit app classifies software requirements into **Functional** or **Non-Functional** using Azure OpenAI's GPT-4 model.

## 🔍 Features
- Upload a CSV file with a column named `requirement`
- Automatically classifies each requirement
- Provides a short summary
- Download the results as a CSV file

## 🚀 Technologies
- 🧠 Azure OpenAI (GPT-4o)
- 📦 Python, Pandas
- 🌐 Streamlit (web UI)
- 🧪 .env for secure API keys

## 📝 Example

**Input CSV:**
| requirement |
|-------------|
| Users must be able to reset passwords. |

**Output CSV:**
| requirement | type         | summary                                      |
|-------------|--------------|----------------------------------------------|
| Users must be able to reset passwords. | Functional | The system must allow users to reset passwords. |

## 🛠️ How to Run

1. Clone the repo
2. Create `.env` file with:
AZURE_OPENAI_KEY=4HoZ7TDCttMZQvggQLPnN6eppfTaMaBdIeTIT4iLNuhAp0S22RoCJQQJ99BFACfhMk5XJ3w3AAAAACOGUPka
AZURE_OPENAI_ENDPOINT=https://prath-mbmrvxc2-swedencentral.cognitiveservices.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_VERSION=2024-12-01-preview
3. install dependencies
pip install -r requirments.text
4. Run the app:
streamlit run app.py

## 📂 Sample
Use the provided `requirments_1.csv` to test the app

## 🧠 Idea Credit
This project is inspired by the need for intelligent document understanding in AI-based product teams


### 🔹 Step 4: Add a sample `example.csv`

```csv
requirement
Users must receive a confirmation email after password change.
The app should maintain 99.9% uptime during working hours.
Administrators can delete user accounts permanently