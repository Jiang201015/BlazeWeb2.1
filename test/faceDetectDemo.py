import cv2, requests
url = "http://localhost:8000/serviceApp/facedetect/"  # web地址(http://localhost:8000)+访问接口（facedetect）

# 上传图像并检测
tracker = None
imgPath = "face.jpg"  #图像路径
files = {
    "image": ("filename2", open(imgPath, "rb"), "image/jpeg"),
}

req = requests.post(url, data=tracker, files=files).json()
print("获取信息: {}".format(req))

# 将检测结果框显示在图像上
img = cv2.imread(imgPath)
for (w, x, y, z) in req["faces"]:
    cv2.rectangle(img, (w, x), (y, z), (0, 255, 0), 2)

cv2.imshow("face detection", img)
cv2.waitKey(0)