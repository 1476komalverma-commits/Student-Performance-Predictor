import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

from sklearn.tree import DecisionTreeClassifier

# Load dataset
df=pd.read_csv(
"student_data.csv"
)

# -------------------
# Linear Regression
# -------------------

X_lr=df[
[
"Study_Hours",
"Attendance",
"Assignments"
]
]

y_lr=df[
"Previous_Marks"
]

X_train_lr,X_test_lr,y_train_lr,y_test_lr=(
train_test_split(
X_lr,
y_lr,
test_size=0.2,
random_state=42
)
)

linear=LinearRegression()

linear.fit(
X_train_lr,
y_train_lr
)

# -------------------
# Decision Tree
# -------------------

X_dt=df[
[
"Study_Hours",
"Attendance",
"Assignments",
"Previous_Marks"
]
]

y_dt=df[
"Result"
]

X_train_dt,X_test_dt,y_train_dt,y_test_dt=(
train_test_split(
X_dt,
y_dt,
test_size=0.2,
random_state=42
)
)

tree=DecisionTreeClassifier()

tree.fit(
X_train_dt,
y_train_dt
)

# -------------------
# UI
# -------------------

st.title(
"Student Performance Predictor"
)

st.write(
"Enter Student Details"
)

study=st.slider(
"Study Hours",
1,
10
)

attendance=st.slider(
"Attendance %",
50,
100
)

assignments=st.slider(
"Assignments",
1,
10
)

if st.button(
"Predict"
):

    predicted_marks=(
        linear.predict(
            [[
                study,
                attendance,
                assignments
            ]]
        )[0]
    )

    result=(
        tree.predict(
            [[
                study,
                attendance,
                assignments,
                predicted_marks
            ]]
        )[0]
    )

    st.subheader(
        "Prediction Result"
    )

    st.metric(
        "Predicted Marks",
        round(
            predicted_marks,
            1
        )
    )

    if result==1:

        st.success(
            "Student Will PASS"
        )

    else:

        st.error(
            "Student Will FAIL"
        )