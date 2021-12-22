import argparse

def hex(value):
    return int(value, 16)

def ignored(offset):
    # UUID
    if offset < 0x10:
        return True
    # Keys, access conditions
    if offset % 64 > 0x2F:
        return True
    return False

def main(args):
    with open(args.input, "rb") as f:
        data = f.read()

    if (file_size := len(data)) != 1024:
        raise Exception(f"Expected file size of 1024 but found {file_size}")

    with open(args.output, "wb") as f:
        for i in range(0x400):
            if i < args.start or i > args.end or ignored(i):
                f.write(data[i].to_bytes(1, byteorder="big"))
            else:
                f.write(args.byte.to_bytes(1, byteorder="big"))

    print(f"Success! Wrote result to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace MIFARE sectors with arbitrary data")
    parser.add_argument("-s", "--start", type=hex, default=0x10, help="Start address (hex)")
    parser.add_argument("-e", "--end", type=hex, default=0x3EF, help="End address (hex)")
    parser.add_argument("-b", "--byte", type=hex, default=0x00, help="Byte to write (hex)")
    parser.add_argument("input", help="MIFARE dump to open")
    parser.add_argument("output", help="MIFARE dump to save")
    args = parser.parse_args()
    main(args)
