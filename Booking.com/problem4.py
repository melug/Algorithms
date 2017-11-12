

def howManyAgentsToAdd(noOfCurrentAgents, callsTimes):
    callsTimes.sort()
    maximum_parallel_calls = 0
    for i in xrange(len(callsTimes)):
        intersection = callsTimes[i]
        parallel_calls = 0
        for j in xrange(i, len(callsTimes)):
            if intersection[1]<callsTimes[j][0]:
                parallel_calls += 1
                intersection[0] = max(intersection[0], callsTimes[j][0])
                intersection[1] = min(intersection[1], callsTimes[j][1])
            else:
                break
        maximum_parallel_calls = max(maximum_parallel_calls, parallel_calls)


