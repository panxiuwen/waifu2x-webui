import bottle
from bottle import run, route, static_file,request
from utils.prepare_images import *
from Models import *
from torchvision.utils import save_image
model_cran_v2 = CARN_V2(color_channels=3, mid_channels=64, conv=nn.Conv2d,
                        single_conv_size=3, single_conv_group=1,
                        scale=2, activation=nn.LeakyReLU(0.1),
                        SEBlock=True, repeat_blocks=3, atrous=(1, 1, 1))
model_cran_v2 = network_to_half(model_cran_v2)
checkpoint = "model_check_points/CRAN_V2/CARN_model_checkpoint.pt"
model_cran_v2.load_state_dict(torch.load(checkpoint,map_location=lambda storage, loc: storage.cuda(0)))
model_cran_v2 = model_cran_v2.float()
app = bottle.default_app()
@route('/',method='GET')
def home():
    return static_file("index.html", root='./assets/')
@route('/<path>')
def html(path):
    return static_file(path, root='./assets/')
@route('/api',method='POST')
def do_upload():
    file=request.files.get('upload') 
    file.save("0.png",overwrite=True)
    img = Image.open("0.png").convert("RGB")
    img_splitter = ImageSplitter(seg_size=64, scale_factor=2, boarder_pad_size=3)
    img_patches = img_splitter.split_img_tensor(img, scale_method=None, img_pad=0)
    with torch.no_grad():
        out = [model_cran_v2(i) for i in img_patches]
    img_upscale = img_splitter.merge_img_tensor(out)
    save_image(img_upscale,"1.png")
    return static_file("2.png", root=".")
run(host="0.0.0.0", port=2333)