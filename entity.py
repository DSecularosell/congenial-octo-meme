
from typing import Tuple

class Entity:
    """
    An object used to represent interactable entities like enemies, items, players etc
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]) -> None:
        self.x=x
        self.y=y
        self.char=char
        self.color=color
    
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
        
        