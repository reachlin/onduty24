#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import os
import urllib

import numpy as np
import tensorflow as tf


def main():
  # Load datasets.
  training_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename="data/train.csv",
    target_dtype=np.int,
    features_dtype=np.int,
    target_column=0)
  test_set = tf.contrib.learn.datasets.base.load_csv_without_header(
    filename="data/test.csv",
    target_dtype=np.int,
    features_dtype=np.int,
    target_column=0)

  # Specify that all features have real-value data
  feature_columns = [tf.contrib.layers.real_valued_column("", dimension=10000)]

  # Build 3 layer DNN with 10, 20, 10 units respectively.
  classifier = tf.contrib.learn.DNNClassifier(feature_columns=feature_columns,
                                              hidden_units=[10, 20, 10],
                                              n_classes=3, #green, yellow, red
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
