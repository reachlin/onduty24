# onduty24

Neural Network Analysis on PagerDuty incident data.

The idea is to use a deep learning neutral network(e.g. CNN) to classify the whole system's status into green, yellow, or red. It will use historical Pagerduty incidents as its input data.

In a complex system, the on-call staff have to monitor hundreds of services. Sometimes, it is hard to decide if the whole system is in a good shape. For example, many incidents raised from non-essential services will raise unecessary panic.

This tool can be easily upgraded to a system failure root cause advisor for oncall engineers. The current output of the classifier is a comprehensive status of the system. It can be changed to an index of components with problems. This is useful, for example, when a base component fails, many upper layer will also report incidents, which makes it difficult to diagnose within the flood of incidents. Another example, when a machine reports an incident on it, the engineer has to spend time to investigate it. But when many of incidents are from the same machine, there's not much help to investigate each of them. It's very likely the machine is down, and reboot it will be much quicker solution. To detect clusters among incidents is also a useful function to develop.

TODO: talk about the format of data, and its holistic view of the system.

* pd_loader.py, a tool to monitor incidents from a specified escalation policy and create training or testing data in csv. All data will be labeled as '0' stands for all systems green in the first column. 1 for minor problems, 2 for major problems, and 3 for critical.

* learn.py, a neutral network studies the training data using tensorflow lib.


## References
* [Tensorflow](https://www.tensorflow.org/get_started/get_started)
* [The book](http://neuralnetworksanddeeplearning.com/chap1.html)
* [pygerduty](https://github.com/dropbox/pygerduty)
* [PagerDuty API](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Incidents/get_incidents)
