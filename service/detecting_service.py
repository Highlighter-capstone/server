import os
from yolo.yolov5 import detect
from haar_cascade.extract_emotions_by_image import get_emotion_by_image

def get_frames(file_name):
    # frame들 이름 가져오기
    folder_name = file_name.split(".")[0]
    dir_path = "../datasets/frame/" + folder_name
    frames = []
    max_value = -1
    for root, directories, files in os.walk(dir_path):
        for file in files:
            max_value = max(int(file.split("_")[1].split(".")[0]), max_value)
    for i in range(max_value + 1):
        frames.append(os.path.join(dir_path, (folder_name + "_" + str(i) + ".jpg")))
    return frames

#print(get_frames("yoonjong-2022-04-19-23:01:00.mp4"))

# 하이라이트 시간 추출
def get_highlight_times():
    frames = get_frames()
    n=0
    left=-1
    right=-1
    buff=0
    list=[]
    last=len(frames)

    # 장면마다
    for frame in frames:
        if right!=-1 and n==last-1:
            temp=[]
            buff=0
            #초반 2초
            if left<2:
                temp.append(0)
                temp.append(right)
            else:
                temp.append(left-2)
                temp.append(right)
            list.append(temp)
            break
        #웃는얼굴찾기 실패
        if not(detect_people(frame)):
            # 버퍼큐에 있는데 실패중
            if right != -1:
                buff += 1
            # 버퍼큐에 있는데 3초동안 웃는얼굴 안나옴
            if buff == 3:
                temp = []
                buff = 0
                # 초반 2초
                if left < 2:
                    temp.append(0)
                    temp.append(right)
                else:
                    temp.append(left-2)
                    temp.append(right)
                left = -1
                right = -1
                list.append(temp)
            continue
        # 웃는얼굴 찾음
        else:
            # 버퍼큐에 없음
            if left == -1:
                left = n
                right = n
            # 버퍼큐에 있음
            else:
                right=n
            buff=0
        
        n+=1
    return list

    # Buffer Queue 적용


# yolov5
def detect_people(file_name):
    result = detect.run(weights="../yolo/yolov5/best.pt",
                        source="../datasets/frame/" + str(file_name))
    if(result[detect]):
        return detect_smile(result, "../datasets/frame/" + str(file_name))
    else:
        return False


# Haar Cascade
def detect_smile(frame_data, path):


    return get_emotion_by_image(path, frame_data)

    






