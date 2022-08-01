# import by me
from django.forms import ModelForm
from todoapp.models import Todo


class TODOform(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'status', 'priority']
