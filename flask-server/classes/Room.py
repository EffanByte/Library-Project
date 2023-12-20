import mysql.connector

# Modify the Room class in your room.py file
class Room:
    def __init__(self, room_no, qalam_id, reservation_time, reservation_status, db_connection):
        self.room_no = room_no
        self.qalam_id = qalam_id
        self.reservation_time = reservation_time
        self.reservation_status = reservation_status
        self.db_connection = db_connection

    def reserve_room(self, user_id, reservation_status='Reserved'):
        query = "INSERT INTO Room (RoomNo, QalamID, ReservationTime, ReservationStatus) VALUES (%s, %s, %s, %s)"
        values = (self.room_no, user_id, self.reservation_time, reservation_status)
        self.db_connection.cursor.execute(query, values)
        self.db_connection.conn.commit()

    def cancel_reservation(self, room_id):
        query = "DELETE FROM Room WHERE RoomNo = %s"
        self.db_connection.cursor.execute(query, (room_id,))
        self.db_connection.conn.commit()

