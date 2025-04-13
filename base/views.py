from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Reminder, Class, Todo, Test
import calendar
from datetime import date, timedelta
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User

class CustomHTMLCalendar(calendar.HTMLCalendar):
    def formatday(self, day, weekday):
        if day == 0:
            return '<td></td>'  # empty day
        if day == date.today():
            return f'<td class="today">{day}</td>'
        return f'<td>{day}</td>'
    
@login_required
def home(request):
    today = date.today()
    days_of_week = [(today + timedelta(days=i)).strftime('%a %d') for i in range(7)]
    now = date.today()
    year = now.year
    month = now.month
    # Create a plain HTML calendar
    cal = CustomHTMLCalendar(firstweekday=0)  # 0 = Monday
    html_calendar = cal.formatmonth(year, month)

    context = {
        'calendar': mark_safe(html_calendar),  # Mark as safe to render raw HTML
        'month': now.strftime("%B"),
        'year': year,
        'days_of_week': days_of_week,
        'reminders': Reminder.objects.filter(date=date.today()),
        'classes': Class.objects.filter(date=date.today()),
        'todos': Todo.objects.all(),
        'Tests': Test.objects.all(),
        'today': today
    }
    return render(request, 'home.html', context)



# def authView(request):
#  if request.method == "POST":
#   form = UserCreationForm(request.POST or None)
#   if form.is_valid():
#    form.save()
#    return redirect("base:login")
#  else:
#   form = UserCreationForm()
#  return render(request, "base/signup.html", {"form": form})
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    # Override the username field to remove help_text
    username = forms.CharField(
        help_text='',  # Empty help text or remove it entirely
        # widget=forms.TextInput(attrs={'placeholder': 'Your usern'})
    )
    password1 = forms.CharField(
        help_text='',  # Empty help text or remove it entirely
        # widget=forms.TextInput(attrs={'placeholder': 'password'})
    )
    password2 = forms.CharField(
        help_text='',  # Empty help text or remove it entirely
        # widget=forms.TextInput(attrs={'placeholder': 'password'})
    )
def authView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": form})

def reminders_view(request):
    today = date.today()
    now = date.today()
    year = now.year
    month = now.month

    # Create HTML calendar
    cal = CustomHTMLCalendar(firstweekday=0)
    html_calendar = cal.formatmonth(year, month)

    context = {
        'calendar': mark_safe(html_calendar),
        'month': now.strftime("%B"),
        'year': year,
        'reminders': Reminder.objects.all(),  # All reminders, not just today
        'today': today
    }
    return render(request, 'reminders.html', context)

def todo_view(request):
    today = date.today()
    now = date.today()
    year = now.year
    month = now.month

    # Create HTML calendar
    cal = CustomHTMLCalendar(firstweekday=0)
    html_calendar = cal.formatmonth(year, month)

    context = {
        'calendar': mark_safe(html_calendar),
        'month': now.strftime("%B"),
        'year': year,
        'reminders': Reminder.objects.all(),  # All reminders, not just today
        'today': today
    }
    return render(request, 'todo.html', context)
