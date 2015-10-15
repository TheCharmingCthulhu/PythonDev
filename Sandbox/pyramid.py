import random

def Pyramid(size, chr_start, chr_end):
    stars = 0;
    for space in range(size, 0, -1):
        stars += 1;
        amount = (stars * 2) - 1
        print ' ' * space + '*' * amount;

   

Pyramid(25, 97, 122);
