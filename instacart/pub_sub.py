import threading, time
#https://dev.to/mandrewcito/fast-pub-sub-python-implementation-threading-ii-1khp

class EventChannel(object):
    def __init__(self):
        self.subscribers = {}

    def unsubscribe(self, event, callback):
        if event is not None or event != "" \
                and event in self.subscribers.keys():
            self.subscribers[event] = list(
                filter(
                    lambda x: x is not callback,
                    self.subscribers[event]
                )
            )

    def subscribe(self, event, callback):
        if not callable(callback):
            raise ValueError("callback must be callable")

        if event is None or event == "":
            raise ValueError("Event cant be empty")

        if event not in self.subscribers.keys():
            self.subscribers[event] = [callback]
        else:
            self.subscribers[event].append(callback)

    def publish(self, event, args):
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                callback(args)


class ThreadedEventChannel(EventChannel):
    def __init__(self, blocking=True):
        self.blocking = blocking
        super(ThreadedEventChannel, self).__init__()

    def publish(self, event, *args):
        threads = []
        if event in self.subscribers.keys():
            for callback in self.subscribers[event]:
                threads.append(threading.Thread(
                    target=callback,
                    args=args
                ))
            for th in threads:
                th.start()

            if self.blocking:
                for th in threads:
                    th.join()


if __name__ == '__main__':
    non_thread = EventChannel()
    threaded = ThreadedEventChannel()
    non_blocking_threaded = ThreadedEventChannel(blocking=False)

    non_thread.subscribe("myevent", time.sleep)
    non_thread.subscribe("myevent", time.sleep)
    start = time.time()
    non_thread.publish("myevent", 3)
    end = time.time()
    print("non threaded function elapsed time {0}".format(end - start))

    #non threaded function elapsed time 6.0080871582
    threaded.subscribe("myevent", time.sleep)
    threaded.subscribe("myevent", time.sleep)
    start = time.time()
    threaded.publish("myevent", 3)
    end = time.time()
    print("threaded function elapsed time {0}".format(end - start))
    # threaded function elapsed time 3.00581121445

    non_blocking_threaded.subscribe("myevent", time.sleep)
    non_blocking_threaded.subscribe("myevent", time.sleep)
    start = time.time()
    non_blocking_threaded.publish("myevent", 3)
    end = time.time()
    print("threaded function non blocking elapsed time {0}".format(end - start))
    # threaded function non blocking elapsed time 0.00333380699158
