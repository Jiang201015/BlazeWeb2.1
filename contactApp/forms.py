from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'sex', 'personID', 'email', 'birth', 'edu','experience', 'position', 'photo')
        sex_list = (
            ('男', '男'),
            ('女', '女'),
        )
        edu_list = (
            ('小学', '小学'),
            ('初中', '初中'),
        )
        widgets = {
            'sex': forms.Select(choices=sex_list),
            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }