from process import Process
from fcfs import FCFS

def main():
    p1 = Process(1, 3, 4)
    p2 = Process(2, 5, 9)
    p3 = Process(3, 8, 4)
    p4 = Process(4, 0, 7)
    p5 = Process(5, 12, 6)

    processes = [p1, p2, p3, p4, p5]
    fcfs = FCFS(processes)
    fcfs.solve()

    # Get completion times from each process object after solve()
    completion_times = [process.et for process in processes]
    fcfs.gantt_chart(completion_times)

    print(f"Average Turnaround Time: {fcfs.att()}")
    print(f"Average Waiting Time: {fcfs.awt()}")

    
if __name__ == "__main__":
    main()