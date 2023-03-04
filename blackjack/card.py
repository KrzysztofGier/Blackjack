"""Blackjack card game"""


class Card:
    
    possible_colors = {
        'spades': 'u\2664' ,
        'hearts': 'u\2661',
        'diamonds': '\u2662',
        'clubs': '\u2667'
    }
    
    possible_values= list(range(2, 11))+[
        'Ace',
        'Jack',
        'Queen',
        'King'
        
    ]
    
    
    def __init__(self, color, value ) -> None:
        self.color = self.possible_colors[color]
        if value not in self.possible_values:
            raise IndexError('Invalid card value')
        self.value= value
        
        
    def __repr__(self) -> str:
        return f'{self.value} -> {self.color}'
    
