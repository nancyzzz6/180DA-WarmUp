# # https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
# # I added the video feed part for the code
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def find_histogram(clt):
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    return bar

# Open video feed
cap = cv2.VideoCapture(0)  

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Reshape the frame
    img = frame_rgb.reshape((frame_rgb.shape[0] * frame_rgb.shape[1], 3))
    # Apply K-Means clustering
    clt = KMeans(n_clusters=3)
    clt.fit(img)
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)
# Display the result
    cv2.imshow('Camera View', cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR))
    cv2.imshow('Dominant Color', cv2.cvtColor(bar, cv2.COLOR_RGB2BGR))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


# The object is more robust to brightness.