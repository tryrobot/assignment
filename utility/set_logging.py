__author__ = 'mranjan'

import os,logging


try:
    log_path=os.path.join(os.path.dirname(os.getcwd()),'reports','debug.log')
    if os.path.exists(log_path):
        pass
    else:
        fp=open(log_path,'w')
        fp.close()
    logger=logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    handler=logging.FileHandler(log_path)
    handler.setLevel(logging.DEBUG)

    formatter=logging.Formatter('%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',datefmt="%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
except (PermissionError,FileNotFoundError,FileExistsError):
    print('Exception occurred while setting up the log path')



