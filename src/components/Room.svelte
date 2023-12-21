<script>
  import axios from "axios";
  import { onMount } from "svelte";
  import {user} from "./store.js";
  let selectedRoom = null;
  let selectedDate = null; // Add a variable to store the selected date

  let rooms = [];

  const timeSlots = [
    '9:00:00', '10:00:00', '11:00:00', '12:00:00', '13:00:00', '14:00:00',
    '15:00:00', '16:00:00', '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00'
  ];
  // Function to get the next 7 days in YYYY-MM-DD format
  function getNext7Days() {
    const today = new Date();
    return Array.from({ length: 7 }, (_, i) => {
      const date = new Date(today);
      date.setDate(today.getDate() + i);
      updateTable();
      return date.toISOString().split('T')[0];
    });
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
 
      // Set hasMounted to true to prevent further calls to onMount
      hasMounted = true;
    }
  });
function isTimeBooked(roomNo, selectedDate, selectedTime) {
    const selectedRoomData = rooms.filter(room => room.RoomNo == roomNo);

    return selectedRoomData.some(room => {
        const reservationDateTime = new Date(room.ReservationTime);
        const formattedReservationDate = reservationDateTime.toISOString().split('T')[0];

if (            formattedReservationDate === selectedDate &&
            room.ReservationTime.includes(selectedTime.substr(0, 5))){
            console.log(room.QalamID)
            return room.QalamID;
            }
else 
return false;
    });
}
 
async function bookNow(selectedDate, selectedTime) {
  const roomNo = selectedRoom;
  const qalamID = $user.id;
  if (qalamID == 0){
    alert("Please login to book a room!")
    return;
  }
  const reservationTime = `${selectedDate} ${selectedTime}`;
  console.log(selectedDate, selectedTime)
  try {
    const response = await axios.post('http://localhost:8000/api/rooms', {
      RoomNo: roomNo,
      QalamID: qalamID,
      ReservationTime: reservationTime,
      ReservationStatus: "Booked",
    });

    if (response.data.message) {
      updateTable();
      console.log("Room booked successfully");
    } else {
      console.error('Error:', response.data.error);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}
 async function removeAllUserBookings() {
    try {
      // Make a request to your server to remove all bookings for the current user
      const response = await axios.post('http://localhost:8000/api/remove_bookings', {
        QalamID: $user.id,
      });

      if (response.data.message) {
        console.log('All bookings removed successfully');
        updateTable(); // Refresh the table after removing bookings
      } else {
        console.error('Error:', response.data.error);
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

async function updateTable() {
    try {
      // Clear the existing data before fetching new data
      rooms = [];
      // Fetch updated rooms data based on the selected room and date
      const response = await axios.get('http://localhost:8000/api/rooms');
      rooms = response.data; // Assuming the API response contains an array of room data
    } catch (error) {
      console.error('Error updating table:', error);
    }
  }
</script>

<main>
  <div class="heading">Book a Room Here!</div>
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
      <button class="btn btn-danger mt-4" on:click={removeAllUserBookings}>
      Remove all your bookings
    </button>
</div>


      <!-- Right side with the smaller Bootstrap table -->
<div class="col-md-6">
  <div class="table-container">
    <div class="mb-3">
      <label for="datePicker">Select a Date:</label>
      <input type="date" id="datePicker"on:click = {updateTable} bind:value={selectedDate} min={getNext7Days()[0]} max={getNext7Days()[6]}>
    </div>
    <table class="table table-sm table-bordered">
      <thead>
        <tr>
          <th>Time</th>
          <th>Availability</th>
          <th>Action</th> <!-- New column for the "Remove" button -->
        </tr>
      </thead>
      <tbody>
{#each timeSlots as time}
  <tr>
    <td>{time}</td>
    <td class="{isTimeBooked(selectedRoom, selectedDate, time) ? 'booked' : 'available'}">
      {isTimeBooked(selectedRoom, selectedDate, time) ? 'Booked' : 'Available'}
    </td>
    <td>
      {#if isTimeBooked(selectedRoom, selectedDate, time)}
        <button class="btn btn-secondary btn-sm" disabled>Not Available</button>
      {:else}
        <button class="btn btn-primary btn-sm" on:click={() => bookNow(selectedDate, time)}>Book Now</button>
      {/if}
    </td>
  </tr>
{/each}


      </tbody>
    </table>
  </div>
</div>


    <div class="row mt-4">
      <div class="col-md-12">
        <h2 class="text-center">Welcome to our Room Booking System!</h2>
        <p class="text-center">Explore the available rooms and plan your bookings accordingly.</p>
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
