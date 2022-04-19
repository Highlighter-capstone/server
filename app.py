from flask import Flask, request
from service import detecting_service, video_loading_service
import json

app = Flask(__name__)


@app.route('/', methods = ['POST'])
def extract_highlight_times():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return json.dumps({'success' : False, 'time' : [1]})
    if not video_loading_service.load_video(params["video_name"]):
        return json.dumps({'success': False, 'time' : [2]})
    if not video_loading_service.split_video(params["video_name"]):
        return json.dumps({'success' : False, 'time' : [3]})

    return json.dumps({'success' : True, 'time' : []})


if __name__ == '__main__':
    app.run()
