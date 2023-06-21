import cv2
import base64
import os

class OpenCVWeChatQRCodeReader():
    def __init__(self):
        self.detector = cv2.wechat_qrcode_WeChatQRCode()

    def decode_file(self, img_path):
        result_dict = {}
        results = []
        text_results, points_list = detector.detectAndDecode(cv2.imread(img_path))
        self.wrap_results(results, text_results, points_list)
        result_dict["results"] = results
        return result_dict
        
    def decode_bytes(self, img_bytes):
        result_dict = {}
        results = []
        text_results, points_list = detector.detectAndDecode(cv2.imdecode(img_bytes))
        self.wrap_results(results, text_results, points_list)
        result_dict["results"] = results
        return result_dict
        
    def wrap_results(self, results, text_results, points_list):
        for i in range(len(text_results)):
            text_result = text_result[i];
            points = points_list[i]
            result = {}
            result["barcodeFormat"] = "QRCode"
            result["barcodeText"] = text_result
            result["barcodeBytes"] = str(base64.b64encode(text_result.encode("utf-8")))[2:-1]
            vertex = points[i]
            result["x1"] = int(vertex[0][0])
            result["y1"] = int(vertex[0][1])
            result["x2"] = int(vertex[1][0])
            result["y2"] = int(vertex[1][1])
            result["x3"] = int(vertex[2][0])
            result["y3"] = int(vertex[2][1])
            result["x4"] = int(vertex[3][0])
            result["y4"] = int(vertex[3][1])
            results.append(result)

if __name__ == '__main__':
    reader = OpenCVWeChatQRCodeReader()
    results = reader.decode_file("test.jpg")
    print(results)
    