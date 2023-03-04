import pytest
from card import Card 


def test_create_card():
    card=Card('hearts', 'A')
    assert card.color=='u\2661'
    assert card.value=='A'
    
    
def test_create_wrong_value():
    with pytest.raises(IndexError) as message:
        card = Card('hearts', 'A')
        assert message == 'Invalid card value'
        
def test_card_representation():
    assert repr(Card('hearts', 'Ace')) == 'Ace -> u\2661' 