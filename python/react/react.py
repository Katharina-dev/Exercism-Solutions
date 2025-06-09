class Cell:
    
    def __init__(self):
        self._value = None
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, data):
        self._value = data
        for change in self.on_change:
            change()
    on_change = []
    
class InputCell(Cell):
    
    def __init__(self, initial_value):
        super().__init__()
        self._value = initial_value
        
class ComputeCell(Cell):
    
    def __init__(self, inputs, compute_function):
        super().__init__()
        self._callbacks = set()
        self._inputs = inputs
        self._compute_function = compute_function
        self.__calculate()
        for i in self._inputs:
            i.on_change.append(self.__calculate)
            
    def __calculate(self):
        old_value = self._value
        self._value = self._compute_function([i.value for i in self._inputs])
        if self._value != old_value:
            for callback in self._callbacks:
                callback(self._value)
                
    def add_callback(self, callback):
        self._callbacks.add(callback)
        
    def remove_callback(self, callback):
        if callback in self._callbacks:
            self._callbacks.remove(callback) 
