class Clock:
    
    def __init__(self, hour, minute):
        self.hour = (hour + minute//60)%24
        self.minute = minute%60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        if self.hour < 10:
            self.hour = f"0{self.hour}"
        if self.minute < 10:
            self.minute = f"0{self.minute}"
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute = self.hour * 60 + self.minute + minutes
        self.hour = (self.minute//60)%24
        self.minute = self.minute%60
        return self

    def __sub__(self, minutes):
        self.minute = self.hour * 60 + self.minute - minutes
        self.hour = (self.minute//60)%24
        self.minute = self.minute%60
        return self

