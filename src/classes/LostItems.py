import mysql.connector

class LostItems:
    def __init__(self, item_id, qalam_id, item_description, date_reported, db_connection):
        self.item_id = item_id
        self.qalam_id = qalam_id
        self.item_description = item_description
        self.date_reported = date_reported
        self.db_connection = db_connection

    def report_lost_item(self, qalam_id, item_description, date_reported):
        query = "INSERT INTO LostItems (QalamID, ItemDescription, DateReported) VALUES (%s, %s, %s)"
        values = (qalam_id, item_description, date_reported)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()
