import base64
import os
from openai import OpenAI
from PIL import Image
from io import BytesIO
from config import OPENAI_API_KEY
from flask import Flask, request, jsonify, url_for
import os
from datetime import datetime

app = Flask(__name__)

# Diretório para salvar as imagens
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Extensões permitidas
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/teste', methods=['GET'])
def teste():
    return jsonify({'mensagem': 'API está funcionando!'}), 200

@app.route('/api/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'erro': 'Nenhum arquivo encontrado na requisição.'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'erro': 'Nenhum arquivo selecionado.'}), 400

    if file and allowed_file(file.filename):
        # Obtém a extensão do arquivo
        ext = file.filename.rsplit('.', 1)[1].lower()
        # Define o nome do arquivo como 'pessoa' com a extensão original
        filename = f'pessoa.png'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", OPENAI_API_KEY))

        prompt_edit = "Troque a cabeça da pessoa na imagem por uma cabeça de um animal aleatório."
        os.makedirs("static", exist_ok=True)
        name = datetime.now().strftime("%Y%m%d%H%M%S")
        img_path_edit = f"static/{name}.jpg"

        img1 = open("./img/pessoa.png", "rb")

        # Generate the new image
        result_edit = client.images.edit(
            model="gpt-image-1",
            image=[img1], 
            prompt=prompt_edit,
            size="1024x1536"
        )

        # Save the image to a file and resize/compress for smaller files
        image_base64 = result_edit.data[0].b64_json
        image_bytes = base64.b64decode(image_base64)

        image = Image.open(BytesIO(image_bytes))
        image.save(img_path_edit, format="JPEG", quality=80, optimize=True)

        return jsonify({
        'mensagem': 'Arquivo enviado com sucesso.',
        'caminho': url_for('static', filename=f'{name}.jpg')
        }), 200
    else:
        return jsonify({'erro': 'Tipo de arquivo não permitido. Apenas PNG, JPG e JPEG são aceitos.'}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)