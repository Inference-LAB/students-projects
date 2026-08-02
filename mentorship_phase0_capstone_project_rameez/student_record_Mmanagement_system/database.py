#we are importing os to use the .env file to protect database password

import os
from dotenv import load_dotenv  

load_dotenv()           #it loads the env file into environment


#python and sqlalchemy part start here:

from sqlalchemy import create_engine    #engine s like bridge between postgresql and python
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL=os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL)

#this line is used to create all table that we define in models.py,we can write that line in main.py too,also import engine and Base there too
Base.metadata.create_all(bind=engine)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)




#mistakes made by me in that file:
# I remembered again loading .env file and importing os
# I wrote DATABASE_URL=os.getenv("DATABASE_URL") before the both sqlalchemy imports which was wrong syntax,later i fixes that
#I forgot to write commas in sessionmaker() False,ones