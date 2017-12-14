# Raichain

## Requirements:

### 1. Download the Project:
```bash
$ git clone https://github.com/Raichain/Raichain.git
 ```
### 2. Install python modules requirements:
```bash
$ pip3 install -r requirements.txt
```
### 3. Download RaiBlocks Wallet and Configure RPC:
Download the Raiblocks Wallet for your currently Operational System [here](https://raiblocks.net/#getwallets).

#### Wait for the wallet synchronizes with the entire blockchain
**OBS:** for a faster download, you can download the blockchain for [x64](https://yadi.sk/d/fcZgyES73Jzj5T) and for [x86](https://yadi.sk/d/fa1oDDsT3JznEY) systems directly from a server. Then, copy and paste "data.ldb" to the Raiblocks folder.

Then, open the config.json file at Raiblocks folder and configure the RPC like this:
```json
"rpc": {
        "address": "::ffff:127.0.0.1",
        "port": "7076",
        "enable_control": "true",
        "frontier_request_limit": "16384",
        "chain_request_limit": "16384"
    },
    "rpc_enable": "true",
    "opencl_enable": "false",
    "opencl": {
        "platform": "0",
        "device": "0",
        "threads": "1048576"
    }
```
#### Restart your wallet.

**Raiblocks Folder:**
```
Windows: C:\Users\<user\AppData\Local\RaiBlocks\
OSX: /Users/<user>/Library/RaiBlocks/
Linux: /home/<user>/RaiBlocks/
```


