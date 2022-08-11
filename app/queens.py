from sqlalchemy import (Column,
                        Integer,
                        String,
                        create_engine)
from sqlalchemy.orm import (declarative_base,
                            Session)
from psycopg2 import (OperationalError,
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
  def __init__(self,x:int,y:int):
    self.x = x
    self.y = y

  def __str__(self) -> str:
    return f'({self.x},{self.y})'

  def __repr__(self) -> str:
    return f'({self.x},{self.y})'

def getAnswerNumber(arr: list,size:int,answer:list=[],dangerPoints:list=[],x:int = 0) -> int:
  if size == 2 : return 0
  if size == 3 : return 0
  if size == 1 : return 1
  if not arr:
    print(answer)
    global CONNECTION_AVAILABLE
    if CONNECTION_AVAILABLE:
      with Session(engine) as session:
        sol = Solution(size=size,points=str(answer))
        session.add(sol)
        try:
          session.commit()
        except OperationalError:
          print('There was an error connecting to the database')
          CONNECTION_AVAILABLE = False
        except IntegrityError:
          print('The solution was in the db already')
        except Exception as e:
          print("There was an error with the database",e)
          CONNECTION_AVAILABLE = False

    answer.pop()
    return 1 
  sum=0
  for y in arr:
    # print(f'({x},{y}) -> {dangerPoints}\n')
    if recursiveSearch(str(Point(x,y)),dangerPoints) : 
      # print(f'Killed Line ({x},{y})')
      continue
    if(x<size-1):
      diagonal = getDiagonal(Point(x,y),size)
      dangerPoints.append(diagonal)
    answer.append(str(Point(x,y)))
    sum = sum + getAnswerNumber([x for x in arr if x != y],size,answer,dangerPoints,x+1)
  if dangerPoints: dangerPoints.pop()
  if answer : answer.pop()
  return sum # Being here means I have passed through all possible combinations

def recursiveSearch(element:any,arr:list):
  for s in arr:
    if isinstance(s,list): 
      if recursiveSearch(element,s):  
        return True
    if element in arr: return True
  return False


def getDiagonal(point:Point,size:int) -> list:
  # print(point,size)
  diagonals = []
  x = point.x
  y = point.y
  while x<size-1 and y<size-1:
    x += 1
    y += 1
    diagonals.append(str(Point(x,y)))
  x,y = [point.x,point.y]
  while x>0 and y>0:
    x -= 1
    y -= 1
    diagonals.append(str(Point(x,y)))
  x,y = [point.x,point.y]
  while x>0 and y<size-1:
    y +=1
    x -= 1
    diagonals.append(str(Point(x,y)))
  x,y = [point.x,point.y]
  while x<size-1 and y>0:
    x +=1
    y -= 1
    diagonals.append(str(Point(x,y)))
  # print(diagonals)
  return diagonals

def gridGenerator(size:int) -> list:
  for i in range(size):
    for j in range(size):
      yield [i,j]

def main(size):
  solutions = getAnswerNumber(list(range(size)),size)
  print(solutions)
  return solutions

if __name__ == '__main__':
  size = input('Dimension: ')
  main(int(size))