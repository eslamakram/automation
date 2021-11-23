from automation import __version__


from automation.automation import *
import re

def test_version():
    assert __version__ == '0.1.0'

def test_Emails():
    with open('assets/emails.txt','r') as emails:
        emails=emails.read()
        emails=emails.split()
    for email in emails:
        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', email)
        assert bool(match)

def test_Phone_Numbers():
    with open('assets/phone_numbers.txt','r') as phones:
        phones=phones.read()
        phones=phones.split()
    for phone in phones:
        match = re.search(r'\d{3}-\d{3}-\d{4}$', phone)
        assert bool(match)