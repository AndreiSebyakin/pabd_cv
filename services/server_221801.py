from flask import Flask, request
import tensorflow as tf

app = Flask('Image classifier')

model = tf.keras.models.load_model('models/my_model')


@app.route('/')
def home():
    """ Function docstring """
    return 'Home page'


@app.route('/classify/binary', methods=['POST'])
def classify_binary():
    data = request.data
    img = tf.io.decode_jpeg(data)
    img_t = tf.expand_dims(img, axis=0)
    img_t = tf.image.resize(img_t, (180, 180))
    predictions = model.predict(img_t)
    dog_probability = float(predictions[0])
    print(dog_probability)
    idx = dog_probability > 0.5
    return ('Cat', 'Dog')[idx]


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    input()
