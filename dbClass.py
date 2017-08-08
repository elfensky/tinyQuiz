class mySQL:
    def __init__(self):
        import mysql.connector as connector

        # #login for db@pi
        # self.__dsn = {
        #     "host": "localhost",
        #     "user": "andrei",
        #     "passwd": "admin",
        #     "db": "db_quiz"
        # }

        #login for db@laptop
        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "admin",
            "db": "db_quiz"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor() #ADDED (dictionary=True) so I get dict results. Life is good now.

    def getDataFromCustomColumn(self, columnName, tableName):
        # Query met parameters
        sqlQuery = "SELECT {param1} FROM {param2}"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=columnName, param2=tableName)

        # create cursor
        self.__cursor = self.__connection.cursor()
        # use cursor
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        # delete cursor
        self.__cursor.close()
        return result

    def getDataFromCustomRow(self, tableName, rowName, value):
        # Query met parameters
        sqlQuery = "SELECT * FROM {param1} WHERE {param2} LIKE '{param3}' LIMIT 1"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=tableName, param2=rowName, param3=value)

        # create cursor
        self.__cursor = self.__connection.cursor()
        # use cursor
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        # delete cursor
        self.__cursor.close()
        return result

    def setDataToDatabase(self, tableName, username, password):
        # Query met parameters
        # sqlQuery = "INSERT INTO {param1} ({param2}) VALUES ({param3})"
        sqlQuery = "INSERT INTO {param1} (username, password) VALUES (%s, %s)"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=tableName)

        self.__cursor.execute(sqlCommand, (username, password))
        self.__connection.commit()
        self.__cursor.close()





















