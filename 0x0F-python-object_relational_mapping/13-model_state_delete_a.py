#!/usr/bin/python3
"""deleting all State objects with a name containing
the letter a from hbtn_0e_6_usa"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from sqlalchemy.schema import Table

    myEng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                          pool_pre_ping=True)
    Base.metadata.create_all(myEng)

    mySess = Session(myEng)
    for s in mySess.query(State).filter(State.name.like('%a%')):
        mySess.delete(s)
    mySess.commit()
    mySess.close()
