from deck import Deck


def test_deck():
    my_deck=Deck()
    assert len(my_deck.cards)==52
    
    
def test_shuffle():
    my_deck=Deck()
    cards =my_deck.cards[:]
    my_deck.shuffle()
    assert  cards !=my_deck.cards
    
    
def test_hit():
    my_deck=Deck()
    last_card =my_deck.cards[-1]
    hitted_card=my_deck.hit()
    assert last_card ==hitted_card
    
def test_deck_count():
    my_deck= Deck()
    my_deck.hit()
    assert len(my_deck.cards)==51
    