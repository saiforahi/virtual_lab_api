from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        # del self.fields['username']
        # self.fields['payment_service'].required = True

    class Meta:
        model = User
        fields = "__all__"


class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        # del self.fields['username']
        # self.fields['groups'].required = True

    class Meta:
        model = User
        fields = "__all__"


# class UserNfcCardForm(forms.ModelForm):
#     class Meta:
#         model = UserNfcCard
#         exclude = ['deleted_at','created_at','updated_at']
