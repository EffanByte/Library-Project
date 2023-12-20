<!-- RoomManage.svelte -->

<script>
   import { onMount } from 'svelte';
  let selectedRoom = null;

  let rooms = [
    { id: 1, name: 'Room 101', bookedTimings: ['11:00 AM', '2:00 PM', '4:00 PM'], bookedBy: ['UserA', 'UserB', 'UserC'] },
    { id: 2, name: 'Room 102', bookedTimings: ['10:00 AM', '3:00 PM', '5:00 PM'], bookedBy: ['UserX', 'UserY', 'UserZ'] },
    // Add more rooms with their bookedTimings and bookedBy as needed
  ];

  const timeSlots = [
    '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM',
    '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM'
  ];

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

 onMount(() => {
    // You can use onMount to load initial data or perform actions when the component is mounted.
  });
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
          {#each rooms as room}
            <option value={room.id}>{room.name}</option>
          {/each}
        </select>
      </div>

      <!-- Right side with the smaller Bootstrap table -->
      <div class="col-md-6">
        <div class="table-container">
          <table class="table table-sm table-bordered">
            <thead>
              <tr>
                <th>Time</th>
                <th>Availability</th>
                <th>Book By</th>
                <th>Action</th> <!-- New column for the "Remove" button -->
              </tr>
            </thead>
<tbody>
  {#each timeSlots as time}
    <tr>
      <td>{time}</td>
      <td class="{rooms.find(room => room.id == selectedRoom)?.bookedTimings.includes(time) ? 'booked' : 'available'}">
        {rooms.find(room => room.id == selectedRoom)?.bookedTimings.includes(time) ? 'Booked' : 'Available'}
      </td>
      <td>
        {#if rooms.find(room => room.id == selectedRoom)?.bookedTimings.includes(time)}
          {rooms.find(room => room.id == selectedRoom)?.bookedBy[rooms.find(room => room.id == selectedRoom)?.bookedTimings.indexOf(time)]}
        {:else}
          - <!-- Display a dash if the time slot is not booked -->
        {/if}
      </td>
      <td>
        {#if rooms.find(room => room.id == selectedRoom)?.bookedTimings.includes(time)}
          <button class="btn btn-danger btn-sm" on:click={() => removeBooking(selectedRoom, time)}>Remove</button>
        {:else}
          - <!-- Display a dash if the time slot is not booked -->
        {/if}
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
