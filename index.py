import requests
import json
import os.path


def create_config():
    print("Enter the bot token")
    token = input()
    file = open("conf.json", "w")
    file.write('{"token":"' + token + '"}')
    file.close()
    get_token()


def get_token():
    if os.path.isfile("conf.json"):
        file = open("conf.json", "r")
        text = file.read()
        if text != '':
            try:
                r = json.loads(text)
                global token
                token = r["token"]
            except Exception:
                create_config()
        else:
            create_config()

    else:
        create_config()


def send_video(video, id):
    url = 'https://api.telegram.org/bot186801765:AAHVFizUvP31UPZPzfZObmjLUqVSacVv5Yc/sendVideoNote'
    try:
        files = {'video_note': open(video, 'rb')}
    except Exception:
        print("Something went wrong. Try to choose the video again")
        video_method()

    if id[0:1] == "@":
        pass
    else:
        id = "@" + id

    r = requests.post(url, files=files, data={'chat_id': "@" + id, 'length': '500'})
    j = r.json()
    try:
        print("https://t.me/" + id + "/" + str(j['result']['message_id']))
    except Exception:
        if j['description'] == 'Bad Request: chat not found':
            print("There is no chat " + id)
            video_method()
        else:
            print("Something went wrong. Try again")
            video_method()


def video_method():
    print("Enter the video address")
    video = input()
    print("Enter the channel id")
    id = input()
    send_video(video, id)
    menu()


def menu():
    print("Please enter 'video'")
    inpu = input()
    if inpu == "video":
        video_method()
    else:
        menu()


get_token()
menu()
