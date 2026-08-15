# 🤖 AI Customer Support & Voice-of-Customer Intelligence

> **AI-assisted customer support analytics project combining SQL, Python, sentiment analysis, automation and BI concepts to convert support-ticket data into actionable business decisions.**

---

## 📌 Executive Summary

Customer support teams generate large volumes of unstructured and semi-structured ticket data. Manually reviewing every ticket to understand sentiment, priority, recurring issues and customer pain points is time-consuming.

This project builds an **AI-assisted Voice-of-Customer (VoC) analytics workflow** that transforms support-ticket data into structured insights.

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
- **Python** — Pandas-based data processing
- **NLP / Sentiment Concepts** — customer sentiment analysis
- **AI-assisted Analytics** — summaries and recommendations
- **Automation** — repeatable support-ticket processing workflow
- **BI Dashboard Concepts** — KPI and trend visualization
- **GitHub** — version control and portfolio presentation

---

## 📊 Dataset

The project uses a **synthetic customer-support dataset containing 12,000 support tickets**.

The dataset covers a representative period from **January 2025 to June 2026** and includes fields such as:

- Ticket ID
- Customer information
- Product / service
- Issue type
- Support channel
- Sentiment
- Priority
- Resolution status
- Resolution time
- CSAT
- Escalation indicators

> **Data note:** The dataset is synthetic and is used only for portfolio demonstration. It does not contain real customer information.

---

## 📈 Key KPIs

The analysis tracks customer-support KPIs such as:

| KPI | Purpose |
|---|---|
| Total Tickets | Overall support workload |
| Negative Sentiment % | Customer dissatisfaction indicator |
| Average Resolution Time | Operational efficiency |
| Average CSAT | Customer satisfaction |
| Escalation Rate | Support-risk indicator |
| Tickets by Channel | Channel performance |
| Tickets by Issue Type | Root pain-point identification |
| Priority Distribution | Workload severity |

---

## 🔎 Key Findings

The analysis highlights patterns such as:

- **App-related bugs** are an important recurring customer pain point.
- **Negative-sentiment tickets** require additional attention and proactive resolution.
- Email and other digital channels can generate significant support volume.
- Long-resolution cases are useful candidates for escalation or process improvement.
- Combining sentiment, priority and resolution time provides a stronger signal than using any single metric.

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
