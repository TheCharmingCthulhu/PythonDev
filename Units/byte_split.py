def split_array(block_size, limit):
    lst = []

    for n in range(1, limit):
        if block_size % n == 0:
            lst.append(n)

    return max(lst)

print split_array(int(raw_input("Bytes:")), int(raw_input("Limit:")))
