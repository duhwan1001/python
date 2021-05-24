# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# print(train_images[0])
#
# print(train_images.shape)
print(train_labels.shape)
#
# print(test_images.shape)
# print(test_labels.shape)

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# print(train_images[0])
#
# print(train_images.shape)
print(train_labels[1])
#
# print(test_images.shape)
# print(test_labels.shape)

train_labels = to_categorical(train_labels)

print(train_labels.shape)
print(train_labels[1])

test_labels = to_categorical(test_labels)

model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=128)

# test_loss, test_acc = model.evaluate(test_images, test_labels)
# print('test_acc: ', test_acc)
