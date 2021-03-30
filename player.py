class player:
    def __init__(self,name,perso): 
        self.name = name
        self.points = 0
        self.perso = perso

    def __str__(self):
        return self.name