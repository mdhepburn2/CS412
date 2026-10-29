# File: models.py
# Author: Matthew Hepburn (mhepburn@bu.edu), 10/27/2026
# Description: Data model for the voter analytics app. Defines the Voter model
#   (name, address, birth and registration dates, party, precinct, election
#   participation, and voter score) and the helper functions that load the
#   Newton voter CSV into the database.

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

def load_data():
    '''Function to load data records from csv file into django database'''
    filename = 'voter_analytics/newton_voters.csv'

    f = open(filename, 'r')

    #discard header
    f.readline()

    for line in f:
        fields = line.strip().split(',')

        try:
            voter = Voter(
                last_name=fields[1],
                first_name=fields[2],
                street_number=fields[3],
                street_name=fields[4],
                apartment_number=fields[5],
                zip_code=fields[6],
                date_of_birth=fields[7],
                date_of_registration=fields[8],
                party_affiliation=fields[9],
                precinct_number=fields[10],
                v20state=parse_bool(fields[11]),
                v21town=parse_bool(fields[12]),
                v21primary=parse_bool(fields[13]),
                v22general=parse_bool(fields[14]),
                v23town=parse_bool(fields[15]),
                voter_score=fields[16]
            )

            voter.save()

        except Exception as e:
            # print('something went wrong')
            # print(f'line={line}')
            print(e)

    print(f'created {Voter.objects.all().count()} voters')

def parse_bool(s:str):
    '''converts a string TRUE or FALSE to boolean'''
    if s.strip().lower() == 'true':
        return True
    elif s.strip().lower() == 'false':
        return False
    else:
        raise ValueError(f'{s} not true or false')