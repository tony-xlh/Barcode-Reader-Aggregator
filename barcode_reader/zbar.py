from pyzbar.pyzbar import decode
from io import BytesIO
from PIL import Image
import base64
import os

class ZBarBarcodeReader():
    def __init__(self):
        pass

    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results = decode(Image.open(img_path))
        self.wrap_results(results, text_results)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        text_results = decode(Image.open(BytesIO(img_bytes)))
        self.wrap_results(results, text_results)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self, results, text_results):
        if text_results!=None:
            for tr in text_results:
                result = {}
                result["barcodeFormat"] = tr.type
                result["barcodeText"] = tr.data.decode("utf-8")
                result["barcodeBytes"] = str(base64.b64encode(tr.data))[2:-1]
                rect = tr.rect
                result["x1"] = rect.left
                result["y1"] = rect.top
                result["x2"] = rect.left + rect.width
                result["y2"] = rect.top
                result["x3"] = rect.left + rect.width
                result["y3"] = rect.top + rect.height
                result["x4"] = rect.left
                result["y4"] = rect.top + rect.height
                results.append(result)
    
if __name__ == '__main__':
    reader = ZbarBarcodeReader()
    results = reader.decode_file("test.jpg")
    print(results)
    