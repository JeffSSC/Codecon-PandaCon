import base64
import os
from openai import OpenAI
from PIL import Image
from io import BytesIO
from IPython.display import Image as IPImage, display
from config import OPENAI_API_KEY
from flask import Flask

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def panda_image():
    return "<p>Hello, World!</p>"

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))

# Create imgs/ folder
folder_path = "img"
os.makedirs(folder_path, exist_ok=True)

prompt_edit = "Coloque uma cabeça de panda igual ao da codecon nessa pessoa."
img_path_edit = "img/resultado.jpg"

img1 = open("./fabiano.jpg", "rb")
img2 = open("img/panda.png", "rb")

# Generate the new image
result_edit = client.images.edit(
    model="gpt-image-1",
    image=[img1,img2], 
    prompt=prompt_edit,
    size="1024x1536"
)

# Save the image to a file and resize/compress for smaller files
image_base64 = result_edit.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

image = Image.open(BytesIO(image_bytes))
image.save(img_path_edit, format="JPEG", quality=80, optimize=True)

# Show the result
display(IPImage(img_path_edit))