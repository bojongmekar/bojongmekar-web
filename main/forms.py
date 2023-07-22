from django.forms import ModelForm
from main.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "email", "message"]