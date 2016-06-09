#!/usr/bin/env python
# coding: utf-8

'''
SCRIPT TEMPLATE GENERATOR
Generates a python script skeleton

DEPENDENCIES
    Python 2.7

HOW TO RUN
    Double click script
'''

import os
import datetime

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1'
__date__ = '21:06h, 27/05/2016'
__status__ = 'Production'

def codeTemplate():
    '''
    Main Script
    Defines the body of the template script, checks for some possible errors
    and creates the file
    '''

    scriptName = 'scriptTemplate.py'
    shebang = '#!/usr/bin/env python'
    coding = '# coding: utf-8'
    title = 'TO DO SCRIPT NAME'
    description = 'TO DO DESCRIPTION'
    dependencies = 'TO DO DEPENDENCIES'
    howToRun = 'TO DO HOW TO RUN'
    requires = 'TO DO REQUIRES'
    ensures = 'TO DO ENSURES'
    author = "__author__ = ''"
    creditsList = "__credits__ = []"
    version = "__version__ = '0.1'"
    date = "__date__ = " + dateDefine()
    status = "__status__ = 'Production'"
    defTest = "def test():\n    pass\n\nif __name__ == '__main__':\n    test()"

    scriptLines = shebang + '\n' + coding + "\n\n'''\n" + title + '\n' + description + '\n\n' \
                + dependencies + '\n' + howToRun + '\n' + requires + '\n' + ensures + "\n'''\n\n" \
                + '#\n# imports\n#\n\n' + author + '\n' + creditsList + '\n' + version + '\n' \
                + date + '\n' + status + '\n\n#\n# code\n#\n\n' + defTest
   
    # Verifies if file already exists
    if os.path.isfile(os.path.join(os.getcwd(), scriptName)):
        print 'Error: File named "' + scriptName + '" already exists'
   
    else:
        try:
            with open(scriptName, 'wb') as script:
                script.write(scriptLines)
 
        except IOError, e:
            print 'Error with "' + e.filename + '" file:'
            print e.strerror

def dateDefine():
    '''
    Returns today's date and time in the following format:
    HH:MMh, dd/mm/yyyy
    '''

    date = datetime.datetime.now()

    # _date verification
    hour = dateVerification(date.hour)
    minute = dateVerification(date.minute)
    day = dateVerification(date.day)
    month = dateVerification(date.month)

    # '##:##h, ##/##/####'
    return "'" + hour + ':' + minute + 'h, ' + day + '/' + month + '/' + str(date.year) + "'"

def dateVerification(value):
    '''
    Adds a 0 if hour minute or second is between 0 and 9
    Used in dateDefine()
    '''

    value = str(value)
   
    if len(value) == 1:
        value = '0' + value

    return value

codeTemplate()
