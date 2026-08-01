from django.contrib import admin
from .models import Candidates


@admin.register(Candidates)
class CandidatesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "current_company",
        "current_role",
        "total_experience",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "current_company",
        "current_role",
    )

    list_filter = (
        "current_company",
        "notice_period",
    )