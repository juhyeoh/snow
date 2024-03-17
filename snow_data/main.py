from sqlalchemy.orm import sessionmaker
from config_setting import create_db_engine, Base
from operation_db import oper_db
    

def main():
    engine = create_db_engine()
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
    oper_db(session)

    session.close()

if __name__ == "__main__":
    main()
