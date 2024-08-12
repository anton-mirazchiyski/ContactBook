from django.contrib.auth import get_user_model

UserModel = get_user_model()


def get_current_account(request):
    account = UserModel.objects.get(username=request.user.username)
    return account
