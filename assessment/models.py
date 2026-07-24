from django.db import models


class Principle(models.Model):
    """A Trustworthy-AI principle, e.g. an ALTAI dimension."""
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    """A single self-assessment question, mapped to a principle."""
    principle = models.ForeignKey(
        Principle, on_delete=models.CASCADE, related_name="questions"
    )
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.text[:80]


class Choice(models.Model):
    """An answer option carrying a maturity score 0-3."""
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="choices"
    )
    label = models.CharField(max_length=200)
    score = models.PositiveIntegerField(default=0)  # 0=No, 1=Partial, 2=Mostly, 3=Yes

    def __str__(self):
        return f"{self.label} ({self.score})"


class Assessment(models.Model):
    """One completed run of the questionnaire."""
    organisation = models.CharField(max_length=200, default="Unnamed org")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organisation} – {self.created_at:%Y-%m-%d}"


class Answer(models.Model):
    """A chosen Choice for a Question within an Assessment."""
    assessment = models.ForeignKey(
        Assessment, on_delete=models.CASCADE, related_name="answers"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
