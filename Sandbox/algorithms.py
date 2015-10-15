import Shapes

def Euclideon(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a = a - b;
        elif b >= a:
            b = b - a;

    if a == 0:
        return b;
    else:
        return a;


if __name__ == "__main__":
    print Euclideon(42, 32);

    ShapeList = [];
    FarmField = Shapes.Rect(10, 20);
    HouseArea = Shapes.Rect(40, 10);

    ShapeList.append(FarmField);
    ShapeList.append(HouseArea);

    for Shape in ShapeList:
        print Shape.GetArea();