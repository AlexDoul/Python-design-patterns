# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Context (object):
    '''Context class that can change his printing strategy.
    '''

    def __init__ (self, text):
        self.header, self.sub_header, self.text = text.split('<sep>', 3)
        self.strategy = None

    def set_strategy (self, strategy):
        self.strategy = strategy

    def do_print (self):
        self.strategy.print_text (self)



class Strategy (object):
    '''Base abstract class for future concrete strategy realizations.
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_text (self, text):
        pass
    
class HeaderkStrategy (Strategy):
    '''Strategy realization for header printing.
    '''
    def print_text (self, context):
        print context.header.upper ()
        print '=' * len (context.header), '\n'


class SubHeaderStrategy (Strategy):
    '''Strategy realization for sub header printing.
    '''
    def print_text (self, context):
        print context.sub_header
        print '-' * len (context.sub_header), '\n'

        
class ParagraphStrategy (Strategy):
    '''Strategy realization for usual text printing.
    '''
    def print_text (self, context):
        print context.text
        


if __name__ == '__main__':

    book_printer = Context ('book header.<sep>Paragraph title.<sep>Some dummy text for fun.')

    book_printer.set_strategy (HeaderkStrategy ())
    book_printer.do_print ()

    book_printer.set_strategy (SubHeaderStrategy ())
    book_printer.do_print ()

    book_printer.set_strategy (ParagraphStrategy ())
    book_printer.do_print ()
    
