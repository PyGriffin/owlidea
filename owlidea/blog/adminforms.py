from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.TextInput,label="摘要",required=False)
