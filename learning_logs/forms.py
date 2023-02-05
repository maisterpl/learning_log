from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        mode = Topic
        fields = ['text']
        labels = {'text': ''}
