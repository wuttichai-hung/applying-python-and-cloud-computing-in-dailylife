import requests

url = 'https://notify-api.line.me/api/notify'

def send_text(token, text):
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS , data = {'message':text})
        print(session_post.text)
    except:
        print("Network is not connected")

def send_text_image(token, text, image_path):
    file_img = {'imageFile': open(image_path, 'rb')}
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS, files=file_img, data= {'message': text})
        print(session_post.text)
    except:
        print("Internet is not connected")

if __name__ == '__main__':
    token = 'your token'
    text = "oh!"
    image_path = "myimage.jpg"
    send_text_image(token, text, image_path)