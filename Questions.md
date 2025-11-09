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
        yield self.env.process(self.process_request())


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
        service_duration = np.random.exponential(self.service_time)
        yield self.env.timeout(service_duration)

    departure_time = self.env.now
    self.response_times.append(departure_time - arrival_time)
```

2-Validate the simulation model
-------------------------------

#### Show at least 3 different simulation results with different parameters and compare them with the analytical model. (6p)

*The parameter `p` is defined as the ratio of the arrival rate to the service rate.*

*To simulate the M/M/1 queue, we consider three values of p : `0.2`, `0.6` and `0.8`. These values are chosen to show the impact on the expected response time E[T] and the expected number of clients in the system E[N].*

*Below is the analytical model, where the expected number of clients in the system E[N] is calculated using E[N] = p/(1-p) and the expected response time E[T] is calculated using E[T] = 1/(SERVICE_RATE - ARRIVAL_RATE). The values corresponding to the different chosen values of P are as follows :* 

- p = `0.2` : E[N] = 0,25 and E[T] = 0,025.
- p = `0.6` : E[N] = 1,5 and E[T] = 0,05.
- p = `0.8` : E[N] = 4 and E[T] = 0,1.

![](./images/queue_behavior_mm1.png)

*Below is the differents results reported during the simulation.*

```bash
With p = 0.2

Mean response time: 0.0201 seconds
Mean number of clients in the system: 0.1672

With p = 0.6

Mean response time: 0.0200 seconds
Mean number of clients in the system: 0.3814

With p = 0.8

Mean response time: 0.0201 seconds
Mean number of clients in the system: 0.4443

```

*To conclude, the simulated results follow the analytical model. For low load, in the case where p = `0,2`, the simulation is close to the analytical values. As the load increases, in the cases where p = `0,6` and p = `0,8`, the simulation underestimates the expected number of clients and response time compared to the analytical model. However, the simulation and the anaylitical model show the same trend, higher load leads to longer queues and higher response times.*


3-Evaluate the impact of an load increase
-----------------------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`? (2p)

*Below is the simulation results when running with ARRIVAL_RATE = `30/s` and SERVICE_RATE = `50/s`.*

```bash
Mean response time: 0.0200 seconds
Mean number of clients in the system: 0.3830
```

#### What are the simulation results when running with a 40% increased `ARRIVAL_RATE`? (2p)

*Below is the simulation results when running with a 40% increased ARRIVAL_RATE, which leads the value from `30` to `42`.*

```bash
Mean response time: 0.0200 seconds
Mean number of clients in the system: 0.4585
```

#### Interpret and explain the results. (3p)

*As the arrival rate increases by 40%, the system load P increases from 0,6 to 0,84.Both the number of clients and the response time increasae significantly. This sohws that the M/M/1 queue becomes more congested under higher load, as their curves are exponential.*


4-Doubling the arrival rate
---------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`? What is the utilization of the server? (2p)

*Your answer here*

#### What is the value of `SERVICE_RATE` that achieves the same mean response time when doubling the `ARRIVAL_RATE` to `80/s`? What is the server utilization in that case? (2p)

*Your answer here*

#### Use the analytical M/M/1 model to confirm your findings. (3p)

*Your answer here*

#### Describe and interpret the results. (3p)

*Your answer here*


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
