from django.shortcuts import render
from predict import predict_marks 

def home(request):
    if request.method == "POST":
        student_name = request.POST.get('student_name', '')
        study_hours = float(request.POST.get('study_hours', 0))
        attendance = float(request.POST.get('attendance', 0))
        sleep_hours = float(request.POST.get('sleep_hours', 0))
        
        internet_status = request.POST.get('internet_status', 'No')
        if internet_status == 'No':
            internet_usage = 0.0
        else:
            internet_usage = float(request.POST.get('internet_usage', 0))
            
        assignments_completed = int(request.POST.get('assignments_completed', 0))
        previous_score = float(request.POST.get('previous_score', 0))

      
        final_prediction = predict_marks(
            study_hours, 
            attendance, 
            sleep_hours, 
            internet_usage, 
            assignments_completed, 
            previous_score
        )

        context = {
            'student_name': student_name,
            'prediction': final_prediction
        }
        
     
        return render(request, "result.html", context)

  
    return render(request, "index.html")