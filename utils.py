import base64 , os , cv2

def Base64Image(image):
    with open(image,"rb") as f:
        i = f.read()
        return base64.b64encode(i).decode('utf-8')

def CleanUp(image_path):
    try:
        if os.path.exists(image_path):
            os.remove(image_path)
            return 1
    except Exception as E:
        return E

def SaveImage(post_image):
        try:
            if not os.path.exists("temp"):
                os.makedirs("temp")
            path = os.path.join("temp", post_image.filename)
            post_image.save(path)
            return path
        except Exception as Error:
            return Error

def Detect(path):
    image = cv2.imread(path)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    (humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
    padding=(32, 32), scale=1.1)

    for (x, y, w, h) in humans:
        pad_w, pad_h = int(0.15 * w), int(0.01 * h)
        cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)
    cv2.imwrite(os.path.join(path), image)
    return str(len(humans))