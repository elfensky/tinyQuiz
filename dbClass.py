class mySQL:
    def __init__(self):
        import mysql.connector as connector

        #login for db@pi
        self.__dsn = {
            "host": "localhost",
            "user": "user",
            "passwd": "password",
            "db": "db_quiz"
        }

        #follow the guide on instructables to import db onto the RPi

        # #login for db@laptop
        # self.__dsn = {
        #     "host": "localhost",
        #     "user": "root",
        #     "passwd": "admin",
        #     "db": "db_quiz"
        # }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor() #ADDED (dictionary=True) so I get dict results. Life is good now.

    # ------ GET ------#
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

    def getQuestionsByCategory(self, category):
        # import random
        # Query met parameters
        sqlQuery = "SELECT * FROM tblquestions " \
                   "JOIN tblcategories ON tblcategories.IDcategory = tblquestions.IDcategory " \
                   "WHERE tblcategories.Description='{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=category)

        # create cursor
        self.__cursor = self.__connection.cursor()
        #ADDED (dictionary=True) so I get dict results. Life is good now.
        # use cursor
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        # delete cursor
        self.__cursor.close()
        return result ##not needed anymore, shuffle order inside function.
        # shuffled_result = random.sample(result, len(result))
        # return shuffled_result

    def getCustomQuery(self, query):
        # Query met parameters
        sqlQuery = "{param1}"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=query)

        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        self.__cursor.close()
        return result

    # ------ SET ------ #
    def setLoginDataToDatabase(self, tableName, username, password):
        # Query met parameters
        # sqlQuery = "INSERT INTO {param1} ({param2}) VALUES ({param3})"
        sqlQuery = "INSERT INTO {param1} (username, password) VALUES (%s, %s)"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=tableName)

        self.__cursor.execute(sqlCommand, (username, password))
        self.__connection.commit()
        self.__cursor.close()

    def setScoreDataToDatabase(self, tableName, IDuser, IDcategory, IDquestion, answer, datetime):
        sqlQuery = "INSERT INTO {param1} (IDuser, IDcategory, IDquestion, answer, datetime) VALUES (%s, %s, %s, %s, %s)"
        sqlCommand = sqlQuery.format(param1=tableName)
        # Combineren van de query en parameter
        self.__cursor.execute(sqlCommand, (IDuser, IDcategory, IDquestion, answer, datetime))
        self.__connection.commit()
        self.__cursor.close()

    def setGameDataToDatabase(self, tableName, IDuser, IDcategory, correct):
        # Query met parameters
        # sqlQuery = "INSERT INTO {param1} ({param2}) VALUES ({param3})"
        sqlQuery = "INSERT INTO {param1} (IDuser, IDcategory, correct) VALUES (%s, %s, %s)"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=tableName)

        self.__cursor.execute(sqlCommand, (IDuser, IDcategory, correct))
        self.__connection.commit()
        self.__cursor.close()

    def setCustomQuery(self, query):
        sqlQuery = "{param1}"
        sqlCommand = sqlQuery.format(param1=query)
        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        self.__cursor.close()












