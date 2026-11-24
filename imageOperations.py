import numpy as np
from PIL import Image
import matplotlib.pyplot as plt



img = np.array(Image.open('images.jpeg').convert('RGB'))

gray = (
    0.299 * img[..., 0] +
    0.587 * img[..., 1] +
    0.114 * img[..., 2]
).astype(np.uint8)
# plt.imshow(Image.fromarray(gray),cmap="gray")

crop = img[150:300, 150:450 ]
plt.imshow(crop)

imgflip=  Image.fromarray(np.flipud(img))
plt.imshow(imgflip)
plt.show(imgflip)
