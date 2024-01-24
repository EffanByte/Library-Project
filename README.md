After cloning the repository, you need to add a few dependencies. Make sure you have node.js/npm installed. On the console, download the dependencies using
npm install svelte
npm install bootstrap
npm install axios

We've created a virtual environment or venv to avoid downloading flask and flask server but not sure if it works. So just write the following code

pip install bcrypt (make sure to cd flask-server)
pip install flask  
pip install mysql-connector-python

For the database, open MySQL instance Go to Server -> Data Import and add all the contents from the given zip file to add our database.

You should be all set now. To run the project, first cd to flask-server and type 'python server.py' to activate the flask server to receive data from MySQL server.
open another terminal (assuming you're on visual studio code) and type npm run dev to start the local host. Click on the given link and the project should display in front of you.
