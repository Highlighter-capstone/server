import os
from yolo.yolov5 import detect

def get_frames(file_name):
    # frame들 이름 가져오기
    dir_path = "../datasets/frame"
    frames = []
    max_value = -1
    for root, directories, files in os.walk(dir_path):
        for file in files:
            max_value = max(int(file.split("frame")[1].split(".")[0]), max_value)
    for i in range(max_value + 1):
        frames.append(os.path.join(dir_path, (file_name + str(i) + ".jpg")))
    return frames
'''
def get_highlight_times():
    frames = get_frames()
    for frame in frames:
        if not(detect_smile(frame) and detect_people(frame)):
            continue
        else:
            # Buffer Queue 적용
'''

def detect_people(file_name):
    result = detect.run(weights="../yolo/yolov5/best.pt",
                        source="../datasets/frame/" + str(file_name))
    print(result)

'''
#yolo test
for i in range(18):
    detect_people("concert" + str(i) + ".jpg")
'''