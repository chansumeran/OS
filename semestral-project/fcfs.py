import operator 
from statistics import mean

class FCFS:
  """
    FCFS Implementation with consideration for idle time.
  """

  def __init__(self, processes) -> None:
    self.processes = processes
    self.current_time = 0
    # Sorted by arrival time first, then process_id. 
    self.sorted = sorted(self.processes, key=operator.attrgetter("at", "process_id"))

  def solve(self):
    for current_process in self.sorted:
      print(f"Process started execution at time {self.current_time}")
      self.current_time += current_process.bt
      self.update_params(current_process)
      print(f"Process {current_process.process_id} completed at time {self.current_time}")

  def gantt_chart(self, completion_times):
    max_time = max(completion_times) + 1
    chart_string = ""

    # indicates the time using "-"
    chart_string += "0" + "-" * (max_time) + "\n"

    # bars for each process
    for time in completion_times:
      chart_string += "-" * time + "|" + "-" * (max_time - time) + "\n"

    print("\nGantt Chart\n" + chart_string)

  def update_params(self, current_process):
    current_process.et = self.current_time
    current_process.tt = current_process.et - current_process.at
    current_process.wt = current_process.tt - current_process.bt

  def att(self):
    return round(sum([p.tt for p in self.processes]) / len(self.processes), 2)
  
  def awt(self):
    return round(sum([p.wt for p in self.processes]) / len(self.processes), 2)