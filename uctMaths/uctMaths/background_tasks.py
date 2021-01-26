from background_task import background

@background(schedule=5,queue="AS-generation-queue")
def process(school):
    print(school + " HELLO!")