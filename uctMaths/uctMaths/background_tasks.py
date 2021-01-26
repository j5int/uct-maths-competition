from background_task import background

import sys
sys.path.append("../")

#from competition.compadmin import generate_zipped_school_answer_sheets_from_id

@background(schedule=5,queue="AS-generation-queue")
def bg_generate_school_answer_sheets(schoolID):
    print("Processing school with ID: " + schoolID)
    #generate_zipped_school_answer_sheets_from_id(schoolID)