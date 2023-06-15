import zxingcpp
from io import BytesIO
from PIL import Image
import base64
import os


class ZXingBarcodeReader():
    def __init__(self):
        pass

    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results = zxingcpp.read_barcodes(Image.open(img_path),formats=zxingcpp.BarcodeFormat.DataMatrix)
        self.wrap_results(results, text_results)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        text_results = zxingcpp.read_barcodes(Image.open(BytesIO(img_bytes)),formats=zxingcpp.BarcodeFormat.DataMatrix)
        self.wrap_results(results, text_results)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self,results,text_results):
        for tr in text_results:
            if tr.valid == True:
                result = {}
                result["barcodeFormat"] = tr.format.name
                result["barcodeText"] = tr.text
                result["barcodeBytes"] = str(base64.b64encode(tr.bytes))[2:-1]
                result["x1"] = tr.position.top_left.x
                result["y1"] = tr.position.top_left.y
                result["x2"] = tr.position.top_right.x
                result["y2"] = tr.position.top_right.y
                result["x3"] = tr.position.bottom_right.x
                result["y3"] = tr.position.bottom_right.y
                result["x4"] = tr.position.bottom_left.x
                result["y4"] = tr.position.bottom_left.y
                results.append(result)
        
if __name__ == '__main__':
    reader = ZXingBarcodeReader()
    results = reader.decode_file("test.jpg")
    print(results)
    