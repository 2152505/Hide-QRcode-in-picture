from PIL import Image   # 若提示No module named 'PIL'，则：pip install Pillow
from funs import MergeQRToImage
from funs import MakeQRCode
# 打开两张素材图片，其中二维码背景为白色。
# 注意：为了代码简洁，这两张图的分辨率必需要是相同的。
# 使用QR库生成png需要修改，MakeQRCode.MakeQRCode()
imgPutong = Image.open("./img/image.jpg")          
imgBarcode = Image.open("./img/qr.png") 
#imgBarcode = imgBarcode.resize((2500,2500))
imgPutong=imgPutong.resize((640,853))  

MergeQRToImage.MergeQRToImage(imgBarcode,imgPutong)

