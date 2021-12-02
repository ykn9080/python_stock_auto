import requests


def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
                             headers={"Authorization": "Bearer "+token},
                             data={"channel": channel, "text": text}
                             )
    print(response)


myToken = "xoxb-2803466359121-2791510940706-SnNVV4TrcNJEBC9bl2uuTLXZ"

post_message(myToken, "#stock", "안뇽하세요")
