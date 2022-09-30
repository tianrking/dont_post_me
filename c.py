import threading

class Singleton:
    _instance = None
    lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        else:
            with cls.lock:
                cls._instance = super().__new__(cls)
                return cls._instance

    def __init__(self, k):
        self.k = k

    def show_value(self):
        print(self.k)
    
    def show_id(cls):
        print(id(cls))
        
c = Singleton(1)
c.show_value()
c.show_id()

        
d = Singleton(2)
d.show_value()
d.show_id()
