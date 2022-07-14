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
python show_folder_tree.py <--path | -p> <folder path> [options]
    --path <folder path>, -p <folder path>')
        path of the folder'
    --output <file path>, -o <file path>'
        output file name'
```
Write the folder structure to a markdown file.

### docker-init
* Usage:
```
./docker-init
```
Install docker engine. Following this [tutorial](https://docs.docker.com/engine/install/ubuntu).

---

## Crawlers
### images
* Usage:  
  Edit the file `settings.cfg` to set this crawler.  

|section|key|optional|type|description|sample|
|-|-|:-:|:-:|-|-|
|URL|url.format|X|`string`|URL format, use `{}` for the parameters placeholder.<br>You can also use `{0}`, `{1}`, etc.|`https://example.com/{}/{}_{}.jpg`<br>`https://example.com/{1}/{0}_{2}.jpg`|
|URL|url.param.count|X|`int`|The count of URL parameters. The same amount of `url.param.<param_number>` set should be added|`3`|
|URL|url.param.1.start|Δ|`int`|Start number of parameter 1|`1`|
|URL|url.param.1.end|Δ|`int`|End number of parameter 1|`3`|
|URL|url.param.1.list|Δ|`string`|Use for non-number values for parameter 1|`ABCD`|
|URL|url.param.1.digits|O|`int`|Left filling each value of parameter 1 with zeros in a string of specified length|`5`|
|OUTPUT|output.threads|O (default:`2`)|`int`|Threads for downloading images|`4`|
|OUTPUT|output.folder.path|X|`string`|The folder path for storing images|`./output`|
|OUTPUT|output.file.extension|X|`string`|File extension name of images|`.jpg`|
|OUTPUT|output.file.format|X|`string`|File name format, use `{}` for the parameters placeholder.<br>You can also use `{0}`, `{1}`, etc.|`{}-{}_{}`|
|OUTPUT|output.file.replace|O (default:`False`)|`bool`|If the file exists, replace it?<br>This value is case-insensitive.|`False`<br>`True`|

If you set `url.param.count` as `1`, you should also have `url.param.1.start` and `url.param.1.end` or `url.param.1.list`.  

For example, `url.param.count = 2`, there should be something like:  
```
url.param.1.start = 1
url.param.1.end = 2

url.param.2.start = 3
url.param.2.end = 4
```

or  
```
url.param.1.start = 1
url.param.1.end = 2

url.param.2.list = ABC
```

---

## Patterns
### multi-params
Just a sample shows a common shell command pattern.
```
./multi-params [--param_a <param_a>] [--param_b <param_b>]
./multi-params [--help]
```
