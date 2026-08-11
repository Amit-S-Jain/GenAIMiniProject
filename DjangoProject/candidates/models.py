from django.db import models

class Candidates(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    linkedIn_url = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    gitHub_profile = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    current_city = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    current_state = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    willing_to_relocate = models.BooleanField()
    citizenship = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    professional_summery = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    preferred_roles = models.CharField(
            max_length=300,
            blank=True,
            null=True
    )

    preferred_locations = models.CharField(
            max_length=300,
            blank=True,
            null=True
    )

    total_experience = models.FloatField()
    relevant_experience = models.FloatField()    
    
    languages_know = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    

    current_company = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    current_role = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    current_ctc = models.FloatField(
        blank=True,
        null=True
    )

    expected_ctc = models.FloatField(
        blank=True,
        null=True
    )

    notice_period = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    LWD_if_resigned = models.DateField(
        blank=True,
        null=True
    )

    immediate_joiner = models.BooleanField()

    skills = models.CharField(
                max_length=100,
                blank=True,
                null=True
    )

    certifications = models.CharField(
                max_length=100,
                blank=True,
                null=True
    )

    education = models.CharField(
                max_length=100,
                blank=True,
                null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name