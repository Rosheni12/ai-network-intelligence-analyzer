import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


def generate_ai_report(network_data: str) -> str:
    if model is None:
        return (
            "❌ Gemini API key not found.\n\n"
            "Create a .env file and add:\n"
            "GEMINI_API_KEY=YOUR_API_KEY"
        )

    prompt = f"""
You are IBM watsonx Security AI, an enterprise Network Intelligence Engine and AI SOC Analyst.

You interpret network telemetry produced by an AI Network Intelligence Analyzer that uses:
• Random Forest Classification
• Isolation Forest Anomaly Detection
• AI Risk Scoring
• Feature Engineering
• Network Behaviour Analytics

Network Metrics:
{network_data}

YOUR JOB:
- Perform deep investigation by correlating metrics.
- Always explain WHY conclusions follow from the metrics.
- Never repeat raw numbers.
- Explicitly reference key metrics (e.g. 82.11 health score, 4.97% anomaly rate, 87.07% HTTPS adoption, 71.69 privacy score) in observations.
- Mention Random Forest and Isolation Forest where relevant to highlight AI analysis.
- Only make conclusions clearly supported by the supplied metrics.

Return the report EXACTLY in this format. No duplicate titles. No extra text.

📑 AI Network Intelligence Report
═══════════════════════════════════════
🟢 Overall Network Status
Overall Status :
Health Grade :
Threat Severity :
Immediate Action :
Write ONLY 2 very short sentences.
═══════════════════════════════════════
🤖 AI Executive Summary
Exactly 5 bullets. Max 12 words each.
═══════════════════════════════════════
🔍 Key Findings
Exactly FIVE findings. Keep every field 1 short sentence max. Reference metrics and models.

Finding 1
Observation :
Root Cause :
Security Impact :
Business Impact :
Priority :
Recommended Action :

(Continue until Finding 5)
═══════════════════════════════════════
🛡 Security Assessment
One short sentence per item:

Network Health :
Threat Exposure :
Encryption Status :
Client Behaviour :
Traffic Stability :
Privacy Posture :
AI Verdict :
═══════════════════════════════════════
⚠ Risk Matrix
Exactly FIVE rows:

| Risk | Severity | Likelihood | Business Impact | Action |
|------|----------|------------|-----------------|--------|
|      |          |            |                 |        |

═══════════════════════════════════════
🚀 AI Recommendations
Exactly FIVE. Keep each under 25 words total.

Issue: 
Reason: 
Recommendation: 
Expected Improvement: 
Priority: 

═══════════════════════════════════════
📈 Near-Term Network Assessment
Maximum 4 short bullets based on current metrics.
═══════════════════════════════════════

Style: Very concise, professional, IBM Security / Splunk tone.
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                temperature=0.3,
                max_output_tokens=5000,
                top_p=0.95,
                top_k=40,
            ),
        )

        if not response.text:
            return "❌ Empty response from Gemini."

        return response.text.strip()

    except Exception as e:
        error = str(e)
        if "429" in error:
            return "⚠️ Gemini API Limit Reached\n\nPlease wait a few minutes."
        return f"❌ Error generating report:\n\n{error}"