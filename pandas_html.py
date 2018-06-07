import pandas as pd
table = pd.read_html("http://www.stat-nba.com/team/CHI.html",attrs = {'class': 'stat_box'})
print(table)
# pd =DataFrame()
# calls_df, = pd.read_html("http://www.stat-nba.com/team/CHI.html", header=None, parse_dates=False)[0]
# # print(calls_df)
# calls_df.to_csv("calls.csv", index=False)