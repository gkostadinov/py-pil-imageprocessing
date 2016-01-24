# A small example of training an SVM and classifying an input data
import cv2
import numpy as np
import matplotlib.pyplot as plt


def get_human_label(raw_label):
    return 'red' if raw_label == 0 else 'blue'


def main():
    # Create a sample training data and associated labels
    train_data = np.array([[1, 1], [2, 2], [2, 1], [1, 2], [3, 1],
                           [2, 3], [3, 3], [4, 3], [3, 2], [4, 2]],
                          dtype=np.float32)
    labels = np.array([0, 0, 0, 0, 0,
                       1, 1, 1, 1, 1],
                      dtype=np.float32)

    # Initialize the SVM and train on the training data
    svm = cv2.SVM()
    svm.train(train_data, labels)

    # Create a sample input data
    input_data = np.array(
        [[3.5, 2.5], [1.5, 1.5], [2.51, 2], [2.49, 2]], dtype=np.float32)

    # Plot the training data
    # Red data
    red = train_data[labels.ravel() == 0]
    plt.scatter(red[:, 0], red[:, 1], s=50, c='r', marker='^')

    # Blue data
    blue = train_data[labels.ravel() == 1]
    plt.scatter(blue[:, 0], blue[:, 1], s=50, c='b', marker='s')

    # Plot the input data - green
    plt.scatter(input_data[:, 0], input_data[:, 1], s=50, c='g', marker='o')

    results = svm.predict_all(input_data)

    for i, result in enumerate(results.tolist()):
        print('Point #%s (%s, %s) classified as: %s'
              % (i + 1, input_data[i][0], input_data[i][1],
                 get_human_label(result[0])))

    plt.show()

if __name__ == '__main__':
    main()
