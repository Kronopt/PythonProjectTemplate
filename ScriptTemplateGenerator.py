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


# imports

# code

##def test():
##    """ Testing Docstring"""
##    pass
##
##if __name__=='__main__':
##    test()


def codeTemplate(scriptName, shebang, coding, description, dependencies, howToRun, requires, ensures, _author, _credits, _version, _date, _email, _status):
   '''
   '''

   # usar os.path.isfile(fname) para verificar se o ficheiro existe antes de fazer overwrite com o novo ficheiro esqueleto...

   try:
      with open(scriptName + '.py', 'wb') as script:
         script.write('cenaaas')
      
   except IOError, e:
      if e.errno == 2:         
         print "Error: the given file doesn't exist."
      elif e.errno == 9:
         print e.strerror
         print
         print e.errno
         print e.filename
         print e.message
         print e.strerror


codeTemplate()
