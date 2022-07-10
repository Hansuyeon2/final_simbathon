from accounts.models import User

def login_processor(request):
    context = {}

    login_session = request.session.get('login_session', '')

    if login_session == '':
        context['login_session'] = False
        context['username'] = '익명'
    else:
        context['login_session'] = True
        context['username'] = User.objects.get(username=login_session).nickname

    return context