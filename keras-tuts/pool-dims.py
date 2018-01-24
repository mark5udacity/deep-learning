from keras.models import Sequential
from keras.layers import MaxPooling2D


i = 2
while (i <= 100):
    j = 1

    while (j <= 100):
        pool_size = i
        strides = j

        print("\n\nsize: {} - strides: {}".format(pool_size, strides))
        model = Sequential()
        model.add(MaxPooling2D(pool_size=pool_size, strides=strides, input_shape=(100, 100, 15)))
        model.summary()
        print("\n\n")

        if j == 64:
            j = 100
        else:
            j *= 2


    if i == 64:
        i = 100
    else:
        i *= 2

print("All done!")
