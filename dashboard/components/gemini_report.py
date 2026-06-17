import os
import google.generativeai as genai
from dotenv import load_dotenv

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-flash-latest")
else:
    model = None


# -----------------------------------
# Generate AI Report
# -----------------------------------

def generate_ai_report(summary):

    if model is None:
        return (
            "❌ Gemini API key not found.\n\n"
            "Create a .env file and add:\n"
            "GEMINI_API_KEY=YOUR_API_KEY"
        )

    network_data = f"""
Network Summary

Total Packets: {summary.get('total_packets')}
Total Clients: {summary.get('total_clients')}
Anomalies: {summary.get('anomaly_count')}
Health Score: {summary.get('network_health_score')}
Health Grade: {summary.get('health_grade')}
Risk Level: {summary.get('risk_level')}
Privacy Score: {summary.get('privacy_score')}
HTTPS Percentage: {summary.get('https_percentage')}%
Carbon Footprint: {summary.get('carbon_footprint')} g CO₂
"""

    prompt = f"""
You are a Senior Cybersecurity Analyst preparing a report for company management.

Analyze the following network summary.

{network_data}

Return the response in Markdown.

Formatting Rules:

- Use ### for the title.
- Use #### for section headings.
- Never use # or ## headings.
- Keep the report between 250 and 350 words.
- Do not repeat every metric.
- Focus on analysis and recommendations.
- Write in a professional but easy-to-understand style.

Structure:

### 📑 AI Network Intelligence Report

#### 📌 Executive Summary
Write 2 short paragraphs explaining the overall condition.

#### 🩺 Network Health
Write 3 bullet points.

#### 🔒 Security Analysis
Write 4 bullet points.

#### 🛡 Privacy Analysis
Write 3 bullet points.

#### 🌱 Sustainability Analysis
Write 2 bullet points.

#### ⚠️ Risk Assessment
Write 3 bullet points.

#### ✅ Recommendations
Write 5 concise actionable recommendations.

Avoid unnecessary technical jargon.
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.2,
                max_output_tokens=650,
            )
        )

        return response.text

    except Exception as e:

        error = str(e)

        if "429" in error:
            return """
### ⚠️ Gemini API Limit Reached

The free Gemini API quota has been exceeded.

Please wait a few moments and try generating the report again.
"""

        return f"❌ Error generating report:\n\n{error}"