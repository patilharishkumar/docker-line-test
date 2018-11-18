Installation.



Step 1:
Implement the script "setup_api.sh" to satisfy the following requirements.
	•	Receive a single positive number.
	•	Spawn a REST-API server proxied by Nginx as a Docker container that will listen for requests on <nginx-ip> TCP port 80
	•	A number will be given as a parameter (3 in the example). Spawn that number of the REST-API server backend containers that will register themselves to the REST-API server.
	•	When HTTP GET / is sent to the REST-API server, the backend container hostname is returned
	•	The REST-API server is scheduling the requests to its back-end with round-robin algorithm
The following sequence of requests must produce the following result:

Test Step:
Create 3 docker container for app
   $ ./setup_api.sh 3

list unique name of container
   $ ./hostNameslist.sh


Step 2:
Implement the REST-API server to satisfy the following requirements.
	•	A Web Server which is able to accept a "to" argument.
	•	"to" argument is the positive number.
	•	When a POST request is sent to /counter with "to" argument, the following result will be produced:
	•	A counter data entity will be created whose value will increment by 1 every single second
	•	The counter should start counting from 1
	•	The counter identifier should be UUID
	•	The counter UUID must be returned immediately upon being created
	•	The counter must disappear when its value reaches the number of "to"
	•	When a GET request  is sent to /counter/<UUID>, a current value of a counter will be returned in JSON format as displayed below:

  Test Step :
  This scrip will help you to test quickly.
  $ ./testStep2.sh


Step 3:
Add the feature to satisfy the following requirements.
	•	Query all created counters with the server API and show their current values, as shown in the following example:

 Test Steps
  $ ./list_counter.sh
  $ ./list_counter.sh  | wc -l

Step 4:
Implement the feature to satisfy the following requirements.
	•	Dynamically change the number of the REST-API server
	•	The counters generated before vanishing must be preserved even when all the REST-API servers have vanished and regenerate again.

Test Steps :
$ ./setup_api.sh 0
$ curl http://127.0.0.1/
 should get 503 Service Unavailable

Now Create  5 hosts with this command.
$ ./setup_api.sh 5

Get list of unique host names
$./hostNameslist.sh


Step 5
Implement the feature to delete the counter, and delete all existing counters as shown below:

Test Steps:
Create counters
$ ./create_couter.sh 10

List counter count.
$ ./list_counter.sh | wc -l

Delete counter count.
$ ./delete_counter.sh

List counter count.
$ ./list_counter.sh | wc -l

Step 6:
Implement a script "wait_counter.sh" that will wait for all counters to expire. wait_counter.sh does not need to be implemented in Shell, it can be called by Python

Testing Steps
$ ./create_couter.sh 10

$ ./wait_counter.sh

$ ./list_counter.sh | wc -l
