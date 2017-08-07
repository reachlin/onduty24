#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import urllib

import numpy as np
import tensorflow as tf
from tensorflow.python.platform import gfile


def load_convert_csv_without_header(filename):
  """Load dataset from CSV file without a header row."""
  target_column = 0
  target_dtype = np.int
  features_dtype = np.int
  with gfile.Open(filename) as csv_file:
    data_file = csv.reader(csv_file)
    data, target = [], []
    for row in data_file:
      target.append(row.pop(target_column))
      # merge row as a giant string then convert to a list of ASCII int
      row_int = []
      for item in row:
        for char in item:
          row_int.append(ord(char))
      # max 10k
      row_int.extend([0]*(10000-len(row_int)))
      data.append(row_int)

    target = np.array(target, dtype=target_dtype)
    import pdb; pdb.set_trace()
    ndata = np.asmatrix(data, dtype=features_dtype)

    return tf.contrib.learn.datasets.base.Dataset(data=ndata, target=target)

def main():
  # Load datasets.
  training_set = load_convert_csv_without_header("data/small.csv")
  test_set = load_convert_csv_without_header("data/test.csv")

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=10000)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[10, 20, 10],
                                              n_classes=4,
                                              model_dir="data/pd_model")
  # Define the training inputs
  def get_train_inputs():
    x = tf.constant(training_set.data)
    y = tf.constant(training_set.target)

    return x, y

  # Fit model.
  classifier.fit(input_fn=get_train_inputs, steps=2000)

  # Define the test inputs
  def get_test_inputs():
    x = tf.constant(test_set.data)
    y = tf.constant(test_set.target)

    return x, y

  # Evaluate accuracy.
  accuracy_score = classifier.evaluate(input_fn=get_test_inputs,
                                       steps=1)["accuracy"]

  print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

  # Classify two new flower samples.
  '''
  def new_samples():
    return np.array(
      [[6.4, 3.2, 4.5, 1.5],
       [5.8, 3.1, 5.0, 1.7]], dtype=np.float32)

  predictions = list(classifier.predict(input_fn=new_samples))

  print(
      "New Samples, Class Predictions:    {}\n"
      .format(predictions))
  '''

if __name__ == "__main__":
    main()
