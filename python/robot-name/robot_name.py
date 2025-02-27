import random

class Robot:
    
    names = set()
    
    def __init__(self):
        Robot.reset(self)
        
    def reset(self):
        self.name = Robot.rand_name()
        while self.name in Robot.names:
            self.name = Robot.rand_name()
        Robot.names.add(self.name)
        
    def rand_name():
        a = chr(random.randint(65, 90))
        b = chr(random.randint(65, 90))
        c = random.randint(0,9)
        d = random.randint(0,9)
        e = random.randint(0,9)
        return f'{a}{b}{c}{d}{e}'
