#!/usr/bin/env python
# coding: utf-8

"""
SCRIPT TEMPLATE GENERATOR
Generates a python script skeleton

DEPENDENCIES:
    Python 2.7

HOW TO RUN:
    Double click script
"""

import os
import datetime

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1'
__date__ = '18:31h, 17/10/2016'
__status__ = 'Production'


def code_template():
    """
    Main Script
    Defines the body of the template script, checks for some possible errors
    and creates the file
    """

    script_name = 'scriptTemplate.py'
    shebang = '#!/usr/bin/env python'
    coding = '# coding: utf-8'
    title = 'TO DO SCRIPT NAME'
    description = 'TO DO DESCRIPTION'
    dependencies = 'TO DO DEPENDENCIES'
    how_to_run = 'TO DO HOW TO RUN'
    requires = 'TO DO REQUIRES'
    ensures = 'TO DO ENSURES'
    author = "__author__ = ''"
    credits_list = "__credits__ = []"
    version = "__version__ = '0.1'"
    date = "__date__ = " + date_define()
    status = "__status__ = 'Production'"
    test_function = "def test():\n    pass\n\nif __name__ == '__main__':\n    test()"

    script_lines = shebang + '\n' + coding + '\n\n"""\n' + title + '\n' + description + '\n\n' + dependencies + '\n' \
        + how_to_run + '\n' + requires + '\n' + ensures + '\n"""\n\n' + '#\n# imports\n#\n\n' + author + '\n' \
        + credits_list + '\n' + version + '\n' + date + '\n' + status + '\n\n\n#\n# code\n#\n\n\n' + test_function \
        + '\n'

    # Verifies if file already exists
    if os.path.isfile(script_name):
        print 'Error: File named "' + script_name + '" already exists'

    else:
        try:
            with open(script_name, 'wb') as script:
                script.write(script_lines)

        except IOError, e:
            print 'Error with "' + e.filename + '" file:'
            print e.strerror


def date_define():
    """
    Returns today's date and time in the following format:
    HH:MMh, dd/mm/yyyy
    """

    date = datetime.datetime.now()

    # date verification
    hour = date_verification(date.hour)
    minute = date_verification(date.minute)
    day = date_verification(date.day)
    month = date_verification(date.month)

    # '##:##h, ##/##/####'
    return "'" + hour + ':' + minute + 'h, ' + day + '/' + month + '/' + str(date.year) + "'"


def date_verification(value):
    """
    Adds a 0 if hour, minute or second is between 0 and 9
    Used in date_define()

    PARAMETERS:
        value : str/int
            Represents an hour, minute or second
    """

    value = str(value)

    if len(value) == 1:
        value = '0' + value

    return value

if __name__ == "__main__":
    code_template()
