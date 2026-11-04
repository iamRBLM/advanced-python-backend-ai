from abc import ABC, abstractmethod

class DB_Connector(ABC):
    @abstractmethod
    def connect(self)->None:
        pass

    def disconnect(self)->None:
        print("Disconnecting generic logic....")


class sql_server_connector(DB_Connector):
    def connect(self)->None:
        print("Connecting to sql server successfully....")


#db = DB_Connector()-> Can't instantiate abstract class DB_Connector with abstract method connect
db = sql_server_connector()
db.connect()
db.disconnect()


