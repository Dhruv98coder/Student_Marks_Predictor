import joblib

# Load the trained model
model = joblib.load("student_marks_model.pkl")

def predict_marks(study_hours, attendance, sleep_hours,
                  internet_usage, assignments_completed,
                  previous_score):

    prediction = model.predict([[
        study_hours,
        attendance,
        sleep_hours,
        internet_usage,
        assignments_completed,
        previous_score
    ]])[0]

    if prediction > 100:
        prediction = 99

    return round(prediction, 2)