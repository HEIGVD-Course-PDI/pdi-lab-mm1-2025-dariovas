import matplotlib.pyplot as plt
import simpy
import models.simpy_m_m_1 as simpy_mm1

# Default parameters
SERVICE_RATE = 50.0  # Service rate (clients per second)
SIM_DURATION = 10_000  # Duration of the simulation (seconds)

def main(service_rate=SERVICE_RATE, sim_duration=SIM_DURATION):
    """Run the M/M/1 queue simulation.

    The function takes the arrival rate, service duration, and simulation duration as parameters.
    It returns the mean response time and mean number of clients in the system.
    """
    # Create a set of values for ARRIVAL_RATE
    arrival_rate = [1.0, 10.0, 12.0, 22.0, 36.0, 45.0, 49.0, 50.0]
    
    # Initialise the list to store the results.
    rhos = []
    mean_response_times = []
    mean_num_clients = []

    for i in arrival_rate:
        # Create the SimPy environment and the server
        env = simpy.Environment()
        server = simpy.Resource(env, capacity=1)
    
        # Create the M/M/1 queueing system
        mm1_queue = simpy_mm1.SimpyQueue(env, server, i, service_rate)

        # Start the request generator and the statistics recorder
        env.process(mm1_queue.generate_requests())
        env.process(mm1_queue.record_statistics(sampling_interval=1.0))

        # Run the simulation
        env.run(until=sim_duration)
        result = mm1_queue.compute_statistics()

        mean_response_times.append(result["E[T]"])
        mean_num_clients.append(result["E[N]"])
        rhos.append(i / service_rate)
    
    # Plot E[T]
    plt.figure()
    plt.plot(rhos, mean_response_times, "o-", label="E[T] simulated")
    plt.xlabel("Utilization p")
    plt.ylabel("Mean response time (s)")
    plt.grid(True)
    plt.legend()
    plt.savefig("mm1_t.png")

    # Plot E[N]
    plt.figure()
    plt.plot(rhos, mean_num_clients, "o-", label="E[N] simulated")
    plt.xlabel("Utilization p")
    plt.ylabel("Mean number of clients")
    plt.grid(True)
    plt.legend()
    plt.savefig("mm1_n.png")


if __name__ == "__main__":
    main()
