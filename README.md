# TrustCheck
A questionnaire-based self-assessment tool for Trustworthy AI, built with Django.
Maps organisational practices against ALTAI principles and produces a per-principle
maturity score.

## Features
- Admin-managed assessment content (principles, questions, weighted choices)
- Structured questionnaire workflow with per-principle scoring
- Results view with maturity bands (At risk / Developing / Strong)

## Stack
Django, SQLite, Python

## Why
Explores how Trustworthy-AI principles (ALTAI) and EU AI Act requirements can be
operationalised into an actionable self-assessment workflow.

## Run locally
```bash
pip install django
python manage.py migrate
python manage.py runserver
```
Visit http://127.0.0.1:8000/ for the assessment, or http://127.0.0.1:8000/admin/
to manage principles, questions, and choices.

## Roadmap
- Weighted principles, PDF export, multi-user orgs, question versioning
