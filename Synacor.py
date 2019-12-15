import sys
f = open("challenge.bin", 'rb')
# x = f.read(2)
# print ord(x)
# x = f.read(2)
# print ord(x)
# x = f.read(2)
# print ord(x)
# x = f.read(2)
# print ord(x)
# x = f.read(2)
# print ord(x)
stack = []
registers = [0,0,0,0,0,0,0,0]
loc = 0
while True:
    low = ord(f.read(1))
    high = ord(f.read(1))
    f.seek(loc, 0)
    loc += 2
    if high != 0:
        sys.stdout.write("unimplemented")
        sys.stdout.write(str(low) + " "+ str(high) + "\n")
        sys.stdout.flush()
        break
    else:
        if low == 0:
            sys.stdout.write("finished\n")
            sys.stdout.flush()
            break
        elif low == 19:
            low = ord(f.read(1))
            high = ord(f.read(1))
            loc += 2
            if high != 0:
                sys.stdout.write("unimplemented print at")
                sys.stdout.write(str(low) + " "+ str(high) + "\n")
                sys.stdout.flush()
                break
            else:
                sys.stdout.write(chr(low))
                sys.stdout.flush()
        elif low == 21:
            continue
        else:
            sys.stdout.write("unimplemented")
            sys.stdout.write(str(low) + " "+ str(high) + "\n")
            sys.stdout.flush()
            break