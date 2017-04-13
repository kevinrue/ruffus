from ruffus import *

def first_task():
    print("First task")

@follows(first_task)
def second_task():
    print("Second task")

pipeline_run(second_task)