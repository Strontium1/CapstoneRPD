print("Importing Libraries, please wait...")
import tensorflow as tf
import os
import sys
import time

### Loading Model ###
isRunning = True
while isRunning:
    os.system('cls||clear')
    model_path = input(r"Enter the model's folder: ")
    model_path = model_path.replace("\"", "")

    try:
        model = tf.keras.models.load_model(filepath=model_path)
        print("Model is loaded.")
        time.sleep(3)
    except:
        quitKey = input("No model found. Press Y/y to try again, else will quit the program.\n")
        if quitKey.lower() != 'y':
            sys.exit()
        continue
    isRunning = False

### Predicting Image ###
isPredicting = 'y'
#### Init Dictionary ####
dict_disease = {
    0: 'Bacterial Blight',
    1: 'Blast',
    2: 'Brownspot',
    3: 'Healthy',
    4: 'Leaf Scald',
    5: 'Bukan padi',
    6: 'Tungro'
}

while isPredicting == 'y':
    os.system('cls||clear')
    image_path = input(r"Enter the image's path to predict: ")
    image_path = image_path.replace("\"", "")

    try:
        image  = tf.keras.utils.load_img(image_path, target_size=(224,224))
    except:
        quitKey = input("No image found. Press Y/y to try again, else will quit the program.\n")
        if quitKey.lower() != 'y':
            sys.exit()
        continue

    print("Image loaded.")
    time.sleep(2)
    os.system('cls||clear')
    
    image  = tf.cast(image, tf.float32)
    image  = tf.expand_dims(image, axis=0)
    yhat   = tf.nn.softmax(model.predict(image, verbose=0))
    yhat   = tf.math.top_k(yhat, k=3)
    proba  = tf.get_static_value(yhat.values)[0]
    yhat   = tf.get_static_value(yhat.indices)[0]

    print("Prediction is:\n")
    for index_disease, disease in enumerate(yhat):
        res = f"{index_disease+1}: {dict_disease[disease]}, {proba[index_disease] * 100:.2f}%."
        print(res)

    isPredicting = input("\nPress Y/y to try again, else quit.").lower()