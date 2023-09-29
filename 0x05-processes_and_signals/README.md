# Processes and signals

When an executing instance of a program is created, it is assigned a unique identification. This is the process id [PID]

A signal is an event generated in response to some condition a
* To list all signals, use ```kill -L```
* The default signal is SIGTERM
* To send a kill signal: ```kill -[SIGNUMBER (from kill -L)] [pID (from pidof proc_name)]```
* example to close the terminal:

    ```
    $ pidof bash
    9191
    $ kill 9191		# Ctrl+C; nothing happens
    $ kill -9 9191	# Ctrl+D; closes the window
    ```


## References:
* The Linux Information Project, Copyright 2005
* Digital Ocean article by Jayant Verma <a href="https://www.digitalocean.com/community/tutorials/process-management-in-linux">Commands for Process Management</a>