import time as t
timer = 0;
running = True;

def Timing():
    global timer;
    while running:
        timer += 1;
        t.sleep(1);
        print 'Current time: ' + str(timer);

Timing();
