# features/steps/auth.py

from behave import given
from django.contrib.auth.models import User


@given('an authenticated user')
def given_auth_user(context):
    User.objects.create_superuser(username='test', email='foo@bar', password='test')

    br = context.browser
    br.visit(context.base_url + '/admin/')
    br.fill('username', 'test')
    br.fill('password', 'test')
    br.find_by_css('.submit-row input').first.click()
