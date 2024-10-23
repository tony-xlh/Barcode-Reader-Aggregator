from aspose.barcode import barcoderecognition
import os
import base64
import platform
import logging

class AsposeBarcodeReader():
    def __init__(self):
        self.reader = barcoderecognition.BarCodeReader()
        
    def decode_file(self, img_path):
        result_dict = {}
        results = []
        self.reader.set_bar_code_image(img_path)
        barcodes = self.reader.read_bar_codes()
        self.wrap_results(results,barcodes)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        self.reader.set_bar_code_image(img_bytes)
        barcodes =  self.reader.read_bar_codes()
        self.wrap_results(results,barcodes)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self,results,text_results):
        if text_results==None:
            return
        for tr in text_results:
            result = {}
            result["barcodeFormat"] = tr.code_type_name
            result["barcodeText"] = tr.code_text
            result["barcodeBytes"] = str(base64.b64encode(tr.code_bytes))[2:-1]
            result["confidence"] = tr.confidence
            points = tr.region.points
            result["x1"] =points[0].x
            result["y1"] =points[0].y
            result["x2"] =points[1].x
            result["y2"] =points[1].y
            result["x3"] =points[2].x
            result["y3"] =points[2].y
            result["x4"] =points[3].x
            result["y4"] =points[3].y
            results.append(result)
            
        
if __name__ == '__main__':
    import time
    reader = AsposeBarcodeReader()
    start_time = time.time()
    results = reader.decode_file("1614224122042.png")
    end_time = time.time()
    elapsedTime = int((end_time - start_time) * 1000)
    print(results)
    print(elapsedTime)
    