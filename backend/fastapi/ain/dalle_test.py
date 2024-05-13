import os

import openai
from PIL import Image
import requests
from io import BytesIO
from rembg import remove

# Replace YOUR_API_KEY with your OpenAI API key
client = openai.OpenAI(api_key=os.environ["DALLE_API_KEY"])


def call_dalle(description: str, gender: str):
    print('generating img..')

    response = client.images.generate(
        model="dall-e-3",
        prompt=
        '"gender": ' + gender + '\n' + """
            "default prompt": "Generate a photo-realistic frontal image of a person in neat clothing.",
            "style": "photo-realistic",
            "size": "256x256",
            "nationality": "Korean"
            "Composition and framing": "The face and upper body should be centered in the image, and The face should occupy half of the image."
            "Detailed description of the character": """
        + description,
        size="1024x1024",
        n=1,
    )
    url = response.data[0].url
    print('img generated. \nurl: ' + url)

    # URL에서 이미지 데이터 가져오기
    response = requests.get(url)
    response.raise_for_status()  # 에러가 발생했다면 예외를 발생시킴

    # BytesIO 객체로 메모리에 이미지 데이터를 로드
    img = Image.open(BytesIO(response.content))
    img = img.resize((256,256))

    print('removing bg..')
    trimmed_img = remove(img)
    print('bg removed.')

    return trimmed_img
