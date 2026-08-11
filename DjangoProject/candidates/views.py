# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ResumeUploadForm, CandidateForm
from AIEngine.app import MainClass   # <-- your custom parsing function
import json
import tempfile
from pathlib import Path

def upload_resume(request):
    print("Inside Upload Resume View")
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES["resume"]

            # Save to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                for chunk in resume_file.chunks():
                    tmp.write(chunk)
                tmp_path = Path(tmp.name)

            # Now pass the Path to DocumentConverter
            parsed_data = MainClass.parse_resume(tmp_path)
            # parsed_data = converter.convert(tmp_path)

            return render(
                request,
                "candidates/success.html",
                {"form": form, "parsed": parsed_data},
            )
    else:
        form = ResumeUploadForm()
    return render(request, "candidates/upload_resume.html", {"form": form})

def candidate_form_view(request):
    print("Inside Candidate Form View")
    default_data = {
        "name": "Amit Sanjay Jain",
        "email": "amitsjain9161@gmail.com",
        "phone": "+91 7020194397",
        "current_city": "Pune",
        "current_state": "Maharashtra",
        "willing_to_relocate": True,
        "citizenship": "Indian",
        "professional_summery": "Results-driven Data Engineer...",
        "preferred_roles": "Data Engineer, Palantir Foundry Specialist",
        "preferred_locations": "Pune, Bangalore",
        "total_experience": 4.0,
        "relevant_experience": 2.0,
        "languages_know": "Python, SQL",
        "current_company": "Infosys Ltd",
        "current_role": "Senior Associate Consultant",
        "skills": "ETL Pipelines, Data Modeling",
        "education": "Bachelor of Engineering in IT"
    }

    # json_string = json.dumps(default_data)
    # return HttpResponse(json_string, content_type='application/json')


    form = CandidateForm(initial=default_data)

    # return render(request, "candidates/candidate_form.html", {"form": form})

    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "candidates/success.html")  # redirect or show success page

    return render(request, "candidates/candidate_form.html", {"form": form})
