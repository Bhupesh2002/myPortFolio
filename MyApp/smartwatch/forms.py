from django import forms

class CaloriesForm(forms.Form):
    
    EXERCISES_CHOICES = [
        ('walking', 'Walking'),
        ('running', 'Running'),
        ('cycling', 'Cycling'),
        ('swimming', 'Swimming'),
        ('yoga', 'Yoga'),
    ]

    age = forms.IntegerField(
        label="Age (years)",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    weight = forms.FloatField(
        label="Weight (kg)",
        min_value=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    duration = forms.IntegerField(
        label="Activity Duration (minutes)",
        min_value=1,
        max_value=120,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    exercise = forms.ChoiceField(
        choices=EXERCISES_CHOICES,
        label="Select Exercise",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

