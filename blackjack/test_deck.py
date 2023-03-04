from deck import Deck


def test_deck():
    my_deck=Deck()
    assert len(my_deck.cards)==52