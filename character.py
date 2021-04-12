#Les personnages gagneront des points supplémentaires en fonction des tabs
class character:
    def __init__(self,name):
        self.name = name
        # Corentin wins more points using words of subjectab
        if name == 'Corentin' :
            self.bonus = 2 
        else if name == 'Juliette' :
        # Juliette wins more points using words of vertab
            self.bonus = 2
        else if name == 'Jean' : 
        # Jean wins more points using words of complementab
            self.bonus = 2
        else if name == 'Aurélie':
        # Aurélie wins more points using words of endtab
            self.bonus = 2
        else if name == 'Francis':
        # Francis wins more points using words of linktab
            self.bonus = 2

    def __str__(self):
        return self.name              
