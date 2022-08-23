from sqlalchemy import Table,Column,String,Integer,MetaData
meta = MetaData()

answers = Table(
  'answers', meta,
  Column('points',String, primary_key=True ),
  Column('size',Integer)
)
