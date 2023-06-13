from pylibdmtx.pylibdmtx import decode
from io import BytesIO
import os
import base64
from PIL import Image

class LibDMTXReader():
    def __init__(self):
        pass
        
    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results = decode(Image.open(img_path))
        self.wrap_results(results,text_results)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        text_results = decode(Image.open(BytesIO(img_bytes)))
        self.wrap_results(results,text_results)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self,results,text_results):
        if text_results==None:
            return
        for tr in text_results:
            print(tr)
            result = {}
            result["barcodeFormat"] = "DataMatrix"
            result["barcodeText"] = tr.data.decode()
            result["barcodeBytes"] = str(base64.b64encode(tr.data))[2:-1]
            left=tr.rect.left
            top=tr.rect.top
            right=left + tr.rect.width
            bottom=top + tr.rect.height
            result["x1"] = left
            result["y1"] = top
            result["x2"] = right
            result["y2"] = top
            result["x3"] = right
            result["y3"] = bottom
            result["x4"] = left
            result["y4"] = bottom
            results.append(result)
        
if __name__ == '__main__':
    import time
    reader = LibDMTXReader()
    start_time = time.time()
    results = reader.decode_file("../AllSupportedBarcodeTypes.png")
    end_time = time.time()
    elapsedTime = int((end_time - start_time) * 1000)
    print(results)
    print(elapsedTime)
    