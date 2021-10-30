from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Learn Django for at least 20 minutes every day!",
    "may": "Learn Django for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Learn Django for at least 20 minutes every day!",
    "august": "Learn Django for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Learn Django for at least 20 minutes every day!",
    "november": "Learn Django for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!",
}


def monthly_challenge_by_number(request, month: int):
    try:
        forward_month = list(monthly_challenges.keys())[month - 1]
    except:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponseRedirect(f'/challenges/{forward_month}')


def monthly_challenge(request, month: str):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
