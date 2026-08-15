# 🤖 AI Customer Support & Voice-of-Customer Intelligence

> AI-assisted customer support analytics project combining SQL, Python, sentiment analysis, automation and BI concepts to convert support-ticket data into actionable business decisions.

## 📌 Executive Summary

Customer support teams generate large volumes of support-ticket data. Manually reviewing every ticket to understand sentiment, priority, recurring issues and customer pain points is time-consuming.

This project builds an AI-assisted Voice-of-Customer (VoC) analytics workflow that transforms support-ticket data into structured business insights.

The solution analyzes:

- Customer sentiment
- Support channels
- Issue categories
- Priority levels
- Resolution time
- Customer satisfaction
- Escalation patterns
- Product and customer pain points

The project also includes a runnable automated workflow that performs repetitive analysis and flags high-impact cases for human review.

---

## 🎯 Business Objective

The primary objective is to help customer-support and business teams:

1. Identify the most common customer problems.
2. Detect negative customer sentiment.
3. Prioritize high-impact support cases.
4. Understand channel and product-level support performance.
5. Reduce repetitive manual analysis.
6. Generate faster business recommendations.
7. Maintain a human-in-the-loop process for important decisions.

---

## 🛠️ Tech Stack

- SQL — analytical queries and KPI analysis
- Python / Pandas — data processing
- Sentiment Analytics — customer sentiment analysis
- AI-Assisted Analytics — summaries and recommendations
- Automation — repeatable support-ticket processing
- BI Dashboard Concepts — KPI and trend visualization
- GitHub — version control and portfolio presentation

---

## 📊 Dataset

The project uses a synthetic customer-support dataset containing 12,000 support tickets.

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
- Escalation information

> Data Note: The dataset is synthetic and is used only for portfolio demonstration. It does not contain real customer information.

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

- Top customer pain point: App Bug
- Channel requiring attention: Email
- Product with highest negative-sentiment rate: Mobile App
- Negative-sentiment tickets require proactive resolution.
- Long-resolution cases are useful candidates for escalation and process improvement.
- Combining sentiment, priority and resolution time provides stronger operational insight than using a single metric.

---

# 🤖 Automated AI-Assisted Workflow

A major feature of this project is the automated support analytics pipeline.

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

### What the Automation Does

The workflow automatically:

1. Reads the support-ticket dataset.
2. Classifies support intent.
3. Generates a sentiment confidence score.
4. Calculates a priority score.
5. Generates a concise ticket summary.
6. Recommends the next business action.
7. Flags high-priority or negative cases for human review.
8. Writes processed results to a new CSV file.

---

## ⚙️ Run the Automated Workflow

From the project root:

    python ai-workflow/ai_support_workflow.py

### Input

    data/support_tickets.csv

### Output

    ai-workflow/ai_workflow_output.csv

The workflow is designed to be API-free and reproducible for portfolio demonstration.

An external LLM or AI API can later replace the summary and recommendation functions without rebuilding the complete pipeline.

---

## 🧠 Human-in-the-Loop Design

Automation should assist analysts rather than blindly make customer-facing decisions.

The workflow flags cases for human review when they have signals such as:

- Negative sentiment
- High priority
- Critical operational impact
- Long resolution time

### Smart-Worker Principle

> Automation handles repetitive analysis while human validation is retained for important business decisions.

This demonstrates a practical approach to using AI in analytics:

**Automation handles repetitive analysis → Human validates important decisions.**

---

# 📊 Dashboard

The dashboard provides a business-facing view of customer-support performance.

It covers:

- Ticket volume
- Sentiment analysis
- Priority distribution
- Issue types
- Channel performance
- Resolution time
- CSAT
- Escalation patterns
- Customer pain points

Dashboard files:

- `dashboard/support_voc_dashboard_preview.png`
- `dashboard/support_voc_dashboard.html`

---

# 💼 Business Value

## Customer Support Teams

