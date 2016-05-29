#!/usr/bin/env python
# coding: utf-8

'''
SCRIPT TEMPLATE GENERATOR

TO DO DESCRIPTION

TO DO DEPENDENCIES
TO DO HOW TO RUN
TO DO REQUIRES
TO DO ENSURES
'''

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '0.1'
__date__ = '21:06h, 27/05/2016'
__status__ = 'Production'

import os
import datetime

def codeTemplate():
   '''
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
   _author = "__author__ = ''"
   _credits = "__credits__ = []"
   _version = "__version__ = '0.1'"
   _date = "__date__ = " + _dateDefine()
   _status = "__status__ = 'Production'"

   scriptLines = shebang + '\n' + coding + "\n\n'''\n" + title + '\n\n' + description + \
                 '\n\n' + dependencies + '\n' + howToRun + '\n' + requires + '\n' + ensures + \
                 "\n'''\n\n" + _author + '\n' + _credits + '\n' + _version + '\n' + _date + \
                 '\n' + _status + '\n\n# imports' + '\n\n# code'
   
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

def _dateDefine():
   '''
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
   Used in _dateDefine()
   '''

   value = str(value)
   
   if len(value) == 1:
      value = '0' + value

   return value

##def test():
##    """ Testing Docstring"""
##    pass
##
##if __name__=='__main__':
##    test()

codeTemplate()
