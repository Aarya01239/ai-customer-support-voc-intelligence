# Automated AI Support Workflow

## What this does

This workflow turns raw customer-support tickets into structured operational signals with minimal manual effort.

```text
Support Ticket
      ↓
Intent Classification
      ↓
Sentiment Scoring
      ↓
Priority Scoring
      ↓
AI-style Summary
      ↓
Recommended Action
      ↓
Human Review Flag
      ↓
CSV / Dashboard
```

## Run

From the project root:

```bash
python ai-workflow/ai_support_workflow.py
```

The workflow reads:

`data/support_tickets.csv`

and creates:

`ai-workflow/ai_workflow_output.csv`

## Why this is portfolio-relevant

The workflow demonstrates how an analyst can automate repetitive analysis while keeping human judgment for high-impact customer decisions.

## AI/Automation Positioning

The current implementation is API-free and reproducible. The summary and recommendation functions are deliberately isolated so they can later be replaced with an LLM/API call without changing the rest of the pipeline.

## Human-in-the-loop

Negative or high-priority cases are flagged for human review. The automation is designed to assist analysts/agents rather than make unsupervised customer-facing decisions.
