import abc
from threading import Thread
#abstract method and interface for components class
class IComponent(metaclass=abc.ABCMeta):
        @classmethod
        def __subclasshook__(cls, subclass):
                return(hasattr(subclass,'initialize') and callable(subclass.initialize) and hasattr(subclass, 'shutdown')and callable(subclass.shutdown) and hasattr(subclass, 'componentMain')and callable(subclass.componentMain) or NotImplemented)
        

        @abc.abstractmethod
        def initialize(self):
                raise NotImplementedError

        @abc.abstractmethod
        def shutdown(self):
                raise NotImplementedError

        @abc.abstractmethod
        def componentMain(self):
                raise NotImplementedError


class GenericThreadedComponent(IComponent,Thread,metaclass=abc.ABCMeta):
        def __init__(self):
                ##print('generaic therefjsdl')
                self._mustShutdown = False
                print('in init of generic threaded component')
                Thread.__init__(self)
        
        @abc.abstractmethod
        def initialize(self):
                self._mustshutdown = False
                print("here")
                Thread.__init__(self)
                self.start()
                

        @abc.abstractmethod
        def shutdown(self):
                self._mustshutdown = True 
        
        def componentMain(self):
                raise NotImplementedError

        @abc.abstractmethod
        def run(self):
                self.componentMain()



##import time             
##class first(GenericThreadedComponent):
##        def initialize(self):
##                print('first runnung')
##                self._mustshutdown = False
##        def shutdown(self):
##                self._mustshutdown = True
##                print('shutting down')
##        def componentMain(self):
##                while not(self._mustshutdown):
##                        print('Hello world')
##                        time.sleep(1)
##        def run(self):
##                self.componentMain()
##
##class firststopper(GenericThreadedComponent):
##        def __init__(self,first):
##                self._first = first
##                Thread.__init__(self)
##        def initialize(self):
##                print('first stopper running')
##                self._mustshutdown = False
##        def shutdown(self):
##                print('shutting down')
##        def componentMain(self):
##                print('first stopperr sleeping')
##                time.sleep(10)
##                print('attempting to shut down first')
##                self._first.shutdown()
##                self.shutdown()
##        def run(self):
##                self.componentMain()
##        
##
##a = first()
##b = firststopper(a)
##a.initialize()
##a.start()
##b.start()

        


