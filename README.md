# toolbox

> Some tools provide two languages, en-US and zh-TW.

## Tools
### macOS-passwd-update-checker_\<language>.sh
> Warning: macOS only

Show the time of the last password change, and check if the time between current date and changing time is greater than the value of `alert_days` (change it if you want).

* Sample outputs:  
  * Not expired:  
    ![](https://i.imgur.com/2bJrATA.png)  
  * Expired:  
    ![](https://i.imgur.com/uFt6Tsh.png)  

### new-sh-generator.sh
* Usage:
```
./new-sh-generator.sh [option]
    --filename <file name>, -f <file name>
      name of this new script
```

### new-queuing-cmd-generator.sh
* Usage: 
```
./new-queuing-cmd-generator.sh [options...]
    --filename <file name>, -f <file name>    
        name of this new script
    --cmds <Bash commands ...>, -c <Bash commands ...>
        Specify command(s), must be surrounding with double quotes("")
        e.g., --cmds "command_1" "command_2"
    --delay <seconds>, -d <seconds>
        Delay between each command
    --no-exit-if-error, -ne
        Disable all exit process when a command failed to run
```
Create a new shell script containing commands with queuing running process.

### ping-logging.sh
* Usage:
```
./ping-logging.sh [option]
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

---

## Patterns
### multi-params.sh
Just a sample shows a common shell command pattern.
```
./multi-params.sh [--param_a <param_a>] [--param_b <param_b>]
./multi-params.sh [--help]
```
