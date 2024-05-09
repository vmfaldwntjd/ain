import openai
from PIL import Image
import requests
from io import BytesIO
from rembg import remove


# Replace YOUR_API_KEY with your OpenAI API key
# client = openai.OpenAI(api_key="sk-proj-11iQpnbfPtbYOtv7v86PT3BlbkFJNMSJmpCfX0UdUMoGIs1U")
# api key는 나중에 환경 변수로 대체될 예정

def call_dalle(description: str, gender: str):
    # print('generating img..')

    # response = client.images.generate(
    #     model="dall-e-2",
    #     prompt="a cute cat with a hat on",
    #     size="256x256",
    #     n=1,
    # )
    # url = response.data[0].url
    # print('img generated. \nurl: ' + url)

    url = 'https://ain-bucket.s3.ap-northeast-2.amazonaws.com/da6c9a6a-f0ce-4c6d-aa96-ff81ad5d24a9.png'

    # URL에서 이미지 데이터 가져오기
    response = requests.get(url)
    response.raise_for_status()  # 에러가 발생했다면 예외를 발생시킴

    # BytesIO 객체로 메모리에 이미지 데이터를 로드
    img = Image.open(BytesIO(response.content))

    print('removing bg..')
    trimmed_img = remove(img)
    print('bg removed.')

    return trimmed_img

## 체크사항
# 사이즈 정사각형
# 한국인
# 옷 입힐 것 (옷 안 입을 때 종종 있음)
