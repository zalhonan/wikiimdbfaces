import matplotlib.pyplot as plt
import numpy as np
from utils import get_meta
import matplotlib.image as mpimg
from skimage import io
from skimage.transform import rescale, resize

db = "wiki"
# db = "imdb"
mat_path = f"data/{db}_crop/{db}.mat"
imgs_path = f"data/{db}_crop/"
full_path, dob, gender, photo_taken, face_score, second_face_score, age, name = get_meta(mat_path, db)

imgs = []
labels = []

for counter in range(0, 100): #range(len(full_path)):
    if face_score[counter] > 0.5 and (gender[counter] == 0 or gender[counter] == 1):
        labels.append(gender[counter])
        img = io.imread(imgs_path + full_path[counter][0])
        img = resize(img, (150,150,3))
        imgs.append(img)
        print (counter)

from keras.utils.np_utils import to_categorical

X = np.array(imgs)
y = to_categorical(np.array(labels))

#[0, 1] - man, [1, 0] - woman

#plt.imshow(X[3])
#Y[1]

np.save('X_wiki_2', X)
np.save('y_wiki_2', y)

