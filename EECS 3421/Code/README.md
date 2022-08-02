# Configuration

The following SQL scripts were designed to be run using PostgreSQL. 
If you are a York University (EECS) student, then you can test these by using the following avenues:
- ssh into the red server, and run the scripts on your psql account. This can be done using your terminal, or through VSCode with the Microsoft Remote - SSH extension.
- Install PostgreSQL onto your computer, and run the scripts locally. Personally, I found it easier on my end to test scripts using WSL2.

# Installing PostgreSQL

This section will mainly focus on installing PostgreSQL through WSL2. I found this avenue to be the easiest to tinker with. 
Do note that as of this moment, the script has been tested on Ubuntu 20.04.4 LTS. 

1. Ensure that you have WSL2 installed on your computer 
2. Open your terminal, and run the following command: ```sudo apt install postgresql postgresql-contrib```
3. Check the status of your postgresql (local) server. Run the following command in your terminal: ```service postgresql status```
4. If the command returns **X/main (port 5432): down**, you must start it. To do so, we issue the command: ```sudo service postgresql start```
5. Once the server has been started, run the command: ```sudo su postgres```.  This will log you into the default superuser, postgres. Of course, you are free from this point, as the super user to either create your own account, or modify this to your specification (i.e., adding a required password.)
6. You are now ready to get tinkering. Simply type **psql** into the terminal, and you will now be ready to run SQL files on your local server. Enjoy!  
