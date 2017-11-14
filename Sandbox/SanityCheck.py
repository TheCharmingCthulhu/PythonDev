value = 0

while True:
    cmd = raw_input("Inc/Dec: ")
    if cmd == "inc":
        value = value + 1
    elif cmd == "dec":
        value = value - 1

    print value
