import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("D:\Machine learning document\machine_learning\Regression\LinearRegression\Student_Practice_Real_marks_data.csv")
X = df[['study_hours','attendance','sleep_hours',
        'internet_usage','assignments_completed',
        'previous_score']]

y = df['exam_score']

model = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "student_marks_model.pkl")

print("Model Saved Successfully")