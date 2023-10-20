import psycopg2
from decimal import Decimal


class DBConn:
    def __init__(self, db_name, user, password, host, port):
        self.dbname = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = self.connect_db()

    def connect_db(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        return conn

    def read_record(self, table):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {table}")
        table = cur.fetchall()
        t_table = []
        for row in table:
            t_row = []
            for value in row:
                if isinstance(value, Decimal):
                    cur.execute("SELECT ROUND(%s::numeric, 1)", (value,))
                    truncated_value = cur.fetchone()[0]
                    t_row.append(float(truncated_value))
                else:
                    t_row.append(value)
            t_table.append(t_row)
        cur.close()
        return t_table

    def create_record(self, table, new_record):
        cur = self.conn.cursor()
        keys = new_record.keys()
        values = [new_record[key] for key in keys]
        placeholders = ', '.join(['%s'] * len(keys))
        insert_query = f"INSERT INTO {table} ({', '.join(keys)}) VALUES ({placeholders})"
        cur.execute(insert_query, values)
        self.conn.commit()
        cur.close()

    def update_record(self, table, id_column, record_id, new_values):
        cur = self.conn.cursor()
        update_query = f"UPDATE {table} SET "
        for key, value in new_values.items():
            update_query += f"{key} = %s, "
        update_query = update_query.rstrip(', ')  # Remove the trailing comma and space
        update_query += f" WHERE {id_column} = %s"
        cur.execute(update_query, list(new_values.values()) + [record_id])
        self.conn.commit()
        cur.close()

    def delete_record(self, table, record_id):
        cur = self.conn.cursor()
        delete_query = f"DELETE FROM {table} WHERE id = %s"
        cur.execute(delete_query, [record_id])
        self.conn.commit()
        cur.close()
