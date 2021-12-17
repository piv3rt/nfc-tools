import argparse

def main(args):

    data = []
    with open(args.file1, "rb") as f:
        data.append(f.read())

    with open(args.file2, "rb") as f:
        data.append(f.read())

    for i in range(2):
        if (file_size := len(data[i])) != 1024:
            raise Exception(f"Expected file size of 1024 but found {file_size} for file #{i+1}")

    print("+" + "-"*20 + " FILE 1 " + "-"*21 + "+" + "-"*8 + "+" + "-"*21 + " FILE 2 " + "-"*20 + "+")
    for i in range(64):
        line1 = line2 = ""
        for j in range(16):
            b1 = data[0][i*16+j]
            b2 = data[1][i*16+j]
            line1 += f"{b1:02x} " if b1 == b2 else f"\033[91m{b1:02x} \033[0m"
            line2 += f"{b2:02x} " if b1 == b2 else f"\033[91m{b2:02x} \033[0m"
        print(f"| {line1}| 0x{i*16:04x} | {line2}|")
        if (i + 1) % 4 == 0:
            print("+" + "-"*49 + "+" + "-"*8 + "+" + "-"*49 + "+")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare two MIFARE 1k dumps")
    parser.add_argument("file1", help="1st MIFARE dump")
    parser.add_argument("file2", help="2nd MIFARE dump")
    args = parser.parse_args()
    main(args)
