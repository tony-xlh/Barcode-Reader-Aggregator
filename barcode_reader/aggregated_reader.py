import time

class AggregatedReader():

    def __init__(self, engine="dynamsoft"):
        self.reader = None
        self.engine = engine
        self.init_reader()
        
    def init_reader(self):
        if self.engine == "Dynamsoft" or self.engine == "":
            from barcode_reader.dynamsoft import DynamsoftBarcodeReader
            self.reader = DynamsoftBarcodeReader()
        elif self.engine == "LibDMTX":
            from barcode_reader.libdmtx import LibDMTXReader
            self.reader = LibDMTXReader()
        elif self.engine == "ZXingCPP":
            from barcode_reader.zxingcpp import ZXingBarcodeReader
            self.reader = ZXingBarcodeReader()
        elif self.engine == "OpenCV WeChat":
            from barcode_reader.opencv_wechat_qrcode import OpenCVWeChatQRCodeReader
            self.reader = OpenCVWeChatQRCodeReader()
        elif self.engine == "ZBar":
            from barcode_reader.zbar import ZBarBarcodeReader
            self.reader = ZBarBarcodeReader()
        elif self.engine == "BoofCV":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="BoofCV",url="http://127.0.0.1:51041/readBarcodes")
        elif self.engine == "Accusoft":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="Accusoft",url="http://127.0.0.1:51041/readBarcodes")
        elif self.engine == "ZXing":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="ZXing",url="http://127.0.0.1:51041/readBarcodes")
        elif self.engine == "MLKit":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="MLKit")
        elif self.engine == "AppleVision":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="AppleVision")
        elif self.engine == "Dynamsoft-iOS":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="DBR")
        elif self.engine == "ZXingObjc":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="ZXing")
        elif self.engine == "Scandit":
            from barcode_reader.http_barcodereader import HTTPBarcodeReader
            self.reader = HTTPBarcodeReader(sdk="Scandit")
        
            
    def get_engines(self):
        return ["Dynamsoft","LibDMTX","ZXingCPP","ZBar","OpenCV WeChat","ZXing","Accusoft","BoofCV","MLKit","AppleVision","Dynamsoft-iOS","ZXingObjc","Scandit"]

    def decode_bytes(self, file_bytes):
        start_time = time.time()
        results = self.reader.decode_bytes(file_bytes)
        end_time = time.time()
        elapsedTime = int((end_time - start_time) * 1000)
        if "elapsedTime" not in results:
            results["elapsedTime"] = elapsedTime
        return results
    
    def decode_file(self, file_path):
        start_time = time.time()
        results = self.reader.decode_file(file_path)
        end_time = time.time()
        elapsedTime = int((end_time - start_time) * 1000)
        if "elapsedTime" not in results:
            results["elapsedTime"] = elapsedTime
        return results
        