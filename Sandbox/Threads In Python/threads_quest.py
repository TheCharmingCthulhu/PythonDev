import threading, Queue

items = []

def Sum(q, a, b):
    q.put(a + b);

if __name__ == "__main__":
    q = Queue.Queue();

    for n in range(100000):
        x = threading.Thread(target=Sum, args=(q, n, n + 1));
        x.daemon = True;
        x.start();
        print q.get();
