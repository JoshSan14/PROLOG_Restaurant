import sys
import PyQt5.QtWidgets as Qtw
import PyQt5.QtGui as Qtg
from PyQt5.QtCore import Qt as Qt
from ingredient import *


class Utils:

    @staticmethod
    def insert_values(db_conn, table_name, record_dict):
        try:
            db_conn.insert_record(table_name, record_dict)
        except Exception as e:
            print(f"Error inserting record: {e}")

    @staticmethod
    def load_values(db_conn, table_name, col_ord, data_tbl):
        try:
            records = db_conn.retrieve_all_records_with_custom_order(table_name, col_ord)

            data_tbl.setRowCount(0)

            for row_num, record in enumerate(records):
                data_tbl.insertRow(row_num)
                for col_num, value in enumerate(record):
                    item = Qtw.QTableWidgetItem(str(value))
                    data_tbl.setItem(row_num, col_num, item)

            data_tbl.resizeColumnsToContents()
        except Exception as e:
            print(f"Error loading records: {e}")

    @staticmethod
    def update_values(db_conn, table_name, id_column, id_object, update_dict):
        try:
            db_conn.update_record(table_name, id_column, id_object, update_dict)
        except Exception as e:
            print(f"Error updating record: {e}")

    @staticmethod
    def delete_values(db_conn, table_name, data_tbl):
        try:
            selected_row = data_tbl.currentRow()
            item = data_tbl.item(selected_row, 0)
            id_record = item.text()
            db_conn.delete_record(table_name, id_record)
        except Exception as e:
            print(f"Error deleting record: {e}")

    @staticmethod
    def get_single_record(db_conn, table_name, data_tbl, col_ord):
        try:
            selected_row = data_tbl.currentRow()
            id_item = data_tbl.item(selected_row, 0)
            id_record = id_item.text()
            record = db_conn.retrieve_single_record_with_custom_order(table_name, id_record, col_ord)
            return record
        except Exception as e:
            print(f"Error reading record: {e}")

    @staticmethod
    def set_combobox_value(combobox, value):
        index = combobox.findText(value.capitalize())
        if index >= 0:
            combobox.setCurrentIndex(index)

    @staticmethod
    def word_to_boolean(value):
        if (value.capitalize() == "True") or (value.capitalize() == "Si"):
            return True
        else:
            return False

    @staticmethod
    def set_checkbox_state(checkbox, value):
        if Utils.word_to_boolean(value):
            checkbox.setChecked(True)
        else:
            checkbox.setChecked(False)

    @staticmethod
    def capitalize_tuples(tuples):
        capitalized_tuples = []
        for item in tuples:
            capitalized_tuple = tuple(word.capitalize() if isinstance(word, str) else word for word in item)
            capitalized_tuples.append(capitalized_tuple)
        return capitalized_tuples

    @staticmethod
    def open_dialog(dialog):
        dialog.exec_()
