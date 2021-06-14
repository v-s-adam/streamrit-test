import streamlit as st
import streamlit.components.v1 as stc
from PIL import Image, ImageDraw, ImageFont
import io
import requests

SUBSCRIPTION_KEY = '6ff4651626dc4903b8afecd141089691'
assert SUBSCRIPTION_KEY
face_api_url = 'https://20210603adam.cognitiveservices.azure.com/face/v1.0/detect'

st.title('顔認証アプリ')

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])

headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
}
params = {
    'returnFaceId': 'true',
    'returnFaceAttributes': 'age, gender, headPose, smile, facialHair, glasses, emotion, hair, makeup, occlusion, accessories, blur, exposure, noise'
}

if uploaded_file is not None:
    img = Image.open(uploaded_file)

    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue()

    res = requests.post(face_api_url, params=params, headers=headers, data=binary_img)
    # 複数人いる場合を考慮して複数形
    results = res.json()

    # results内に複数情報があった場合にfor文で回す
    for result in results:
        rect = result['faceRectangle']
        gender = result['faceAttributes']['gender']
        age = str(round(result['faceAttributes']['age']))

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left']+rect['width'], rect['top']+rect['height'])], fill=None, outline='green', width=5)

        if rect['width']/4 > 20:
            t_size = round(rect['width']/4)
        else:
            t_size = 20
        fnt = ImageFont.truetype("arial", t_size)
        draw.multiline_text((rect['left']+(rect['width']/2), rect['top']-32), gender + '\n' +
                            age, fill='red', anchor='ms', font=fnt, spacing=2, align='center')

    st.image(img, caption='Uploaded Image.', use_column_width=True)
