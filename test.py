from predict import predict_marks

result = predict_marks(
    8,   # Study Hours
    90,  # Attendance
    7,   # Sleep Hours
    3,   # Internet Usage
    18,  # Assignments Completed
    80   # Previous Score
)

print("Predicted Marks:", result)