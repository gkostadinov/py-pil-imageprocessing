# Example for training a kNN and classifying a given point
import cv2
import numpy as np
import matplotlib.pyplot as plt

DATA_SIZE = 30
MAX_INT = 100


def get_human_label(raw_label):
    return 'red' if raw_label == 0 else 'blue'


def main():
    # Training set of 20 random (x, y) values, x,y is between 0 and 49
    train_data = np.random.randint(
        0, MAX_INT, (DATA_SIZE, 2)).astype(np.float32)
    # Labels for each value in the training set - 0 for red, 1 for blue
    labels = np.random.randint(0, 2, (DATA_SIZE, 1)).astype(np.float32)

    # Red data: take all training data with label 0
    red = train_data[labels.ravel() == 0]
    # Plot: x points, y points, s - size of points,
    # c - color, marker - the shape
    plt.scatter(red[:, 0], red[:, 1], s=100, c='r', marker='^')

    # Blue data: take all training data with label 1
    blue = train_data[labels.ravel() == 1]
    plt.scatter(blue[:, 0], blue[:, 1], s=100, c='b', marker='s')

    # Green data: A single random (x, y) for input data
    input_data = np.random.randint(0, MAX_INT, (1, 2)).astype(np.float32)
    plt.scatter(input_data[:, 0], input_data[:, 1], s=100, c='g', marker='o')

    knn = cv2.ml.KNearest_create()
    knn.train(train_data, cv2.ml.ROW_SAMPLE, labels)
    # Find k=3 nearest neighbours and classify the given input data
    retval, results, neighbours, dists = knn.findNearest(input_data, k=5)

    classified_label = get_human_label(results[0][0])
    print('The input point (%s, %s) is %s'
          % (input_data[0][0], input_data[0][1], classified_label))
    for i, neighbour in enumerate(neighbours[0].tolist()):
        print('Neightbour #%s is %s, distance to point: %s'
              % (i + 1, get_human_label(neighbour), dists[0][i]))

    plt.show()

if __name__ == '__main__':
    main()
