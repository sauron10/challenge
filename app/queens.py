from time import time
from point import Point
from diagonals import Diagonals
from solution import Solution
from helper import write_to_db

'''To avoid creating sessions on every record write this accummulates 10000 records an the write them'''
def dump_to_db(solution_queue:list[Solution],in_db:bool) -> tuple[int,bool]:
  status,in_db = write_to_db(solution_queue,in_db)
  solution_queue.clear()
  return status,in_db


'''Recursively goes through the possibility tree of the queens vertically recursively and horizontally iteratively
and adds the number of answers for an n size board'''

def get_answer(queens:list,
                size:int,
                solution_queue:list[Solution],
                x:int=0,
                diagonal_list:list[Diagonals]=[],
                solution:list[Point]=[],
                status:bool=True,
                in_db:bool=False) -> tuple[int,bool,bool]:
  if not queens: # Break condition, the stack begins to shrink from here
    if(status):
      solution_queue.append(Solution(size=size,points=str(solution))) #Adds a solution to the queue for bulk db writting
      if len(solution_queue) > 10000: #Checks that the queue is big enough to be written in the db
        status,in_db = dump_to_db(solution_queue,in_db) # Dumps the solutions in memory to db to avoid high memory usage
    return 1,status, in_db
  sum = 0
  for y in queens: # Moves horizontally in the tree to visit all the nodes 
    diagonal = Diagonals(Point(x,y))
    if ([d.up for d in diagonal_list if d.up == diagonal.up] or
        [d.down for d in diagonal_list if d.down == diagonal.down]): # If the point is inside some bad diagonal kills the recursion there
      continue 
    diagonal_list.append(diagonal) # Adds the current point diagonal to the diagonal list
    solution.append(Point(x,y)) # Adds the current point to the solution 
    add,status,in_db = get_answer([n for n in queens if n!=y],size,solution_queue,x+1,diagonal_list.copy(),solution.copy(),status,in_db) #Recursion yehi
    sum += add
    diagonal_list.pop()
    solution.pop()
  return sum,status,in_db #Reaching the end of the row

'''Checks for easy cases and declares somer variables important for the database queue'''
def solve(size) -> int:
  if size == 2 : return 0
  if size == 3 : return 0
  if size == 1 : return 1
  solution_queue = []
  answer,status,in_db = get_answer(list(range(size)),
            size,
            solution_queue,
            )
  if status: write_to_db(solution_queue,in_db)
  return answer

'''Main method, also adds some strings to the shell for clarity of the information given'''
def main(size:int) -> int:
  print('Processing...')
  start_time = time()
  solutions = solve(size)
  print(f'{solutions} possible answers in {round(time() - start_time,2)} seconds')
  return solutions


if __name__ == '__main__':
  size = input('Dimension: ')
  main(int(size))