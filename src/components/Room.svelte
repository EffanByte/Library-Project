<!-- Import Bootstrap CSS if not already imported -->
<script>
  let selectedRoom = null;

  let rooms = [
    { id: 1, name: 'Room 101', bookedTimings: ['11:00 AM', '2:00 PM', '4:00 PM'] },
    { id: 2, name: 'Room 102', bookedTimings: ['10:00 AM', '3:00 PM', '5:00 PM'] },
    // Add more rooms with their bookedTimings as needed
  ];

  const timeSlots = [
    '9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM',
    '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM', '7:00 PM', '8:00 PM', '9:00 PM', '10:00 PM'
  ];

  function updateTable() {
    // Logic to update the table based on the selected room
  }

  function bookNow(selectedTime) {
    // Logic for booking the selected time and sending it to the database
    // Here you would typically make an API request to your backend to handle the booking
    if (selectedRoom)
    console.log(`Booked for ${selectedTime} in Room ${rooms.find(room => room.id == selectedRoom).name}`);
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
                <th>Action</th> <!-- New column for the "Book Now" button -->
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
                      <button class="btn btn-secondary btn-sm" disabled>Not Available</button>
                    {:else}
                      <button class="btn btn-primary btn-sm" on:click={() => bookNow(time)}>Book Now</button>
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
