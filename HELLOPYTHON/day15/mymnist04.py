import cv2
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical
import numpy as np


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(test_labels[0])

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images_refine = test_images.reshape((10000, 28 * 28))
test_images_refine = test_images_refine.astype('float32') / 255

train_labels = to_categorical(train_labels)
# test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_images_refine)

cnt_o = 0
cnt_x = 0

for idx, pred in enumerate(predictions):
    mypred = np.argmax(pred)
    mygoog = test_labels[idx]
    if mypred == mygoog:
        cnt_o += 1
    else:
        cnt_x += 1
        cv2.imwrite("miss/" + str(idx) + "_" + str(mypred) +"_" + str(mygoog) + ".jpg", test_images[idx])
        
print(cnt_o, cnt_x)
cv2.waitKey()
cv2.destroyAllWindows()