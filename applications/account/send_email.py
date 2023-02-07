from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Py25 account project', # title
        f'http://localhost:8000/account/activate/{code}', # body
        'ismail.arsa050505@gmail.com', # from
        [email] # to
    )