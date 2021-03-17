# Death Note Telegram Bot 

## How To Use 
- Create a file .env 
### in the .env 
 Get a bot token from [@BotFather](http://telegram.me/BotFather) and replace BOT_TOKEN with your own
- Replace ADMINS with your id 
- Replace PGPASSWORD with your own

<br>available commands:</br>
<br>/start - start a conversation</br>
/help - get info
<br>/rules - rules for the use of the death note</br>
/write_down - write in the death note
<br>/death_list - show victim list</br

***
At the command to start:
<br>A user database is created and the user is added to it and a welcome message is displayed</br>
<br>![Image alt](https://github.com/Amantais/DeathNoteBot/blob/master/examples/Screenshot%20from%202021-03-14%2018-41-47.png)</br>
***
If a person clicks on the /rules:
<br>Then the rules with the page turnover keyboard will be displayed</br>
<br>![Image alt](https://github.com/Amantais/DeathNoteBot/blob/master/examples/Screenshot%20from%202021-03-17%2022-49-27.png)</br>
***
If the user presses /write_down, he will be sent to the death note entry state
<br>The first state will ask for the first and last name, the second the cause of death, and it will all be added to the database</br>
<br>![Image alt](https://github.com/Amantais/DeathNoteBot/blob/master/examples/Screenshot%20from%202021-03-17%2022-51-18.png)</br>
<b>Second Parts</b>
<br>![Image alt](https://github.com/Amantais/DeathNoteBot/blob/master/examples/Screenshot%20from%202021-03-17%2022-51-25.png)</br>
*** 
The last command /death_list takes from the database, the people recorded in the death note, and displays the list to the user.
<br>![Image alt](https://github.com/Amantais/DeathNoteBot/blob/master/examples/Screenshot%20from%202021-03-17%2022-53-40.png)</br>
