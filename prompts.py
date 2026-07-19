"""
prompts.py
----------
AI prompt templates and Groq API integration.
Uses Groq free tier — no OpenAI credits needed.
"""

import os
from dotenv import load_dotenv

load_dotenv(override=True)


def generate_company_report(
    company: str,
    sector: str,
    report_type: str,
    context: str,
    kpis: list,
) -> str:
    """
    Generate a structured company intelligence report using Groq.
    Falls back to a helpful error message if API key is missing.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "⚠️ GROQ_API_KEY not found in .env file. Please add it and restart the app."

    kpi_names = ", ".join([k["name"] for k in kpis[:6]])

    prompts = {
        "Full Intelligence Report": f"""You are a senior analyst at a top-tier strategy firm producing an intelligence briefing.

Generate a structured company intelligence report for **{company}** in the **{sector}** sector.

SECTOR CONTEXT:
{context}

KEY METRICS TO REFERENCE: {kpi_names}

FORMAT YOUR RESPONSE EXACTLY LIKE THIS using markdown headers:

## Executive Summary
[3-4 sentences: what {company} does, its market position, and current strategic posture]

## Market Position & Competitive Standing
[4-5 bullet points on competitive positioning, market share, key differentiators]

## Financial Performance Indicators
[4-5 bullet points on financial health, key ratios, trends — use realistic estimates with appropriate caveats]

## Strategic Priorities
[4-5 bullet points on what the organisation is focused on strategically]

## Key Risks & Challenges
[3-4 bullet points on material risks facing the business]

## Transformation Outlook
[3-4 bullet points on digital, operational or strategic transformation underway]

## Analyst View
[2-3 sentences of objective strategic assessment]

IMPORTANT: Be specific and professional. Use industry terminology appropriate for {sector}.
If exact figures are uncertain, frame as estimates or industry benchmarks.
Do not say "I don't have access to" — instead provide informed analysis based on publicly known information.""",

        "KPI Snapshot": f"""You are a financial analyst producing a KPI snapshot briefing.

Generate a KPI-focused intelligence snapshot for **{company}** in the **{sector}** sector.

RELEVANT KPIs FOR THIS SECTOR: {kpi_names}

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:

## KPI Performance Summary
[2-3 sentences on overall financial and operational health]

## Headline Metrics
[6-8 bullet points with specific KPI estimates and commentary, e.g. "Cost-to-Income: estimated ~55%, reflecting ongoing efficiency programme"]

## Performance vs Industry Benchmarks
[4-5 bullet points comparing {company} to sector peers]

## Key Performance Drivers
[3-4 bullet points on what's driving current performance]

## Watch Points
[3 bullet points on metrics to monitor closely]

Frame estimates professionally. Use language like "estimated", "approximately", "reported" where appropriate.""",

        "Strategic Position": f"""You are a strategy consultant producing a competitive positioning assessment.

Generate a strategic positioning analysis for **{company}** in the **{sector}** sector.

SECTOR CONTEXT: {context}

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:

## Strategic Position Overview
[3 sentences on overall strategic positioning]

## Competitive Advantages
[4-5 bullet points — what {company} does better than competitors]

## Strategic Vulnerabilities
[3-4 bullet points — where {company} is exposed or under pressure]

## Competitive Threats
[3-4 bullet points — who is threatening {company}'s position and how]

## Strategic Options
[3-4 bullet points — strategic moves available to {company}]

## Recommendation
[2-3 sentences of strategic direction recommendation]""",

        "Risk Assessment": f"""You are a risk advisor producing an enterprise risk assessment.

Generate a risk assessment for **{company}** in the **{sector}** sector.

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:

## Risk Profile Summary
[2-3 sentences on overall risk posture]

## Top Strategic Risks
[4-5 bullet points — existential or major strategic risks with likelihood and impact]

## Operational Risks
[3-4 bullet points — day-to-day operational vulnerabilities]

## Financial Risks
[3-4 bullet points — balance sheet, liquidity, market risks]

## Regulatory & Compliance Risks
[3 bullet points — regulatory exposure and compliance pressures]

## Emerging Risks
[3 bullet points — horizon risks from technology, geopolitics, climate]

## Risk Mitigation Priorities
[3 bullet points — what management should focus on immediately]""",
    }

    prompt = prompts.get(report_type, prompts["Full Intelligence Report"])

    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior analyst at a top-tier strategy consulting firm. You produce concise, professional, boardroom-ready intelligence reports. Always use markdown formatting with ## headers. Be specific, use industry terminology, and provide genuine strategic insight."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4,
            max_tokens=1500,
        )
        return response.choices[0].message.content

    except ImportError:
        return "⚠️ Groq package not installed. Run: pip install groq"
    except Exception as e:
        return f"⚠️ Error generating report: {str(e)}"
