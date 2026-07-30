#we are importing os to use the .env file to protect database password

import os
from dotenv import load_dotenv

load_dotenv()           #it loads the env file into environment


#python and sqlalchemy part start here:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL=os.getenv("DATABASE_URL")

DATABASE_URL="postgresql://postgres:rameezpostgres78@localhost:5432/Student_Record_Management_System"

engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)




#mistakes made by me in that file:
# I remembered again loading .env file and importing os
# I wrote DATABASE_URL=os.getenv("DATABASE_URL") before the both sqlalchemy imports which was wrong syntax,later i fixes that
#I forgot to write commas in sessionmaker() False,ones