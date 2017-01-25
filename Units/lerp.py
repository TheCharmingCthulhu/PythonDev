def lerp(a, b, t):
    return a + (b - a) * t;

def lerpt(a, b, t):
    time = t;
    while time < 1:
        yield lerp(a, b, time);
        time = time + t;

for i in lerpt(100, 1, 0.0001):
    print i
