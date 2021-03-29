from player import player

print('Player 1, Choose your username : ')
username1 = str(input())
p1 = player(username1)
print('Player2, Choose your username : ')
username2 = str(input())
p2 = player(username2)
print(p1.name + ' VS ' + p2.name + ' FIGHT !')

Turnp1 = 'Player 1, your turn.'
Turnp2 = 'Player 2, your turn.'
# 1. choose subject
# 2. Choose verb
# 3. Choose situation
# 4. Choose end
def round():

