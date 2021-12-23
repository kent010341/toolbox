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

Create a new shell script containing basic pattern.

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
