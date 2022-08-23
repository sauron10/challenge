from sqlalchemy import (Column,Integer,String)
from sqlalchemy.orm import (declarative_base)

Base = declarative_base()

'''Class representing the model of the solution inside the database'''
class Solution(Base):
  __tablename__ = 'diagrams'
  size = Column(Integer)
  points = Column(String, primary_key=True)

  def __repr__(self) -> str:
    return f'size: {self.size}, solution: {self.points}'