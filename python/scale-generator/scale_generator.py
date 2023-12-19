sharp = ['C', 'a', 'G', 'D', 'A', 'E', 'B', 'F♯', 'e', 'b', 'f#', 'c#', 'g#', 'd#']
flat = ['F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'd', 'g', 'c', 'f', 'bb', 'eb']
scale_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
scale_flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
class Scale:
    def __init__(self, tonic):
        self.tonic = tonic
        self.scale = scale_sharp if tonic in sharp else scale_flat
        
    def chromatic(self):
        return self.scale[self.scale.index(self.tonic.capitalize()):] + self.scale[:self.scale.index(self.tonic.capitalize())]
    def interval(self, intervals):
        self.chrom_scale = self.chromatic()
        self.music_scale = []
        self.intervals = intervals
        self.note = 0
        self.skip = 0
        while self.note < len(self.chrom_scale):
            self.music_scale.append(self.chrom_scale[self.note])
            if self.intervals[self.skip] == 'A':
                self.note += 3
            elif self.intervals[self.skip] == 'M':
                self.note += 2
            elif self.intervals[self.skip] == 'm':
                self.note += 1
            self.skip += 1
        return self.music_scale + [self.music_scale[0]]
