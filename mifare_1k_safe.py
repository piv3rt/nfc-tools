import argparse

def protect(access_conditions):
    access_conditions |= 0x880080
    access_conditions &= 0xFF77F7
    return access_conditions

def main(args):
    with open(args.input, "rb") as f:
        data = f.read()

    if (file_size := len(data)) != 1024:
        raise Exception(f"Expected file size of 1024 but found {file_size}")

    with open(args.output, "wb") as f:
        for i in range(64):
            block = data[i*16:i*16+16]
            if (i + 1) % 4 == 0:
                access_conditions = int.from_bytes(block[6:9], byteorder="big")
                access_conditions = protect(access_conditions)
                access_conditions = access_conditions.to_bytes(3, byteorder="big")
                block = block[:6] + access_conditions + block[9:]
            f.write(block)

    print(f"Success! Wrote result to {args.output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edit MIFARE 1k access conditions to avoid locked keys")
    parser.add_argument("input", help="MIFARE dump to open")
    parser.add_argument("output", help="MIFARE dump to save")
    args = parser.parse_args()
    main(args)
