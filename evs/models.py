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

    def __str__(self):
        return self.name

class BlockchainCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    blockchain_code = models.CharField(max_length=64)  # Assuming 64 characters for the blockchain code

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"