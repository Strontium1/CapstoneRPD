# Smart Farm
## About Our Project
<p align="justify"> The majority of the people in Indonesia work as farmers and rely on the environment to provide for all of their necessities, making it one of the most agricultural nations. Comparatively speaking, rice is one of the food items that Indonesia imports the most from any other nation. Thus, agriculture is one of the largest sectors of employment in the country, providing job opportunities to approximately 49 million people. Although agriculture has many great opportunities for the community, crop failure is also something that farmers often face. Crop failure due to sickness is one of the factors that limit the productivity of agricultural crops in Indonesia, especially rice, which is the main staple food. Some of the soil-borne pathogens that cause crop failure can cause very high losses in economic terms and affect the food security of the country. Therefore, our app exists to assist farmers with handling illnesses that are frequently seen in rice plants by using computer vision to classify rice plant diseases and giving treatment recommendations for farmers to treat their crops. Our hope is that our application can improve our country's quality of rice and help Indonesia become "Lumbung Padi Asia". </p>

## About the Model
We are using transfer learning on CNN models, specifically MobileNetv3 as it can accelerate training time and reducing misclassification rate which may prove fatal to the user. Our model was trained on few thousand images that you can check [here](https://drive.google.com/file/d/1ZHLZC8wypY0ppUMRUzzd6eTwDXx5rI7A/view?usp=drive_link). To retrain or do further training on our model, you can use our dataset, or provide your own images. Before inputting to our model, make sure to resize it to 224x224, in RGB color format, and batched. For complete overview, please refer to the ```Multi Class.ipynb``` notebook as it contains the complete code on loading the dataset and train the model. If you wish to contribute to our model, feel free to fork this repository.

## Requirements
- Python 3.8 or later
- Tensorflow 2 or later

To run our model, you have to install [Python](https://www.python.org/downloads/), version 3.8 should be supported but latest one is preferred. For tutorials on how to install Python can be seen [here](https://realpython.com/installing-python/) or [here](https://www.tutorialspoint.com/how-to-install-python-in-windows).
Once you have installed Python, open Terminal and install Tensorflow using pip, extensive tutorial can be checked on it's official [website](https://www.tensorflow.org/install/pip).
``` 
pip install tensorflow
```
Once installed, you can run ```smartfarm.py``` using Python, enter the model's path which is ```/checkpoint/``` and choose either best or latest. After the model is loaded, enter the image's path you want to predict and the model will quickly output the predictions and it's probabilities.

## Credits
- (ML) M360DSX2575 – Rifqi Raenanda Faqih
- (ML) M038DSX0594 – Ignatius Pandu Adityawan
- (ML) M038DKX4046 – Akbar Fikriawan
- (CC) C360DSX2715 – Khoirul Azkiya
- (CC) C287DSX0818 – Muhammad Irfan Jazuli
- (MD) A360DSX3044 – Wijdan Khalil