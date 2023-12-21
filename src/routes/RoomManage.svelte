<!-- RoomManage.svelte -->

<script>
  import axios from 'axios';
   import { onMount } from 'svelte';
  let selectedRoom = null;
  let selectedDate = null; // Add a variable to store the selected date
let rooms = [];

  const timeSlots = [
    '9:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00',
    '15:00:00', '16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00'
  ];


  
  function getNext7Days() {
    const today = new Date();
    return Array.from({ length: 7 }, (_, i) => {
      const date = new Date(today);
      date.setDate(today.getDate() + i);
      updateTable();
      return date.toISOString().split('T')[0];
    });
  }
  function updateTable() {
    // Logic to update the table based on the selected room
  }

 function removeBooking(roomId, timing) {
    // Logic for removing the booking from the selected room and timing
    const room = rooms.find(room => room.id === roomId);
    const timingIndex = room.bookedTimings.indexOf(timing);

    if (timingIndex !== -1) {
      // Remove booking locally
      room.bookedTimings.splice(timingIndex, 1);
      room.bookedBy.splice(timingIndex, 1);

      // Communicate with the backend to cancel the reservation
      cancelReservation(roomId, timing);
    }
  }

 async function cancelReservation(roomId, timing) {
    try {
      const response = await fetch('http://localhost:8001/api/rooms/cancel', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          RoomNo: roomId,
          ReservationTime: timing,
        }),
      });

      if (response.ok) {
        console.log('Reservation canceled successfully');
      } else {
        console.error('Failed to cancel reservation');
      }
    } catch (error) {
      console.error('Error during reservation cancelation:', error);
    }
  }

  let hasMounted = false; // Add a variable to check if the component has mounted
  // Initialize the selectedDate with today's date
  onMount(async () => {
    // Fetch rooms data from the API only once when the component mounts
    if (!hasMounted) {
      try {
        const response = await axios.get('http://localhost:8000/api/rooms');
        rooms = response.data; // Assuming the API response contains an array of room data
      } catch (error) {
        console.error('Error fetching rooms:', error);
      }

      // Initialize the selectedDate with today's date
      const today = new Date().toISOString().split('T')[0];
      selectedDate = today;
      console.log(selectedDate);
      console.log(rooms)
      // Set hasMounted to true to prevent further calls to onMount
      hasMounted = true;
    }
  });
function TimeBooked(roomNo, selectedDate, selectedTime) {
    const selectedRoomData = rooms.filter(room => room.RoomNo == roomNo);

    const bookedUser = selectedRoomData.find(room => {
        const reservationDateTime = new Date(room.ReservationTime);
        const formattedReservationDate = reservationDateTime.toISOString().split('T')[0];

        return (
            formattedReservationDate === selectedDate &&
            room.ReservationTime.includes(selectedTime.substr(0, 5))
        );
    });

    return bookedUser ? String(bookedUser.QalamID) : "Available";
}

 
</script>

<main>
  <div class="heading">Room Management</div>
  <div class="container">
    <div class="row">
      <!-- Left side with dropdown room list -->
      <div class="col-md-6">
<label for="roomDropdown">Select a Room:</label>
  <select id="roomDropdown" bind:value={selectedRoom} on:change={updateTable} class="form-control">
    <option value="">-- Select a Room --</option>
    {#each Array.from(new Set(rooms.map(room => room.RoomNo))) as roomNo}
      <option value={roomNo}>{roomNo}</option>
    {/each}
  </select>
      </div>

      <!-- Right side with the smaller Bootstrap table -->
      <div class="col-md-6">
         <div class="mb-3">
      <label for="datePicker">Select a Date:</label>
      <input type="date" id="datePicker"on:click = {updateTable} bind:value={selectedDate} min={getNext7Days()[0]} max={getNext7Days()[6]}>
    </div>
        <div class="table-container">
          <table class="table table-sm table-bordered">
            <thead>
              <tr>
                <th>Time</th>
                <th>Availability</th>
                <th>Booked By</th>
              </tr>
            </thead>
<tbody>
{#each timeSlots as time}
  <tr>
    <td>{time}</td>
    <td>
{#if TimeBooked(selectedRoom, selectedDate, time) != ''}
Booked
{:else}
Available
{/if}
    </td>
<td>
 { TimeBooked(selectedRoom, selectedDate, time)}
</td>
    </tr>
{/each}
</tbody>

          </table>
        </div>
      </div>
    </div>

    <div class="row mt-4">
      <div class="col-md-12">
        <h2 class="text-center">Room Booking Management</h2>
        <p class="text-center">View and manage room bookings.</p>
      </div>
    </div>
  </div>
</main>

<style>
  /* Additional CSS for the table container */
  .table-container {
    max-height: 50vh;
    overflow-y: auto;
    border: 1px solid #ddd; /* Optional border for aesthetics */
    padding: 10px; /* Optional padding for aesthetics */
  }

  /* Additional CSS for the 'booked' class */
  .booked {
    background-color: #FFCCCC; /* You can customize the background color for booked slots */
  }
</style>
