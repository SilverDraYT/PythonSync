# PYTHON SYNCRONITATOR (PythonSync)

- This is more of a personal proyect that i have to manage all the music that i have on my USBs and mp3 player.

- Seen from above this proyect has 2 local directories. One whith the music, another one with the music that you download and then by my decision there are also two external directories (in my case my USB and my mp3 player)
Then it takes all the files (from the local directory) and adds them to the USB if it doesnt exist there (it also overwrites the file if the modify timestamp of the local is earlier than the one on the USB) at the same time it checks that if a file exist on the USB and not localy it errases that file.

- The other function is the same but reversed it takes from the USB and moves to local with the same functions.


## INSTALATION

- Until now the only thing that is needed to make this work it to have windows. 
- Other than that the only thing needed is to download it and write your paths on the 'config.ini' file.


