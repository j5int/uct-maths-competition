from background_task import background

import ho.pisa as pisa
import sys
sys.path.append("../")

@background(queue="AS-generation-queue")
def bg_generate_school_answer_sheets(schoolID):
    print("Processing school with ID: " + str(schoolID))
    from competition.compadmin import generate_zipped_school_answer_sheets_from_id
    from competition.reports import send_confirmation
    path = generate_zipped_school_answer_sheets_from_id(schoolID)

    pdf = pisa.pisaDocument("../" + path)
    send_confirmation(None, pdf, "test")
