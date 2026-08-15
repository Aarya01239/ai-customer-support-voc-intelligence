"""
Automated AI Customer Support Workflow
--------------------------------------
Input: ../data/support_tickets.csv
Output: ai_workflow_output.csv

Pipeline:
1. Detect customer intent from issue text/type
2. Score sentiment
3. Calculate priority
4. Generate an AI-style ticket summary
5. Recommend the next business action
6. Flag cases for human review

This portfolio implementation is intentionally API-free and reproducible.
An LLM/API can be plugged into the summarize/recommend functions later.
"""

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "support_tickets.csv"
OUTPUT = ROOT / "ai-workflow" / "ai_workflow_output.csv"

df = pd.read_csv(INPUT)

def classify_intent(row):
    issue = str(row["issue_type"]).lower()
    mapping = {
        "payment failed": "Payment Support",
        "login issue": "Authentication",
        "refund delay": "Refund Support",
        "card issue": "Card Support",
        "account access": "Account Support",
        "app bug": "Technical Support",
        "loan query": "Loan Support",
    }
    return mapping.get(issue, "General Support")

def sentiment_score(row):
    sentiment = str(row["sentiment"]).lower()
    return {"positive": 0.85, "neutral": 0.50, "negative": 0.15}.get(sentiment, 0.50)

def priority_score(row):
    score = 0
    score += {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}.get(
        str(row["priority"]), 2
    )
    if str(row["sentiment"]) == "Negative":
        score += 1
    if float(row["resolution_time_hours"]) > 48:
        score += 1
    return min(score, 6)

def generate_summary(row):
    return (
        f"{row['issue_type']} reported through {row['channel']}; "
        f"sentiment={row['sentiment']}, priority={row['priority']}, "
        f"resolution_time={row['resolution_time_hours']}h."
    )

def recommend_action(row):
    if row["priority_score"] >= 5:
        return "Escalate to priority queue + human review"
    if row["sentiment"] == "Negative":
        return "Agent review + proactive resolution"
    if row["resolution_status"] == "Pending":
        return "Follow-up required"
    return "Standard workflow"

df["intent"] = df.apply(classify_intent, axis=1)
df["sentiment_confidence"] = df.apply(sentiment_score, axis=1)
df["priority_score"] = df.apply(priority_score, axis=1)
df["ai_summary"] = df.apply(generate_summary, axis=1)
df["recommended_action"] = df.apply(recommend_action, axis=1)
df["human_review_required"] = (
    (df["priority_score"] >= 5) |
    (df["sentiment"] == "Negative")
)

df.to_csv(OUTPUT, index=False)

print(f"Processed {len(df):,} support tickets.")
print(f"Human-review cases: {df['human_review_required'].sum():,}")
print(f"Output: {OUTPUT}")
