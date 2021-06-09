import pandas as pd
df = pd.read_csv('c:/tmp/Traffic/demo_traffic_jam_prediction/dataML.csv', 
            # index_col='stt',  
            header=0, 
            names=[ 'ev','lb'])
print(df.ev)
ev=list(df.ev)
lb=list(df.lb)
for x in range(0,10):
    ev+=ev
    lb+=lb
newdt = pd.DataFrame({"ev":ev,"lb":lb},columns=["ev","lb"])
newdt.to_csv('c:/tmp/Traffic/demo_traffic_jam_prediction/rawData.csv')