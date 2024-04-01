import operator as op
from process import Process

class SJF:
    def __init__(self, processes : list) -> None:
        self.processes = processes
        self.current_time = 0
        self.processes_in_cpu = []
        # self.sorted = sorted(self.processes, key=op.attrgetter("bt", "at"))
        self.copy = self.processes.copy()
        
            
    def solve(self):
        self.set_first_processes()
        self.show_processes_in_cpu()
        print()
        
        while self.processes_in_cpu:            
            self.show_processes_in_cpu()

            processes_sorted_in_cpu = sorted(self.processes_in_cpu, key=op.attrgetter("bt", "at", "process_id"))
            
            process = processes_sorted_in_cpu[0]
            print(f"Process {process.process_id} started at time {self.current_time}")
            
            self.current_time += process.bt
            
            # update params
            original = self.find_by_id(process.process_id)
            original.et = self.current_time
            original.tt = original.et - original.at
            original.wt = original.tt - original.bt
            
            self.remove_process(process)
            self.update_cpu_processes()
            
            print(f"Process {process.process_id} ended at time {self.current_time}")
        
        print("P\tAT\tBT\tET\tTT\tWT")        
        for p in self.processes:
            print(f"P{p.process_id}\t{p.at}\t{p.bt}\t{p.et}\t{p.tt}\t{p.wt}")
        print(self.att())
        print(self.awt())
    
    def remove_process(self, process):
        for p in self.copy:
            if p.process_id == process.process_id:
                self.copy.remove(p)
                
        for p in self.processes_in_cpu:
            if p.process_id == process.process_id:
                self.processes_in_cpu.remove(p)

    
    def set_first_processes(self):
        while not self.processes_in_cpu:
            for p in self.copy:
                if p.at <= self.current_time:
                    self.processes_in_cpu.append(p)
                    self.copy.remove(p)
                    
            if not self.processes_in_cpu:
                self.current_time += 1

    def update_cpu_processes(self):
        for p in self.copy:
            if p.at <= self.current_time and not self.exists(p):
                self.processes_in_cpu.append(p)
                
    def exists(self, process):
        for p in self.processes_in_cpu:
            if p.process_id == process.process_id:
                return True
        return False
    
    def find_by_id(self, id):
        for p in self.processes:
            if p.process_id == id:
                return p
        return None
                
    def show_processes_in_cpu(self):
        for p in self.processes_in_cpu:
            print(f"P{p.process_id}, AT:{p.at}, BT:{p.bt}")

    def att(self):
        return round(sum([p.tt for p in self.processes]) / len(self.processes), 2)
    
    def awt(self):
        return round(sum([p.wt for p in self.processes]) / len(self.processes), 2)        
    
    
# test
p1 = Process(1, 3, 4)
p2 = Process(2, 5, 9)
p3 = Process(3, 8, 4)
p4 = Process(4, 0, 7)
p5 = Process(5, 12, 6)

processes = [p1, p2, p3, p4, p5]
fcfs = SJF(processes)
fcfs.solve()