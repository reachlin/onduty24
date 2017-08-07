# onduty24

Neural Network Analysis on PagerDuty incident data.

The idea is to use a deep learning neutral network to classify the whole system's status. It will use history Pagerduty incidents as the data. In a complex system, the on-call staff have to monitor hundreds of services. Sometimes, it is hard to decide if the whole system is in a good shape. For example, many incidents raised from non-essential services will raise unecessary panic.

* pd_loader.py, a tool to monitor incidents from a specified escalation policy and create training or testing data in csv. All data will be labeled as '0' stands for all systems green in the first column. 1 for minor problems, 2 for major problems, and 3 for critical.

* learn.py, a tool study the training data using tensorflow lib.


