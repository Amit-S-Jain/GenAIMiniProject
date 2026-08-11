# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import ResumeUploadForm, CandidateForm
from AIEngine.app import MainClass   # <-- your custom parsing function
import json
import tempfile
from django.conf import settings
from pathlib import Path


def upload_resume(request):
    print("Inside Upload Resume View")
    if request.method == "POST":
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES["resume"]
            candidate_email = form.cleaned_data["email"]  # assuming your form has an email field

            # Create folder if not exists
            save_dir = Path(settings.MEDIA_ROOT) / "resumes"
            save_dir.mkdir(parents=True, exist_ok=True)

            # Build filename using candidate email
            file_extension = Path(resume_file.name).suffix  # keep original extension (.pdf, .docx, etc.)
            safe_email = candidate_email.replace("@", "_at_").replace(".", "_")  # sanitize filename
            filename = f"{safe_email}{file_extension}"
            file_path = save_dir / filename

            # Save file permanently
            with open(file_path, "wb+") as destination:
                for chunk in resume_file.chunks():
                    destination.write(chunk)

            # Optional: parse resume after saving
            print("File Path is as below : ",file_path)
            parsed_data = MainClass.parse_resume(file_path)

             # Redirect to candidate_form_view with parsed_data
            request.session["parsed_data"] = parsed_data  # store temporarily in session
            return redirect(reverse("candidate_form_view"))
    else:
        form = ResumeUploadForm()
    return render(request, "candidates/upload_resume.html", {"form": form})

    #         return render(
    #             request,
    #             "candidates/success.html",
    #             {"form": form, "parsed": parsed_data, "saved_path": file_path},
    #         )
    # else:
    #     form = ResumeUploadForm()
    # return render(request, "candidates/upload_resume.html", {"form": form})


def candidate_form_view(request):
    print("Inside Candidate Form View")
    # default_data = {
    #     "name": "Amit Sanjay Jain",
    #     "email": "amitsjain9161@gmail.com",
    #     "phone": "+91 7020194397",
    #     "current_city": "Pune",
    #     "current_state": "Maharashtra",
    #     "willing_to_relocate": True,
    #     "citizenship": "Indian",
    #     "professional_summery": "Results-driven Data Engineer...",
    #     "preferred_roles": "Data Engineer, Palantir Foundry Specialist",
    #     "preferred_locations": "Pune, Bangalore",
    #     "total_experience": 4.0,
    #     "relevant_experience": 2.0,
    #     "languages_know": "Python, SQL",
    #     "current_company": "Infosys Ltd",
    #     "current_role": "Senior Associate Consultant",
    #     "skills": "ETL Pipelines, Data Modeling",
    #     "education": "Bachelor of Engineering in IT"
    # }

    # json_string = json.dumps(default_data)
    # return HttpResponse(json_string, content_type='application/json')


    # form = CandidateForm(initial=default_data)

    # # return render(request, "candidates/candidate_form.html", {"form": form})

    # if request.method == "POST":
    #     form = CandidateForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return render(request, "candidates/success.html")  # redirect or show success page

    # return render(request, "candidates/candidate_form.html", {"form": form})

    parsed_data = request.session.get("parsed_data", {})  # retrieve parsed data
    form = CandidateForm(initial=parsed_data)  # pre-fill with parsed resume data

    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()  # saves into Candidate model
            return render(request, "candidates/success.html", {"candidate": form.instance})

    return render(request, "candidates/candidate_form.html", {"form": form})