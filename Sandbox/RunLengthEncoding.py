# -*- coding: cp1252 -*-


def EncodeRLE(items):
    idx = {}
    for item in items:
        if not item in idx:
            idx[item] = 1
        else:
            idx[item] += 1
    return idx;

def DecodeRLE(idx):
    loop_count = 0;
    items = [];
    for k in idx:
        if idx[k] > loop_count:
            loop_count = idx[k]

    for i in range(1, loop_count+1):
        for k in idx:
            if idx[k] >= i:
                items.append(k)
    return items

test_str = 'Portale sind von Wikipedianern redaktionell gepflegte Einstiegsseiten in die Enzyklopädie. Sie präsentieren eine Übersicht der wichtigsten Artikel zu einem Themengebiet und verraten, welche Artikel neu geschrieben worden sind und welche gerade Hilfe benötigen.'
split_str = test_str.split(' ');
print test_str

erle = EncodeRLE(split_str)
derle = DecodeRLE(erle)
print erle
print derle
