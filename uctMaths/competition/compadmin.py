# Some auxiliary functions and constants for competition
# administration.

from datetime import date

#A few administration constants and associated methods to be used around the website.

#The date until which entries are accepted
comp_closingdate=date(2013, 12, 19) #(YYYY, MM, DD) format
#The date of prizegiving
comp_prizegivingdate=date(2013, 12, 19) #(YYYY, MM, DD) format

admin_emailaddress='admin@admin.com' #Email address for inquiries/outgoing emails

def isOpen():
    """Logic to compare the closing date of the competition with today's date"""
    if date.today() > comp_closingdate:
        #print 'The competition is closed'
        return False
    else:
        #print 'The competition is open'
        return True

def closingDate():
    return str(comp_closingdate.day) + '/' + str(comp_closingdate.month)  + '/' + str(comp_closingdate.year)
