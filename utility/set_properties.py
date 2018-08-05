__author__ = 'mranjan'

import os
from set_logging import logger
def get_properties():
    try:
        properties={}
        # Setting up the property file path to access the properties
        property_file_path=os.path.join(os.path.dirname(os.getcwd()),'pre_requisite','environment.properties')
        # Reading the properties files and setting up the values in a dictionary to use it globally
        logger.debug('Reading the properties files')
        with open(property_file_path) as fp:
            for line in fp.readlines():
                key_value=line.split('=')  # splitting each line of properties file
                properties[key_value[0]]=key_value[1]  # adding key values of property to the dictionary
            fp.close()
        return properties
    except FileNotFoundError as e:
        logger.error('Properties file not found\n'+str(e))

