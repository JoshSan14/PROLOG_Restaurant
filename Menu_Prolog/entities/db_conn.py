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

    def truncate_numeric_value(self, value, decimal_places=2):
        if isinstance(value, Decimal):
            cur = self.conn.cursor()
            cur.execute("SELECT ROUND(%s::numeric, %s)", (value, decimal_places))
            truncated_value = cur.fetchone()[0]
            cur.close()
            return float(truncated_value)
        return value

    @staticmethod
    def boolean_to_words(boolean):
        if boolean:
            return "Si"
        else:
            return "No"

    def convert_and_truncate_records(self, records, decimal_places):
        t_records = []
        for record in records:
            record = [self.boolean_to_words(value) if isinstance(value, bool) else value for value in record]
            t_row = [self.truncate_numeric_value(value, decimal_places) for value in record]
            t_records.append(t_row)
        return t_records

    def retrieve_single_record_with_custom_order(self, table_name, record_id, column_order, decimal_places=2):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT {', '.join(column_order)} FROM {table_name} WHERE id = %s", (record_id,))
            record = cur.fetchone()
            cur.close()
            record = [self.boolean_to_words(value) if isinstance(value, bool) else value for value in record]
            t_record = [self.truncate_numeric_value(value, decimal_places) for value in record]
            return t_record
        except Exception as e:
            print(f"Error: {e}")

    def retrieve_all_records(self, table_name, decimal_places=2):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {table_name} ORDER BY id ASC")
        records = cur.fetchall()
        t_records = self.convert_and_truncate_records(records, decimal_places)
        cur.close()
        return t_records

    def retrieve_all_records_with_custom_order(self, table_name, column_order, decimal_places=1):
        try:
            cur = self.conn.cursor()
            cur.execute(f"SELECT {', '.join(column_order)} FROM {table_name} ORDER BY id ASC")
            records = cur.fetchall()
            t_records = self.convert_and_truncate_records(records, decimal_places)
            cur.close()
            return t_records
        except Exception as e:
            print(f"Error: {e}")

    def insert_record(self, table_name, new_record):
        cur = self.conn.cursor()
        keys = new_record.keys()
        values = [new_record[key] for key in keys]
        placeholders = ', '.join(['%s'] * len(keys))
        insert_query = f"INSERT INTO {table_name} ({', '.join(keys)}) VALUES ({placeholders})"
        cur.execute(insert_query, values)
        self.conn.commit()
        cur.close()

    def update_record(self, table_name, id_column, id_record, new_values):
        cur = self.conn.cursor()
        update_query = f"UPDATE {table_name} SET "
        for key, value in new_values.items():
            update_query += f"{key} = %s, "
        update_query = update_query.rstrip(', ')
        update_query += f" WHERE {id_column} = {id_record}"
        cur.execute(update_query, list(new_values.values()))
        self.conn.commit()
        cur.close()

    def delete_record(self, table_name, record_id):
        cur = self.conn.cursor()
        delete_query = f"DELETE FROM {table_name} WHERE id = %s"
        cur.execute(delete_query, [record_id])
        self.conn.commit()
        cur.close()