- Faster ticket triage
- Better prioritization
- Earlier identification of dissatisfied customers
- Reduced repetitive analysis

## Business Analysts

- Faster Voice-of-Customer reporting
- Automated KPI preparation
- Data-driven recommendations
- Repeatable analytical workflow

## Product Teams

- Identification of recurring product issues
- Customer pain-point discovery
- Support-driven product improvement opportunities

## Management

- Executive-level support KPIs
- Escalation visibility
- Customer experience monitoring
- Operational improvement opportunities

---

# 🧠 How Generative AI Was Used

Generative AI was used as an analytical copilot to assist with:

- Data profiling
- SQL query generation and refinement
- Python analysis
- KPI selection
- Sentiment and pain-point interpretation
- Business recommendation generation
- Workflow design
- Documentation
- Dashboard planning

Final metrics and analytical outputs were programmatically validated.

---

# 🔄 AI-Assisted Workflow Architecture

The project follows a repeatable analytics workflow:

Raw Data
↓
Data Cleaning
↓
SQL / Python Analysis
↓
Customer Sentiment Analysis
↓
AI-Assisted Interpretation
↓
Automated Recommendations
↓
Human Validation
↓
Business Dashboard
↓
Executive Insights

This approach helps reduce repetitive manual work while maintaining analytical quality and business judgment.

---

# 🔮 Future Enhancements

- Real-time ticket ingestion
- LLM-based ticket summarization
- Automated root-cause extraction
- RAG-based support knowledge assistant
- Automated response drafting
- Real-time sentiment monitoring
- Power BI / Tableau live dashboard
- Critical sentiment alerts
- Customer churn-risk prediction
- CRM / helpdesk integration
- Automated weekly executive reports
- Real-time customer experience monitoring

---

# 📁 Repository Structure

ai-customer-support-voc-intelligence/
│
├── README.md
│
├── data/
│   └── support_tickets.csv
│
├── sql/
│   └── support_voc_analysis.sql
│
├── python/
│   └── support_voc_analysis.py
│
├── ai-workflow/
│   ├── README.md
│   └── ai_support_workflow.py
│
├── dashboard/
│   ├── support_voc_dashboard_preview.png
│   └── support_voc_dashboard.html
│
├── business-insights/
│   └── executive_insights.md
│
└── AI_WORKFLOW.md

---

# 🧪 Portfolio Demonstration

This project demonstrates practical capability across:

**SQL → Python → Analytics → AI Assistance → Automation → BI → Business Recommendations**

The objective is not simply to build a dashboard.

It demonstrates how an analyst can create a repeatable analytics workflow that:

- Reduces manual effort
- Automates repetitive analysis
- Identifies customer pain points
- Generates actionable recommendations
- Supports faster decision-making
- Keeps human validation for important cases

---

# 🎯 Skills Demonstrated

- Data Analysis
- Business Analytics
- Customer Analytics
- Voice-of-Customer Analytics
- SQL
- Python
- Pandas
- Sentiment Analysis
- KPI Development
- Dashboard Design
- AI-Assisted Analytics
- Workflow Automation
- Business Intelligence
- Executive Reporting
- GitHub Portfolio Development

---

## 👤 Author

**Venkata Kumar Pulapa**

Aspiring Data Analyst | Business Analyst | Product Analytics | AI-Assisted Analytics

---

## ⭐ Portfolio Highlights

- Synthetic dataset for safe portfolio demonstration
- SQL analytics
- Python data processing
- Customer sentiment analysis
- Support KPI analysis
- AI-assisted workflow
- Automated processing pipeline
- Human-in-the-loop validation
- Business-focused recommendations
- Dashboard visualization
- Executive insights
- GitHub-ready project structure

---

## 📌 Project Status

**Completed — Portfolio Ready ✅**

The project demonstrates an end-to-end analytics workflow from raw customer-support data to automated analysis, dashboard insights and business recommendations.
