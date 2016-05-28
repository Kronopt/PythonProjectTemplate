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
   _author = ''
   _credits = []
   _version = '0.1'
   _date = '' # DATETIME
   _status = 'Production'
   
   # Verifies if file with the same name exists in the same directory, to avoid overwriting
   if os.path.isfile(os.path.join(os.getcwd(), scriptName)):
      print 'Error: File named "' + scriptName + '" already exists"
   
   else:
      try:
         with open(scriptName, 'wb') as script:
            script.write('cenaaas')














            
      except IOError, e:
         print 'Error with "' + e.filename + '" file:'
         print e.strerror

##def test():
##    """ Testing Docstring"""
##    pass
##
##if __name__=='__main__':
##    test()

codeTemplate()
