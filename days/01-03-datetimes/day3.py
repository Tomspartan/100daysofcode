from datetime import datetime,date,timedelta

freedom_date = datetime(2018,4,12)
start_code = datetime(2018,6,1)
today = datetime.today()

result = ((today - freedom_date).days)
days_since = ((today - start_code).days)

print("It has been " + str(result) + " days since Sherief left us")
print("You are on day " + str (days_since))
