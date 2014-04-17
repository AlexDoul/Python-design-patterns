# -*- coding: utf-8 -*-

import inspect

class Subject (object):
    '''This is a simple Subject class, that has some methods for changing
    his state. Each such a method starts with 'change_'.
    '''
    def __init__ (self):
        self.color = 'red'  # dummy
        self.size = 24  # dummy
        self.weight = 100  # dummy
        self.observers = {}
        self.events = ['all',]
        for member in dir (self):      
            obj = getattr (self, member)
            if callable (obj) and obj.__name__.startswith ('change_'):
                self.events.append (member)
        
    def add_observer (self, observer, event):
        ''' This is a signing observer for only one kind of events at once.
        '''
        if not (observer and event):
            raise 'You must specify observer and event'
        if event not in self.events:
            raise 'Wrong event type. You can choose one of : {}'.format (self.events)
        if event not in self.observers:
            self.observers [event] = [observer, ]
        else:
            if not observer in self.observers [event]:
                self.observers [event].append (observer)
                    
    def remove_observer (self, observer_2_del):
        '''Remove signed observer from all kind of events
        '''
        for event in self.observers.iterkeys ():
            if observer_2_del in self.observers [event]:
                self.observers [event].remove (observer_2_del)

    def notify (self, message):
        '''Notify observers about a specific event.
        '''
        # we want know, which of callers (events) is notifying
        event = inspect.stack()[1][3]
        # getting observers for our kind of event
        observers_event = self.observers [event] if event in self.observers else []
        # getting observers for all events
        observers_all = self.observers['all'] if 'all' in self.observers else []
        # making the set of observers to be unique
        observers_set = set (observers_event + observers_all)
        # updating each observer
        for observer in observers_set:
            # notifying
            observer.update (message)
    
    def change_color (self, new_color):
        self.color = new_color
        self.notify ('Subject has new color = {}'.format (new_color))
    
    def change_size (self, new_size):
        self.size = new_size
        self.notify ('Subject has new size = {}'.format (new_size))
    
    def change_weight (self, new_weight):
        self.weight = new_weight
        self.notify ('Subject has new weight = {}'.format (new_weight))
    
    
    
class Observer (object):
    '''Simple observer class.
    '''
    def __init__ (self, name):
        self.name = name
        
    def update (self, message):
        print '{}. {}'.format(self.name, message)



if __name__ == '__main__':

    subject = Subject ()
    # this observer wants to know only about color changes
    os1 = Observer ('Color observer')
    subject.add_observer (os1, 'change_color')
    # this observer wants to know only about size changes
    os2 = Observer ('Size observer')
    subject.add_observer (os2, 'change_size')
    # this observer wants to know about all changes
    os3 = Observer ('All events observer')
    subject.add_observer (os3, 'all')

    print '------------'
    subject.change_size (11)
    print '------------'
    subject.change_color('blue')
    print '------------'
    subject.change_weight (200)
    print '------------'





