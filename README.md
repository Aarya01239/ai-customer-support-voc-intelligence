# 🤖 AI Customer Support & Voice-of-Customer Intelligence

> AI-assisted customer support analytics project combining SQL, Python, sentiment analysis, automation and BI concepts to convert support-ticket data into actionable business decisions.

## 📌 Executive Summary

Customer support teams generate large volumes of support-ticket data. Manually reviewing every ticket to understand sentiment, priority, recurring issues and customer pain points is time-consuming.

This project builds an **AI-assisted Voice-of-Customer (VoC) analytics workflow** that transforms support-ticket data into structured business insights.

The solution analyzes:

- Customer sentiment
- Support channels
- Issue categories
- Priority levels
- Resolution time
- Customer satisfaction
- Escalation patterns
- Product/customer pain points

The project also includes a **runnable automated workflow** that performs repetitive analysis and flags high-impact cases for human review.

---

## 🎯 Business Objective

The primary objective is to help customer-support and business teams:

1. Identify the most common customer problems.
2. Detect negative customer sentiment.
3. Prioritize high-impact support cases.
4. Understand channel and product-level support performance.
5. Reduce repetitive manual analysis.
6. Generate faster business recommendations.
7. Maintain a **human-in-the-loop** process for important decisions.

---

## 🛠️ Tech Stack

- **SQL** — analytical queries and KPI analysis
- **Python / Pandas** — data processing
- **Sentiment Analytics** — customer sentiment analysis
- **AI-Assisted Analytics** — summaries and recommendations
- **Automation** — repeatable support-ticket processing
- **BI Dashboard Concepts** — KPI and trend visualization
- **GitHub** — version control and portfolio presentation

---

## 📊 Dataset

The project uses a **synthetic customer-support dataset containing 12,000 support tickets**.

The dataset covers January 2025 to June 2026 and includes:

- Ticket ID
- Product / service
- Issue type
- Support channel
- Sentiment
- Priority
- Resolution status
- Resolution time
- Customer satisfaction

> **Data Note:** The dataset is synthetic and is used only for portfolio demonstration. It does not contain real customer information.

---

## 📈 Key KPIs

| KPI | Value |
|---|---:|
| Total Tickets | 12,000 |
| Negative Sentiment | 45.8% |
| Average Resolution Time | 34.1 hours |
| Average CSAT | 3.21 / 5 |
| Escalation Rate | 3.9% |

---

## 🔎 Key Findings

- **Top customer pain point:** App Bug
- **Channel requiring attention:** Email
- **Product with highest negative-sentiment rate:** Mobile App
- Negative-sentiment tickets require proactive resolution.
- Long-resolution cases are useful candidates for escalation and process improvement.
- Combining sentiment, priority and resolution time provides stronger operational insight than using a single metric.

---

# 🤖 Automated AI-Assisted Workflow

A major feature of this project is the **automated support analytics pipeline**.

```text
Raw Support Tickets
        ↓
Intent Classification
        ↓
Sentiment Scoring
        ↓
Priority Scoring
        ↓
AI-style Ticket Summary
        ↓
Recommended Business Action
        ↓
Human Review Flag
        ↓
CSV / Dashboard Output
