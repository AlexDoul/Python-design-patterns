# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import random

class Coder (object):
    '''Abstract factory class, that implements factory method 'code_factory_method'
    '''
    
    __metaclass__ = ABCMeta

    def __init__ (self):
        self.mistake_count = 0
        self.code_creator = self.code_factory_method ()
        
    @abstractmethod
    def code_factory_method (self):
        '''Factory method.
        Creates Coder object, that can create and execute some code.
        '''
        pass
    
    def do_work (self):
        self.code_creator.create_code ()
        # code may be broken
        try:
            self.code_creator.execute_code ()
        except:
            # we don't raise exception, just do counting mistakes
            self.mistake_count += 1

    
class Junior (Coder):

    def code_factory_method (self):
        '''Factory method realization
        '''
        
        class JuniorLevel (object):
            
            def create_code (self):
                self.code = "1/{}".format (random.randint (0, 2))
            def execute_code (self):
                    eval (self.code)

        return JuniorLevel ()
                

class Developer (Coder):
    
    def code_factory_method (self):
        '''Factory method realization
        '''
    
        class DeveloperLevel (object):
            def create_code (self):
                self.code = "1/{}".format (random.randint (0, 20))
            def execute_code (self):
                eval (self.code)

        return DeveloperLevel ()
    

class Senior (Coder):

    def code_factory_method (self):
        '''Factory method realization
        '''

        class SeniorLevel (object):
            def create_code (self):
                self.code = "1/{}".format (random.randint (0, 100))
            def execute_code (self):
                eval (self.code)

        return SeniorLevel ()

if __name__ == '__main__':

    j = Junior ()
    d = Developer ()
    s = Senior ()
    for _ in xrange (365):
        j.do_work ()
        d.do_work ()
        s.do_work ()
    print "Junior's mistake count = {}".format (j.mistake_count)
    print "Developer's mistake count = {}".format (d.mistake_count)
    print "Senior's mistake count = {}".format (s.mistake_count)

        
        
    
    
