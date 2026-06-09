import pandas as pd
import random

data=[]

for i in range(100):

    study=random.randint(1,10)
    attendance=random.randint(50,100)
    assignments=random.randint(1,10)

    marks=(
        study*5
        + attendance*0.5
        + assignments*2
        + random.randint(-10,10)
    )

    marks=max(30,min(100,marks))

    result=1 if marks>=50 else 0

    data.append([
        study,
        attendance,
        assignments,
        marks,
        result
    ])

df=pd.DataFrame(
data,
columns=[
"Study_Hours",
"Attendance",
"Assignments",
"Previous_Marks",
"Result"
]
)

df.to_csv(
"student_data.csv",
index=False
)

print("Dataset Created")