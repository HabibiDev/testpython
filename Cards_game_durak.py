import random

class Player:

	def __init__(self, cards, name, rank):
		self.name='player№'+str(name+1)
		self.cards=cards
		self.rank=rank

def mysort(sortlist):
	return int(sortlist.rank)
#Create deck of cards
Card_Rank_list=['06', '07', '08', '09', '10', '11', '12', '13', '14']
Card_dict_realname={'11':'J', '12':'Q', '13':'K', '14':'A'}
Colours_list=['hearts', 'diamond', 'club', 'spade']
Card_deck=[]
for name in Card_Rank_list:
	for mast in Colours_list:
		Card_deck.append(str(name)+'-'+str(mast))

try:
	n=int(input('\nPlease choose amount of players(2-6):'))
except ValueError:
	print('Wrong input format')
if n<=6:
#Mix deck of cards
	random.shuffle(Card_deck)
#Determination of trump colour 
	Trump_colour=random.choice(Colours_list) 
	print('\nTrump colour: {0}\n'.format(Trump_colour))
	
	cards_on_hands=[]
	players=[]
#Players get their cards	
	for player in range(n):
		for card in range(6):
			cards_on_hands.append(random.choice(Card_deck))
			Card_deck=list(set(Card_deck).difference(cards_on_hands))
#Calculate rank of cards		
		rank=0 
		for card in cards_on_hands:
			if card[3]==Trump_colour[0]:
				rank+=int(card[0:2])*10
			else:
				rank+=int(card[0:2])
#Create list of players with their cards, and rating of cards
		players.append(Player(cards_on_hands, player, rank))
		cards_on_hands=[]
#Assign name of cards 
	for player in players:
		for card in range(len(player.cards)):
			for key in Card_dict_realname.keys():
				if player.cards[card].startswith(key):
					player.cards[card]=str(Card_dict_realname[key]+player.cards[card][2:])
		print('\n{0}:{1}\n'.format(player.name, player.cards))
		print()
#Sort list of players by rank
	players.sort(key=mysort, reverse=True)
	print('\nPlayer with the strongest set of cards: {0}\n'.format(players[0].name))

else:
	print('The amount of players must be more than 2 and less than 6')
	





