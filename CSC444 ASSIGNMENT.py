
# coding: utf-8

# In[2]:


# Python program for implementation of RR Scheduling
avgTT =[]
avgWT = []
count = 0
quantum = [10, 25, 50]
while count< 3:
    print("ITERATION", count)
    print("Enter Total Process Number: ")
    total_p_no = int(input())
    total_time = 0 
    total_time_counted = 0
    # proc is process list
    proc = []
    wait_time = 0
    turnaround_time = 0
    for _ in range(total_p_no):
        # Getting the input for process
        print("Enter process arrival time and burst time") 
        input_info = list(map(int, input().split(" ")))
        arrival, burst, remaining_time = input_info[0], input_info[1], input_info[1]
        # processes are appended to the proc list in following format
        proc.append([arrival, burst, remaining_time, 0])
        # total_time gets incremented with burst time of each process
        total_time += burst

    time_quantum = quantum[count]
    print("The Quantum time is: ", time_quantum)
    # Keep traversing in round robin manner until the total_time == 0
    while total_time != 0:
        # traverse all the processes
        for i in range(len(proc)):
            # proc[i][2] here refers to remaining_time for each process i.e "i"
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                # the process has completely ended here thus setting it's remaining time to 0.
                proc[i][2] = 0 
            elif proc[i][2] > 0:
                # if process has not finished, decrementing it's remaining time by time_quantum
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                # if remaining time of process is 0
                # and 
                # individual waiting time of process has not been calculated i.e flag
                wait_time += total_time_counted - proc[i][0] - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                # flag is set to 1 once wait time is calculated
                proc[i][3] = 1 
    avg_waiting_time = (wait_time * 1) / total_p_no 
    avg_TaT = (turnaround_time * 1) / total_p_no
    print("average waiting time ", avg_waiting_time )
    print("average turnaround time ", avg_TaT)
    print("\n")
    print("----------------------------------------------------------------------------------------------")
    avgWT.append(avg_waiting_time)
    avgTT.append(avg_TaT)
    count += 1
print("Average  Waiting time for all Q: ", avgWT)
print("Average Turnaround time for all Q: ", avgTT)
print("\n")
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
print("\n")
print("OBSERVATIONS: ")
print("\n")
print("It had a deterministic response time")
print("when the quantum time is small, the context switching increases")
print("when the quantum time is large, response time is reduced and behaves like FIFO algorithm")

