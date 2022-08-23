### Instructions
1. Place yourself at the directory level of the docker-compose file
2. Run the command
		`docker-compose -f docker-compose.yml up`
3. This should start the database docker container
4. Place yourself inside the app/   folder
5. To build the python applications run the command
		`sudo docker build --tag queens .`
6. Run the command
		`sudo docker run -it --net challenge_net queens`
	- This is assuming you the folder is still challenge
6. This will ask you for the dimension of the chess board e.g. 4,5,6...12
7. If you want to run the test you will have to add pytest at the end 
		`sudo docker run -it --net challenge_net queens pytest`
	- The flag `-s` is optional if you want the output weaved inside pytest output
8. If you want to start any of your two containers this should do the trick
		`sudo docker start -ia __containerId__`
	- To check your containers 
		`sudo docker ps -a`

#### Notes
1. I didn't include the python script into the compose because of the terminal that asks you the dimension of the board (I can include it if needed)
2. Saving things in the database slows down the program a little.
	1. The test is only to n=14 it will take nearly 2 minutes to write all the answers, you can uncomment tests for bigger numbers before building but the time curve will be steep 
	3. Without saving to database the biggest calculable number in a sensible time would be 15 in 12 and a half minutes