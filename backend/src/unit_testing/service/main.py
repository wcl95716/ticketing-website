import sys
sys.path.append("./src")


from service import flask_service

if __name__ == "__main__":
    flask_service.get_app().run(host='127.0.0.1',port=5000,debug=True)
