from flask import Flask, request
from googletrans import Translator
import text2emotion as te
app = Flask(__name__)


@app.route('/')
def hello():
    a = te.get_emotion("hello World how are hope you are fine")
    print(a)
    return "a"


@app.route('/emotion', methods=['POST'])
def emotion():
    body = request.json
    l = " ".join(body)
    print(str(body))
    print(l)
    ans = te.get_emotion(l)
    print(ans)
    emo = ""
    val = 0
    for key, value in ans.items():
        if (value > val):
            print(value)
            val = value
            emo = key

    if val == 0:
        return "Neutral"

    return emo


@app.route('/translate', methods=['POST'])
def translate():
    body = request.json
    l = " ".join(body)

    translator = Translator()

    print(translator.translate('안녕하세요.'))

    return l


if __name__ == "__main__":
    app.run(debug=True, port=5001)
