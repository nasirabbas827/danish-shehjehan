from django.db import models 
from django.contrib.auth.models import User

class Election(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=[('upcoming', 'Upcoming'), ('ongoing', 'Ongoing'), ('completed', 'Completed')])

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='candidates/', null=True, blank=True)
    description = models.TextField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE, default=1)
    party_name = models.CharField(max_length=255, default="Party Name")
    party_symbol = models.ImageField(upload_to='party_symbols/', null=True, blank=True)  # New field for party symbol

    def __str__(self):
        return self.name


class VoteBlocks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    blockchain_code = models.CharField(max_length=64)  # Assuming the blockchain code is a hex string
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Vote by {self.user.username} for {self.candidate.name}"
