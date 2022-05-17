from domain.S3Connector import S3Connector
import cv2
import os

s3Connector = S3Connector()


# 영상을 다운로드하는 메소드.
def load_video(key):
    client = s3Connector.get_client()
    file_name = os.path.join(os.getcwd(),'datasets','video',key)
    key = "public/" + key
    client.download_file("highlighter234514-dev", key, file_name)
    return True
#load_video("yoonjong-2022-04-19-23:01:00.mp4")

# 다운로드 된 영상을 1초 단위로 split
def split_video(file_name):
    file_name = os.path.join(os.getcwd(), 'datasets','video',file_name)
    vid_cap = cv2.VideoCapture(file_name)
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    if not os.path.exists(".\\datasets"):
        os.makedirs(".\\datasets")
    count = 0
    while vid_cap.isOpened():
        ret, image = vid_cap.read()
        if ret == False:
            break
        # 1초마다 프레임 추출
        if (int(vid_cap.get(1)) % round(fps) == 0):
            if not os.path.exists(".\\datasets\\frame\\" + file_name.split('\\')[-1].split('.')[0]):
                os.makedirs(".\\datasets\\frame\\" + file_name.split('\\')[-1].split('.')[0])
            cv2.imwrite(".\\datasets\\frame\\" + file_name.split('\\')[-1].split('.')[0] + "\\%s_%d.jpg" % (
                file_name.split("\\")[-1].split(".")[0], count), image)
            print('Saved frame number : ', str(int(vid_cap.get(1))))
            count += 1
    vid_cap.release()
    return True

#print(split_video("concert.mp4"))
