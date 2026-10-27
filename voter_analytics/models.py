from django.db import models

# Create your models here.
class Voter(models.Model):
    """A registered voter record."""

    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)

    # Residential address
    street_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10, blank=True)
    zip_code = models.CharField(max_length=10)

    date_of_birth = models.DateField()
    date_of_registration = models.DateField()

    party_affiliation = models.CharField(max_length=2)
    precinct_number = models.CharField(max_length=10)

    # Participation in recent elections
    v20state = models.BooleanField(default=False)
    v21town = models.BooleanField(default=False)
    v21primary = models.BooleanField(default=False)
    v22general = models.BooleanField(default=False)
    v23town = models.BooleanField(default=False)

    # How many of the 5 elections above the voter participated in (0-5)
    voter_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.street_number} {self.street_name})"