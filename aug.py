# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
from PIL import Image

# 画像を読み込む。

base_path='base/'
save_path='aaa/'
import os
os.makedirs(save_path, exist_ok=True)

#plt.imshow(img)
#plt.show()

# 画像データ生成器を作成する。
# -20° ~ 20° の範囲でランダムに回転を行う。
#datagen = image.ImageDataGenerator(rotation_range=20)
#datagen = image.ImageDataGenerator(width_shift_range=0.1)
#datagen = image.ImageDataGenerator(brightness_range=[0.3, 1.0])
#datagen = image.ImageDataGenerator(shear_range=5)
#datagen = image.ImageDataGenerator(zoom_range=0.2)
datagen = image.ImageDataGenerator(
    rotation_range=10,
    zoom_range=0.1,
    width_shift_range=0.1,
    brightness_range=[0.3, 1.0],
    shear_range=5)

files = os.listdir(base_path)
dirs = [f for f in files if os.path.isdir(os.path.join(base_path, f))]

for dir in dirs:
    print("Generating image for " + dir + ".")
    os.makedirs(save_path + dir, exist_ok=True)
    for file in os.listdir(base_path + dir):
        img = image.load_img(base_path + dir + '/' + file)
        img = np.array(img)
        x = img[np.newaxis]  #  (Height, Width, Channels)  -> (1, Height, Width, Channels)         
        
        gen = datagen.flow(x, batch_size=1, save_to_dir=save_path + dir,
                   save_prefix='generated', save_format='png')
        for i in range(100):
            next(gen)

#    batches = next(gen)  # (NumBatches, Height, Width, Channels) の4次元データを返す。
    # 画像として表示するため、3次元データにし、float から uint8 にキャストする。
#    gen_img = batches[0].astype(np.uint8)

#    plt.subplot(10, 10, i + 1)
#    plt.imshow(gen_img)
#    plt.axis('off')

#plt.show()