### Instructions
1. Place yourself at the directory level of the docker-compose file
2. Run the command
		`docker-compose -f docker-compose.yml up`
3. This should start the database docker container
4. Place yourself inside the app/   folder
5. Run the command
		`sudo docker run -it --net challenge_default queens`
	- This is assumming you the folder is still challenge
6. This will ask you for the dimension of the chess board e.g. 4,5,6...12
7. If you want to run the test you will have to add pytest at the end 
		`sudo docker run -it --net challenge_default queens pytest`
8. I didnt include the python script into the compose because of the terminal that asks you how many rows
9. I can include it if needed