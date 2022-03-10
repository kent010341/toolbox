# toolbox

> Some tools provide two languages, en-US and zh-TW.

## Tools
### macOS-passwd-update-checker_\<language>
> Warning: macOS only

Show the time of the last password change, and check if the time between current date and changing time is greater than the value of `alert_days` (change it if you want).

* Sample outputs:  
  * Not expired:  
    ![](https://i.imgur.com/2bJrATA.png)  
  * Expired:  
    ![](https://i.imgur.com/uFt6Tsh.png)  

### new-sh-generator
* Usage:
```
./new-sh-generator [option]
    --filename <file name>, -f <file name>
      name of this new script
    --path <path>, -p <path>
        location of where the script run
```

### new-queuing-cmd-generator
* Usage: 
```
./new-queuing-cmd-generator [options...]
    --filename <file name>, -f <file name>    
        name of this new script
    --cmds <Bash commands ...>, -c <Bash commands ...>
        Specify command(s), must be surrounding with double quotes("")
        e.g., --cmds "command_1" "command_2"
    --delay <seconds>, -d <seconds>
        Delay between each command
    --no-exit-if-error, -ne
        Disable all exit process when a command failed to run
    --path <path>, -p <path>
        location of where the script run
```
Create a new shell script containing commands with queuing running process.

### ping-logging
* Usage:
```
./ping-logging [option]
    --period <period>, -T <period>
        period (in second) between each pings (default: 3)
    --target <target ip/url>, -ip <target ip/url>
        ping target (default: google.com)
    --path <path>, -p <path>
        location of where the log is stored
```
Infinite loop pinging the target IP/URL with specified period and write to a log file.  

### ws_server.py
> Python 3.6 (or above)  
> Requires `websockets` (can be installed by `pip install`)

Start a simple WebSocket server on port 8765.  
Use URL `ws://localhost:8765` to connect it. 

### show_folder_tree.py
* Usage:
```
python show_folder_tree.py [options]
    --path <folder path>, -p <folder path>')
        path of the folder'
    --output <file path>, -o <file path>'
        output file name'
```
Write the folder structure to a markdown file.

---

## Patterns
### multi-params
Just a sample shows a common shell command pattern.
```
./multi-params [--param_a <param_a>] [--param_b <param_b>]
./multi-params [--help]
```
