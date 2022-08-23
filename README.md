### Instructions
1. Place yourself at the directory level of the docker-compose file
2. Run the command
		`sudo docker-compose -f docker-compose.yml up`
3. This should start the database docker container
4. Place yourself inside the app/   folder
5. To build the python applications run the command
		`sudo docker build --tag queens .`
6. Run the command
		`sudo docker run -it --net challenge_net queens`
6. This will ask you for the dimension of the chess board e.g. 4,5,6...12
7. If you want to run the test you will have to add pytest at the end 
		`sudo docker run -it --net challenge_default queens pytest`


#### Notes
1. I didn't include the python script into the compose because of the terminal that asks you the dimension of the board (I can include it if needed)
2. Saving things in the database severely slows down the program.
	1. The test is only to n=12 it will take nearly 3 minutes to write all the answers, you can uncomment tests for bigger numbers before building but the time curve will be steep 
	2. After the answers are added to the database the times will decrease sharply, n=12 will only take around 17 seconds is they are already in the db, 4 seconds if we take out the db entirely
	3. Without saving to database the biggest calculable number in a sensible time would be 15 in 12 and a half minutes or 14 in 2 minutes