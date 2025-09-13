import logging

def add(a,b):
    logging.debug("Adding operation is taking place")
    return a+b

logging.debug("The addition function is called")
add(2,3)