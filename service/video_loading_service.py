from domain.S3Connector import S3Connector
import cv2
import os

s3Connector = S3Connector()

# 영상을 다운로드하는 메소드.
def load_video():
    try:
        client = s3Connector.get_client()
        file_name = '../datasets/video/concert.mp4'
        key = 'public/compressed.mp4'
        client.download_file(s3Connector.get_bucket(), key, file_name)
    except:
        return False
    return True

# 다운로드 된 영상을 1초 단위로 split
def split_video(file_name):
    try:
        vid_cap = cv2.VideoCapture(file_name)
        fps = vid_cap.get(cv2.CAP_PROP_FPS)
        if not os.path.exists("../datasets"):
            os.makedirs("../datasets")
        count = 0
        while vid_cap.isOpened():
            ret, image = vid_cap.read()
            if ret == False:
                break
            # 1초마다 프레임 추출
            if(int(vid_cap.get(1)) % round(fps) == 0):
                if not os.path.exists("../datasets/frame"):
                    os.makedirs("../datasets/frame")
                cv2.imwrite("../datasets/frame" + "/%s%d.jpg" % (file_name.split("/")[-1].split(".")[0], count), image)
                print('Saved frame number : ' , str(int(vid_cap.get(1))))
                count+=1
        vid_cap.release()
        return True
    except:
        return False

print(split_video("../datasets/video/attention_process.mp4"))