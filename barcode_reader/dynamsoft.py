from dbr import *
import os
import base64
import platform
import logging

class DynamsoftBarcodeReader():
    def __init__(self,use_intermediate_detection_results=False):
        if platform.system() == 'Linux':
            # Sets a directory path for saving the license cache.
            folder_path = "/tmp/Dynamsoft"
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        DBR_license = os.environ.get('DBRLicense')
        if DBR_license == None:
            DBR_license = "DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ=="
        error = BarcodeReader.init_license(DBR_license)
        if error[0] != EnumErrorCode.DBR_OK:
            logging.warning("License error: "+ error[1])
        self.dbr = BarcodeReader()
        
    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results = self.dbr.decode_file(img_path)
        self.wrap_results(results,text_results)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        text_results = self.dbr.decode_file_stream(img_bytes)
        self.wrap_results(results,text_results)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self,results,text_results):
        if text_results==None:
            return
        for tr in text_results:
            result = {}
            result["barcodeFormat"] = tr.barcode_format_string
            result["barcodeText"] = tr.barcode_text
            result["barcodeBytes"] = str(base64.b64encode(tr.barcode_bytes))[2:-1]
            result["confidence"] = tr.extended_results[0].confidence
            points = tr.localization_result.localization_points
            result["x1"] =points[0][0]
            result["y1"] =points[0][1]
            result["x2"] =points[1][0]
            result["y2"] =points[1][1]
            result["x3"] =points[2][0]
            result["y3"] =points[2][1]
            result["x4"] =points[3][0]
            result["y4"] =points[3][1]
            results.append(result)
        
if __name__ == '__main__':
    import time
    reader = DynamsoftBarcodeReader()
    start_time = time.time()
    results = reader.decode_file("../AllSupportedBarcodeTypes.png")
    end_time = time.time()
    elapsedTime = int((end_time - start_time) * 1000)
    print(results)
    print(elapsedTime)
    