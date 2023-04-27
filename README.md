# waifu2x-webui
The webui of waifu2x-python
Except [nagadomi-waifu2x](https://github.com/nagadomi/waifu2x), there is no WebUI for the waifu2x-like softwares (nagadomi-waifu2x is so inconvenient to use it ), so I spent the whole afternoon to achieved this and share with people who need this function.

## The use of WebUI Waifu2x Vulkan
```
git clone https://github.com/panxiuwen/waifu2x-webui
```
Install waifu2x-vulkan and requirements
```
pip3 install waifu2x-vulkan -v
pip3 install paste bottle
```
Then run the script
```
python3 WebUI-Waifu2x-Vulkan-Linux.py
```
Then open 127.0.0.1:2333 in your browser, Select one of your pictures and upload it, wait a few seconds.
## The use of WebUI Waifu2x PyTorch
```
git clone https://github.com/panxiuwen/waifu2x-webui
```
Install  requirements
```
pip3 install paste bottle pytorch
```
Then run the script
```
python3 WebUI-Waifu2x-PyTorch-Linux.py
```
Then open 127.0.0.1:2333 in your browser, Select one of your pictures and upload it, wait a few seconds.
## Credit
[nagadomi-waifu2x](https://github.com/nagadomi/waifu2x): web assets folder
[Waifu2x-vulkan](https://github.com/tonquer/waifu2x-vulkan)
[Waifu2x PyTorch](https://github.com/yu45020/Waifu2x): 
