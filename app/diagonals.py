from point import Point

'''Class that describes a pair of diagonals for a certain point up and down'''
class Diagonals: 
  def __init__(self,point:Point) -> None:
    self.down = point.x - point.y
    self.up = point.x + point.y
  
  def __str__(self) -> str:
    return f'({self.up},{self.down})'
  
  def __repr__(self) -> str:
    return f'({self.up},{self.down})'