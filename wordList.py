class wordList:
    def __init__(self):
        self.mainTab = []



    def fillMainTab(self):
        self.subjecTab = [
            'Your sister',
            'Your dad',
            'You',
            'Your skill',
            'Your IQ',
        ]
        self.verbTab = [
            'looks like',
            'is like',
            'eats',
            'loves',
            'sniff',
            'is',
        ]
        self.complementab = [
            'a fish',
            'a dog',
            'the floor',
            'a trash',
            'an empty hole',
            'idiot'
        ]
        self.endTab = [
            'hairless',
            'abandoned',
            'lost',
            'rotten',
            'so stupid'
        ]
        self.linkTab = [
            'and',
            'also',
            'too',
            'moreover',
        ]
        
    def __str__(self):
        return str(self.mainTab)