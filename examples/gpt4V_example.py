import unicodedata
import matplotlib.pyplot as plt
from openai import OpenAI
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

client = OpenAI(
    api_key="sk-mnTfVOUdjIfBf8lAE6E45d150bD344Ac989fC120DbF65e89", # KEY
    base_url="https://lonlie.plus7.plus/v1"
)

inputs = "Describe this image in detail."
img = encode_image("/data/wl/code/CodeLLaVA/examples/matplotlib_images/sphx_glr_bar_colors_001.jpg")

completion = client.chat.completions.create(
    messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": inputs},
                        {
                            "type": "image_url",
                            "image_url": f"data:image/jpeg;base64,{img}",
                        },
                    ],
                }
            ],
    model="gpt-4-vision-preview",
    temperature=0.2
)

message = completion.choices[0].message
content = unicodedata.normalize('NFKC', message.content)
print(content)