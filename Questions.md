Questions to answer
==================================

These are the questions related to the M/M/1 queueing model using SimPy.

You will need to answer the questions in this file. Your answers will be graded. 

You can answer in English or French.


1-Implement the M/M/1 queueing model in SimPy
---------------------------------------------

### The implementation in the file `models/simpy_m_m_1.py` counts for 4 points maximum. (4p)

Below, you can find the implementation of the two functions `generate_requests` and `process_request`.

```py
def generate_requests(self):
    """Generate requests following a Poisson process."""
    while True:
        # ******** Add your code here ********
        # Generates the waiting time until the next client.
        interarrival_time = np.random.exponential(self.interarrival_time)
        # Waits this time.
        yield self.env.timeout(interarrival_time)
        # Process the request.
        self.env.process(self.process_request())


def process_request(self):
    """Place a request in the queue and process it when the server is available.
    
    The method also records statistics about the response time.
    """
    arrival_time = self.env.now

    # ******** Add your code here ********
    # Waits until the server is ready.
    with self.server.request() as req:
        yield req
        # Serves the client.
        yield self.env.timeout(np.random.exponential(self.service_time))

    departure_time = self.env.now
    self.response_times.append(departure_time - arrival_time)
```

2-Validate the simulation model
-------------------------------

#### Show at least 3 different simulation results with different parameters and compare them with the analytical model. (6p)

*The parameter `p` is defined as the ratio of the arrival rate to the service rate.*

*To simulate the M/M/1 queue, we consider three values of p : `0.2`, `0.6` and `0.8`. These values are chosen to show the impact on the expected response time E[T] and the expected number of clients in the system E[N].*

*Below is the analytical model, where the expected number of clients in the system E[N] is calculated using E[N] = p/(1-p) and the expected response time E[T] is calculated using E[T] = 1/(SERVICE_RATE - ARRIVAL_RATE). The values corresponding to the different chosen values of P are as follows :* 

- p = `0.2` : E[N] = 0.25 and E[T] = 0.025.
- p = `0.6` : E[N] = 1.5 and E[T] = 0.05.
- p = `0.8` : E[N] = 4 and E[T] = 0.1.

![](./images/queue_behavior_mm1.png)

*Below is the differents results reported during the simulation.*

```bash
With p = 0.2

Mean response time: 0.0251 seconds
Mean number of clients in the system: 0.2570

With p = 0.6

Mean response time: 0.0506 seconds
Mean number of clients in the system: 1.5097

With p = 0.8

Mean response time: 0.0992 seconds
Mean number of clients in the system: 3.9915
```

*In conclusion, the simulation and the analytical model give the same results. We can see that as p increases, meaning the system is busier, both the response time and the number of clients in the queue increase. This confirms that the M/M/1 model accurately describes the queue.*

3-Evaluate the impact of an load increase
-----------------------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`? (2p)

*Below is the simulation results when running with ARRIVAL_RATE = `30/s` and SERVICE_RATE = `50/s`.*

```bash
Mean response time: 0.0499 seconds
Mean number of clients in the system: 1.5114
```

#### What are the simulation results when running with a 40% increased `ARRIVAL_RATE`? (2p)

*Below is the simulation results when running with a 40% increased ARRIVAL_RATE, which leads the value from `30` to `42`.*

```bash
Mean response time: 0.1215 seconds
Mean number of clients in the system: 5.1218
```

#### Interpret and explain the results. (3p)

*As the arrival rate increases by 40%, the system load P increases from 0,6 to 0,84. Both the number of clients and the response time increase significantly. This shows that the M/M/1 queue becomes more congested under higher load, as their curves are exponential.*


4-Doubling the arrival rate
---------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`? What is the utilization of the server? (2p)

*Below is the simulation results when running with ARRIVAL_RATE = `40/s` and SERVICE_RATE = `50/s`.*

*The server utilization is given by `p = ARRIVAL_RATE/SERVICE_RATE`, in that case, `p = 40/50 = 0,8`. It means the server is busy 80% of the time.

```bash
Mean response time: 0.1013 seconds
Mean number of clients in the system: 4.0651
```

#### What is the value of `SERVICE_RATE` that achieves the same mean response time when doubling the `ARRIVAL_RATE` to `80/s`? What is the server utilization in that case? (2p)

*When we double the ARRIVAL_RATE, the server becomes overloaded and the mean response time increases dramatically.

```bash
Mean response time: 1876.1881 seconds
Mean number of clients in the system: 150165.7651
```

This occurs because p > 1, which means the M/M/1 queue is no longer stable. To archieve the same mean response time as before, we would need to choose a SERVICE_RATE that keeps p > 1.

#### Use the analytical M/M/1 model to confirm your findings. (3p)

*Using the analytical M/M/1 model, we know that the expected number of clients in the system E[N] is calculated using E[N] = p/(1-p) and the expected response time E[T] is calculated using E[T] = 1/(SERVICE_RATE - ARRIVAL_RATE). For an `ARRIVAL_RATE = 80/s` and `SERVICE_RATE = 50/s`, we get `p = 1.6 > 1`, E[N] = -2.66 and E[T] = -0.05. This confirms that the queue is unstable, because the mean response time and the mean number of clients in the system grow without bound.

#### Describe and interpret the results. (3p)

*The negative values for E[N] and E[T] indicate that the formulas are no more valid when p > 1. This happens because the arrival rate exceeds the service rate, which means that the server cannot process clients fast enough. Thus, the queue grows indefinitely.*


5-Rule of Bertsekas and Gallager
--------------------------------

#### Describe your experiments and results. (2p)

*Your answer here*

#### Provide an analytical explanation of your findings. (2p)

*Your answer here*


Conclusion
----------

#### Document your conclusions here. What did you learn in this lab? (2p)

*Your answer here*
