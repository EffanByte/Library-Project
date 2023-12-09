class Room:
    def __init__(self, room_no, qalam_id, reservation_time, reservation_status, db_connection):
        self.room_no = room_no
        self.qalam_id = qalam_id
        self.reservation_time = reservation_time
        self.reservation_status = reservation_status
        self.db_connection = db_connection

    def reserve_room(self, user_id, reservation_time, reservation_status='Reserved'):
        call_proc = "CALL ReserveRoom(%s, %s, %s, %s)"
        values = (self.room_no, user_id, reservation_time, reservation_status)
        self.db_connection.cursor.execute(call_proc, values)
        self.db_connection.conn.commit()

    def cancel_reservation(self, room_id):
        call_proc = "CALL CancelReservation(%s)"
        self.db_connection.cursor.execute(call_proc, (room_id,))
        self.db_connection.conn.commit()
