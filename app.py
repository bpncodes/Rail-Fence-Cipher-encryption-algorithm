from flask import Flask, request, render_template
from encrypt import rail_fence_cipher_encrypt
from decrypt import decryptRailFence
import pdb
from waitress import serve

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        choice = request.form['choice']
        input_string = request.form['input_text']
        key_depth = int(request.form['key_depth'])
        key_repeat = int(request.form['key_repeat'])
        result = ""
        if choice == 'encryption':
        #     pdb.set_trace()
            result = rail_fence_cipher_encrypt(input_string, (key_depth, key_repeat))
        elif choice == 'decryption':
            result = decryptRailFence(input_string, key_depth, key_repeat)
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    # app.run()
    serve(app, listen='*:8080')


