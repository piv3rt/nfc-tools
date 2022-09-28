import argparse

def main(args):
    with open(args.input, "rb") as f:
        data = f.read()

    if (file_size := len(data)) != 1024:
        raise Exception(f"Expected file size of 1024 but found {file_size}")

    with open(args.output, "wb") as f:
        for i in range(64):
            block = bytearray(data[i*16:i*16+16])
            # If sector trailer
            if i % 4 == 3:
                block[6] |= 0x08
                block[7] &= 0x77
                block[8] |= 0x80
                if args.key == "A":
                    block[6] |= 0x80
                    block[8] &= 0xF7
                if args.key == "B":
                    block[6] &= 0x7F
                    block[8] |= 0x08
            f.write(block)

    print(f"Success! Wrote result to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edit MIFARE 1k sector trailer to avoid locking access bits forever.")
    parser.add_argument("input", help="MIFARE dump to open")
    parser.add_argument("output", help="MIFARE dump to save")
    parser.add_argument("-k", "--key", type=str.upper, choices=["A", "B"], default=False, help="Force A or B key for sector trailer write access")
    args = parser.parse_args()
    main(args)
