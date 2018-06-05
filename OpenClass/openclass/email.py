from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def get_url():
    return 'http://localhost:8000'

def send_verification_mail(user, token):
    site_url = get_url()
    context = {}
    context['token'] = token
    context['site_url'] = site_url

    subject = "OpenClass Email verification"
    msg = "Here is the link for the validation %s%s" % \
            (site_url, reverse('openclass:verify', kwargs={'token':token}))
    html_msg = render_to_string('openclass/email_verification.html', context)
    to = [user.email,]
    send_mail(subject, msg, settings.EMAIL_HOST_USER, to, html_message=html_msg)


def ask_for_feedback(workshop):
    site_url = get_url()
    subject = "OpenClass need your feedback"
    msg = """Thank you for being part of the %s workshop, we hope that you \
            enjoyed it. We want to hear from you about how the workshop was,\
            please fill this form to give us some feedback %s%s""" % \
            (
            workshop.title,
            site_url,
            reverse('openclass:feedback', kwargs={'workshop_pk': workshop.pk})
            )
    to = [u.email \
            for u in workshop.registration_set.filter(present=True).profile]
    send_mail(subject, msg, settings.EMAIL_HOST_USER, to)

def notify_user_acceptance(workshop, user):
    site_url = get_url()
    subject = "Congratulations"
    msg = """Congratulations,\
            You have been accepted to the %s workshop.
            link to the workshop here: %s%s""" % \
            (
            workshop.title,
            site_url,
            reverse(
                    'openclass:workshops_detail',
                    kwargs={'workshop_pk':workshop.pk}
                    )
            )
    to = [user.email,]
    send_mail(subject, msg, settings.EMAIL_HOST_USER, to)

def notify_user_refusal(workshop, user):
        site_url = get_url()
        subject = "We are really sorry"
        msg = """We are really sorry,\
                You have been refused to the %s workshop.""" % workshop.title
        to = [user.email,]
        send_mail(subject, msg, settings.EMAIL_HOST_USER, to)
