from flask import Flask, request
from service import detecting_service, video_loading_service
import json

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def extract_highlight_times():
    params = json.loads(request.get_data(), encoding='utf-8')
    video_name = params['video_name']
    if len(params) == 0:
        return json.dumps({'success' : False, 'time' : []})

    video_loading_service.load_video(video_name)
    video_loading_service.split_video(video_name)
    result = detecting_service.get_highlight_times(video_name)
    return json.dumps({'success' : False, 'time' : [43]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
