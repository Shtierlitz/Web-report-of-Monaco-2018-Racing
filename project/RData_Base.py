import sqlite3


class RData_Base:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = '''SELECT * FROM report'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения БД")
        return []

    def add_data(self, title, data):
        try:
            self.__cur.execute("INSERT INTO report VALUES(NULL, ?, ?)", (title, data))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления данных в db" +str(e))
            return False
        return True

