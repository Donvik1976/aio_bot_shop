from sqlite3 import connect


class DatabaseManager:

    def __init__(self, path):
        self.conn = connect(path)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def create_tables(self):
        # Создание таблицы продуктов
        self.query(
            'CREATE TABLE IF NOT EXISTS products (idx text, title text, '
            'body text, photo blob, price int, tag text)')
        # Создание таблицы заказов
        self.query(
            'CREATE TABLE IF NOT EXISTS orders (cid int, usr_name text, '
            'usr_address text, products text)')
        # Создание таблицы корзины
        self.query(
            'CREATE TABLE IF NOT EXISTS cart (cid int, idx text, '
            'quantity int)')
        # Создание таблицы категории
        self.query(
            'CREATE TABLE IF NOT EXISTS categories (idx text, title text)')
        # Создание таблицы кошелёк
        self.query('CREATE TABLE IF NOT EXISTS wallet (cid int, balance real)')
        # Создание таблицы вопросы
        self.query(
            'CREATE TABLE IF NOT EXISTS questions (cid int, question text)')

    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    # получение из базы данных одного значения
    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    # получение из базы данных всех значения
    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
