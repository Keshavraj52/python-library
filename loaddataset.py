import pandas as pd
import numpy as np
data=pd.read_csv("Training.csv")

data3=pd.read_csv("kesh.csv")
data.head()

data1=data[data["prognosis"]=="Fungal infection"]
replaced_prognosis=data.replace("Fungal infection","बुरशीजन्य संसर्ग")
print(replaced_prognosis)
# replaced_prognosis.to_csv("keshavraj.csv")
remove_col=data.drop(["itching","skin_rash"],axis=1)
remove_get=data.iloc[1:5]

# row= {"name":"keshavrajpore",
#       "height":"543",
#       "weight":"54",
#       "bmi":"20"}
# new_row=data3.append(row,ignore_index=True)
unique=data.drop_duplicates(subset=["prognosis"])

print("unique data:",len(unique))