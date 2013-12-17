# Some auxiliary functions and constants for competition
# administration.

from datetime import date


comp_closingdate=date(2013, 12, 13) #Year, Month, Day date format


def isOpen():
    """Logic to compare the closing date of the competition with today's date"""
    if date.today() > comp_closingdate:
        print 'The competition is closed'
        return False
    else:
        print 'The competition is open'
        return True

def closingDate():
    return str(comp_closingdate.day) + '/' + str(comp_closingdate.month)  + '/' + str(comp_closingdate.year)
