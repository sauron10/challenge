from sqlalchemy import (Column,
                        Integer,
                        String,
                        create_engine)
from sqlalchemy.orm import (declarative_base,
                            Session)

from sqlalchemy.exc import (OperationalError,
                            IntegrityError)

CONNECTION_AVAILABLE=True
Base = declarative_base()
engine = create_engine('postgresql://postgres:postgres@challenge-database-1:5432/solutions',echo=True,future=True)

class Solution(Base):
  __tablename__ = 'diagrams'
  id = Column(Integer,primary_key=True)
  size = Column(Integer)
  points = Column(String())

  def __repr__(self) -> str:
    return f'size: {self.size}, solution: {self.points}'

class Point:
  def __init__(self,x:int,y:int)-> None:
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f'({self.x},{self.y})'

  def __repr__(self) -> str:
    return f'({self.x},{self.y})'

class Diagonals: 
  def __init__(self,point:Point) -> None:
    self.down = point.x - point.y
    self.up = point.x + point.y
  
  def __str__(self) -> str:
    return f'({self.up},{self.down})'
  
  def __repr__(self) -> str:
    return f'({self.up},{self.down})'

def getAnswer(arr:list,size:int,x:int=0,diagonalList:list[Diagonals]=[],solution:list[Point]=[]) -> int:
  if size == 2 : return 0
  if size == 3 : return 0
  if size == 1 : return 1
  if not arr:
    # print(solution)
    global CONNECTION_AVAILABLE
    if CONNECTION_AVAILABLE:
      with Session(engine) as session:
        try:
          sol = Solution(size=size,points=str(solution))
          session.add(sol)
          session.commit()
        except OperationalError as e:
          print('There was an error connecting to the database')
          CONNECTION_AVAILABLE = False
        except IntegrityError:
          print('The solution was in the db already')
        except Exception as e:
          print("There was an error with the database",e)
          CONNECTION_AVAILABLE = False 
    return 1
  sum = 0
  for y in arr:
    diagonal = Diagonals(Point(x,y))
    if ([d.up for d in diagonalList if d.up == diagonal.up] or
        [d.down for d in diagonalList if d.down == diagonal.down]):
      continue
    diagonalList.append(diagonal)
    solution.append(Point(x,y))
    sum += getAnswer([n for n in arr if n!=y],size,x+1,diagonalList.copy(),solution.copy())
    diagonalList.pop()
    solution.pop()
  return sum #Reaching the end of the row

def main(size):
  solutions = getAnswer(list(range(size)),size)
  print(solutions)
  return solutions
  

if __name__ == '__main__':
  size = input('Dimension: ')
  main(int(size))