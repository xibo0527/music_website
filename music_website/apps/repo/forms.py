from django import forms
from .models import SongComments
from django.core.exceptions import ValidationError

class CommentsForm(forms.ModelForm):
    class Meta:
        model = SongComments
        fields = ['content']

    # &lt;script&gt;&lt;/script&gt;
    def clean_content(self):
        pattern = 'script'
        content = self.cleaned_data.get('content')
        if pattern in content:
            raise ValidationError('评论数据不合法')
        else:
            return self.cleaned_data.get('content')

