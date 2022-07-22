class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
        
class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.
 
    message: explanation of the error.
 
    """
    def __init__(self, message):
        self.message = message
        
class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.gen = self.f()
        
    def read(self):
        try:
            self.capacity += 1
            return next(self.gen)
        except StopIteration:
            raise BufferEmptyException("Circular buffer is empty")
        
    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException("Circular buffer is full")
            
    def overwrite(self, data):
        if len(self.buffer) >= self.capacity:
            next(self.gen)    
        self.buffer.append(data)
        
    def clear(self):
        self.buffer = []
        
    def f(self):
       for i in self.buffer:
           yield i
