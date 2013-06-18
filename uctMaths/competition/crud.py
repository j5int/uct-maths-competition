from competition.models import *

def Add_School(name, language, address, phone, fax, contact, entered, score, email):
	School.objects.create(name=name, language=language, address=address, phone=phone, fax=fax, contact=contact, entered=entered,score=score, email=email)
	