-- AI Customer Support & Voice-of-Customer Intelligence
-- Table: support_tickets

SELECT COUNT(*) AS total_tickets,
       AVG(resolution_time_hours) AS avg_resolution_hours,
       AVG(customer_satisfaction) AS avg_csat,
       SUM(CASE WHEN sentiment='Negative' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS negative_rate,
       SUM(CASE WHEN resolution_status='Escalated' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS escalation_rate
FROM support_tickets;

SELECT issue_type, COUNT(*) AS tickets,
       AVG(resolution_time_hours) AS avg_resolution_hours,
       AVG(customer_satisfaction) AS avg_csat,
       SUM(CASE WHEN sentiment='Negative' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS negative_rate
FROM support_tickets GROUP BY issue_type ORDER BY negative_rate DESC;

SELECT channel, COUNT(*) AS tickets,
       AVG(resolution_time_hours) AS avg_resolution_hours,
       AVG(customer_satisfaction) AS avg_csat,
       SUM(CASE WHEN sentiment='Negative' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS negative_rate
FROM support_tickets GROUP BY channel ORDER BY avg_csat DESC;

SELECT product, COUNT(*) AS tickets,
       AVG(customer_satisfaction) AS avg_csat,
       SUM(CASE WHEN sentiment='Negative' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS negative_rate
FROM support_tickets GROUP BY product ORDER BY negative_rate DESC;

SELECT priority, COUNT(*) AS tickets,
       SUM(CASE WHEN resolution_status='Escalated' THEN 1 ELSE 0 END) AS escalations,
       AVG(resolution_time_hours) AS avg_resolution_hours
FROM support_tickets GROUP BY priority ORDER BY tickets DESC;

SELECT DATE_TRUNC('month',ticket_date) AS month, COUNT(*) AS tickets,
       SUM(CASE WHEN sentiment='Negative' THEN 1 ELSE 0 END)*1.0/COUNT(*) AS negative_rate,
       AVG(customer_satisfaction) AS avg_csat
FROM support_tickets GROUP BY DATE_TRUNC('month',ticket_date) ORDER BY month;
