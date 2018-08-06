import inspect
import logging
import os

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    log_path=os.path.join(os.path.dirname(os.getcwd()),'Logs','debug.log')
    if os.path.exists(log_path):
        pass
    else:
        fp = open(log_path,'w')
        fp.close()
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler(log_path.format(loggerName), mode='w')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger