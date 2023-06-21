import cv2
import base64
import os
import numpy as np

class OpenCVWeChatQRCodeReader():
    def __init__(self):
        self.detector = cv2.wechat_qrcode_WeChatQRCode()

    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results, points_list = self.detector.detectAndDecode(cv2.imread(img_path))
        self.wrap_results(results, text_results, points_list)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        img_bytes_array = np.asarray(bytearray(img_bytes), dtype="uint8")
        text_results, points_list = self.detector.detectAndDecode(cv2.imdecode(img_bytes_array, cv2.IMREAD_COLOR))
        self.wrap_results(results, text_results, points_list)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self, results, text_results, points_list):
        print(points_list)
        for i in range(len(text_results)):
            text_result = text_results[i];
            points = points_list[i]
            result = {}
            result["barcodeFormat"] = "QRCode"
            result["barcodeText"] = text_result
            result["barcodeBytes"] = str(base64.b64encode(text_result.encode("utf-8")))[2:-1]
            result["x1"] = int(points[0][0])
            result["y1"] = int(points[0][1])
            result["x2"] = int(points[1][0])
            result["y2"] = int(points[1][1])
            result["x3"] = int(points[2][0])
            result["y3"] = int(points[2][1])
            result["x4"] = int(points[3][0])
            result["y4"] = int(points[3][1])
            results.append(result)

if __name__ == '__main__':
    reader = OpenCVWeChatQRCodeReader()
    results = reader.decode_file("test.jpg")
    print(results)
    