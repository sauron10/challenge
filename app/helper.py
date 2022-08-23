from sqlalchemy.orm import (Session)
from sqlalchemy import create_engine
from sqlalchemy.exc import (OperationalError,IntegrityError)
from solution import Solution

engine = create_engine('postgresql://postgres:postgres@challenge_db:5432/solutions',echo=False,future=True)

def write_to_db(queue:list[Solution],in_db:bool) -> tuple[bool,bool]:
    with Session(engine) as session:
      try:
        session.add_all(queue)
        session.commit()
        return True,False
      except OperationalError as e:
        print('There was an error connecting to the database')
        print('Still the solution will be printed...')
        return False,False
      except IntegrityError as e:
        if not in_db:
          print('The solution was in the db already')
          print('It is still getting your result tho ...')
        return True,True
      except Exception as e:
        print("There was an error with the database",e)
        return False,False