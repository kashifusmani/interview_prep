'''
1a) "Given a string of server-statuses ("1 0 0 1")
and a time that the server was taken offline, determine how many statuses the server was off by.
0 indicates the server is running, 1 indicates the server is offline"

1b) "Given the previous, determine when the best time would have been to take the server offline. "

2a) "Ok given a string with multiple server statuses nested together, determine the best time to take the server offline"
example strings were like "BEGIN BEGIN 0 0 1 END BEGIN 0 1 END", but only for the inner-most BEGIN/END combinations."

Question about allocating and deallocating servers.
The question was along the lines of allocating and deallocating the id of an api host.
Allocation happens when the server comes online and deallocation happens when the server goes offline or crashes
Implement a system to keep track of, allocate and deallocate server names
Write a function compute penalty that computes the total penalty given a server log (as a string)
AND a time at which we removed the server from the network (call that variable remove_at_.

'''