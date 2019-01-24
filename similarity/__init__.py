class Similarity:
    def __init__(self, sample, input):
        self.sample = sample
        self.input = input
        self.rate = 0

        if self.sample.__len__() < self.input.__len__():
            self.sample, self.input = self.input, self.sample

    def getDifferentPercent(self):
        sample_lenght = self.sample.__len__()
        input_lenght = self.input.__len__()

        lenght_different_percent = (sample_lenght - input_lenght) * 100 / sample_lenght
        return lenght_different_percent

    def compare(self):
        margin = self.getDifferentPercent() * self.sample.__len__() / 100; same = 0

        for id, w in enumerate(self.input):
            for idx, sample in enumerate(self.sample[int(id):int(id+margin+1)]):
                if w == sample: same += 1

        if margin != 0 and same != 0:
            self.rate = ((same * 100 / self.input.__len__()) / 2) / margin + (100 - self.getDifferentPercent()) / 2
        elif same != 0:
            self.rate = ((same * 100 / self.input.__len__()) / 2) + (100 - self.getDifferentPercent()) / 2
        else:
            self.rate = 0

        return self.rate


name = 'similarity'