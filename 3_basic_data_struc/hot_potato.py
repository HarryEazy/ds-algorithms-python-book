from Queue import Queue


def hot_potato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

   # while simqueue.size() > 1:
    for i in range(num):
        simqueue.enqueue(simqueue.dequeue())
    simqueue.dequeue()
    print(f'You Last -> {simqueue.dequeue()}')
    return simqueue.dequeue()

names = ['0', '1', '2', '3', '4']
hot_potato(names, 4)
