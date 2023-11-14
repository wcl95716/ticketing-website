import sys
sys.path.append("./src")


from service import flask_service

import requests

def test_upload_file():
    url = 'http://localhost:5000/upload_file'
    files = {'file': ('2.mp4', open("/Users/panda/Desktop/github.nosync/ticketing-website/backend/src/unit_testing/service/2.mp4", 'rb'))}
    response = requests.post(url, files=files)
    print(response.text)

if __name__ == "__main__":
    flask_service.get_app().run(host='127.0.0.1',port=5000,debug=True)
    # test_upload_file()