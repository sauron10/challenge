from time import time
from point import Point
from diagonals import Diagonals
from solution import Solution
from helper import write_to_db

def get_answer(queens:list,
                size:int,
                solution_queue:list[Solution],
                x:int=0,
                diagonal_list:list[Diagonals]=[],
                solution:list[Point]=[],
                status:bool=True,
                in_db:bool=False) -> tuple[int,bool,bool]:
  if not queens:
    if(status):
      solution_queue.append(Solution(size=size,points=str(solution)))
      if len(solution_queue) > 10000:
        status,in_db = write_to_db(solution_queue,in_db)
        solution_queue.clear()
    return 1,status, in_db
  sum = 0
  for y in queens:
    diagonal = Diagonals(Point(x,y))
    if ([d.up for d in diagonal_list if d.up == diagonal.up] or
        [d.down for d in diagonal_list if d.down == diagonal.down]):
      continue
    diagonal_list.append(diagonal)
    solution.append(Point(x,y))
    add,status,in_db = get_answer([n for n in queens if n!=y],size,solution_queue,x+1,diagonal_list.copy(),solution.copy(),status,in_db)
    sum += add
    diagonal_list.pop()
    solution.pop()
  return sum,status,in_db #Reaching the end of the row


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


def main(size:int) -> int:
  print('Processing...')
  start_time = time()
  solutions = solve(size)
  print(f'{solutions} possible answers in {round(time() - start_time,2)} seconds')
  return solutions


if __name__ == '__main__':
  size = input('Dimension: ')
  main(int(size))