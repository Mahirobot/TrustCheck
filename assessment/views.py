from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice, Assessment, Answer, Principle


def home(request):
    return render(request, "assessment/home.html")


def questionnaire(request):
    questions = Question.objects.select_related("principle").all()

    if request.method == "POST":
        assessment = Assessment.objects.create(
            organisation=request.POST.get("organisation", "Unnamed org")
        )
        for q in questions:
            choice_id = request.POST.get(f"question_{q.id}")
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                Answer.objects.create(
                    assessment=assessment, question=q, choice=choice
                )
        return redirect("assessment:result", assessment_id=assessment.id)

    return render(request, "assessment/questionnaire.html", {"questions": questions})


def result(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    answers = assessment.answers.select_related("choice", "question__principle")

    # Score per principle
    by_principle = {}
    for ans in answers:
        p = ans.question.principle.name
        by_principle.setdefault(p, {"got": 0, "max": 0})
        by_principle[p]["got"] += ans.choice.score
        by_principle[p]["max"] += 3  # max score per question

    results = []
    for name, s in by_principle.items():
        pct = round(100 * s["got"] / s["max"]) if s["max"] else 0
        band = "Strong" if pct >= 75 else "Developing" if pct >= 40 else "At risk"
        results.append({"principle": name, "pct": pct, "band": band})

    overall = round(sum(r["pct"] for r in results) / len(results)) if results else 0

    return render(request, "assessment/result.html", {
        "assessment": assessment,
        "results": results,
        "overall": overall,
    })
