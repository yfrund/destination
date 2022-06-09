class Destination:

    def __init__(self, filepath):
        self.file = filepath
        self.distance = self._distance_converter()
        self.days = self.work_days()

    def _distance_converter(self):
        with open (self.file, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            tokens = [line.split() for line in lines]
            distance = tokens[3][5]
            metric = tokens[3][6]
            if metric == 'km':
                distance = int(distance)*1000
            return int(distance)

    def __gt__(self, other):
        return self.distance > other.distance

    def __repr__(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            return f.read()

    def work_days(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            tokens = [line.split() for line in lines]
            open_days = tokens[4][2:]
            return open_days

    def open_on(self, day):
        return day in self.days

    def shared_opening_days(self, other):
        shared = []
        for day in self.days:
            if day in other.days:
                shared.append(day)
        return shared

#to test
kunsthaus = Destination('zurich_sightseeing/kunsthaus')
grossmunster = Destination('zurich_sightseeing/grossmunster')
sprungli = Destination('zurich_sightseeing/sprungli')
# print (kunsthaus)
# print (kunsthaus > grossmunster)

print (kunsthaus.shared_opening_days(sprungli))

print (grossmunster > sprungli)

