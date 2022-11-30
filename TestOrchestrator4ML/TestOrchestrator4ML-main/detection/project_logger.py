import logging

# Implement logger similar to logging_example in workshop 9
def projectLogger():
    logging.basicConfig(filename='Project.log', level=logging.INFO, format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt='%d-%b-%y %H:%M:%S') 
    forensicLogger = logging.getLogger()
    return forensicLogger