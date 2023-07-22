import bottle, time, os, sys
from bottle import run, route, static_file,request
from waifu2x_vulkan import waifu2x_vulkan as waifu2x
sts = waifu2x.init()
if sts < 0:
    # cpu model
    isCpuModel = True
sts = waifu2x.initSet(sts,8)

app = bottle.default_app()
@route('/',method='GET')
def home():
    return static_file("index.zh-CN.html", root='/app/waifu2x-webui/assets')
@route('/<path>')
def html(path):
    return static_file(path, root='/app/waifu2x-webui/assets')
@route('/api',method='POST')
def do_upload():
    file=request.files.get('upload')
    file.save("/app/waifu2x-webui/0.png",overwrite=True)
    f = open("/app/waifu2x-webui/0.png", "rb")
    data = f.read()
    waifu2x.add(data, waifu2x.MODEL_CUNET_NOISE3, 1, 2.5)
    info = waifu2x.load(0)
    if not info:
        return "Error in convert"
    else:
        newData, foramt, backId, tick = info
        f = open("/app/waifu2x-webui/1.png", "wb+")
        f.write(newData)
        f.close()
    return static_file("1.png", root="/app/waifu2x-webui")
run(host="0.0.0.0", port=2333)
