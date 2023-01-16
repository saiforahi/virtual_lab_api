from django import forms
from django.forms import ModelForm

from schedules.models import Schedule


class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class DatePickerInput(forms.TimeInput):
    input_type = 'date'


class ScheduleCreateForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['date','start_time', 'end_time', 'is_available']

        widgets = {
            'date' : DatePickerInput(),
            'start_time' : TimePickerInput(),
            'end_time': TimePickerInput(),
        }


class ScheduleChangeForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['date','start_time', 'end_time', 'is_available']

        widgets = {
            # 'date' : DatePickerInput(),
            'start_time' : TimePickerInput(),
            'end_time': TimePickerInput(),
        }