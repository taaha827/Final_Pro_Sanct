import pymysql

class Database:

    host = 'localhost'
    user = 'root'
    password = ''
    db = 'daraz'
    connection =None
    cursor = None
    def __init__(self):

        self.connection = pymysql.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()



    def query(self, query):
        cursor = self.connection.cursor( pymysql.cursors.DictCursor )
        cursor.execute(query)

        return cursor.fetchall()

    def __del__(self):
        self.connection.close()
