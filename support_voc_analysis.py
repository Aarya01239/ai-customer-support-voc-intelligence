import pandas as pd
df=pd.read_csv("../data/support_tickets.csv",parse_dates=["ticket_date"])
print("Tickets:",len(df))
print("Negative rate:",df.sentiment.eq("Negative").mean())
print("Average resolution:",df.resolution_time_hours.mean())
print("Average CSAT:",df.customer_satisfaction.mean())
