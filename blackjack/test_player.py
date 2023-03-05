from player import Player
from card import Card




def test_calculate_player_points():
    #given
    card=Card('spades', 2)
    card2=Card('hearts', 5)
    player=Player()
    
    
    #when
    player.take_card(card)
    player.take_card(card2)
    
    #then
    
    assert player.calculate_points()== 7
    
    
    
def test_calculate_player_points_two_aces():
    card=Card('spades', 'Ace')
    card2=Card('hearts', 'Ace')
    player=Player()
    
    player.take_card(card)
    player.take_card(card2)
    
    #then
    
    assert player.calculate_points()== 21
    
    
def test_calculate_player_points_one_ace():
    card=Card('spades', 'Ace')
    card2=Card('hearts', '2')
    player=Player()
    
    player.take_card(card)
    player.take_card(card2)
    
    #then
    
    assert player.calculate_points()== 13