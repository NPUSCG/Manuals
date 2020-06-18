import sys

origin = r"font-family: 'JetBrains Mono';"
substitution = r"font-family: SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;"


def main():
    argv = sys.argv[1:]
    for item in argv:
        text_data = []
        with open(item, 'r', encoding="utf-8") as fin:
            text_data = fin.readlines()
        text_data = [_.rstrip() for _ in text_data]
        text_data = [_ for _ in text_data if len(_) > 0]
        with open(item, 'w', encoding="utf-8") as fout:
            for line in text_data:
                line = line.replace(origin, substitution)
                print(line, file=fout)
            print(file=fout)
        print("{} done.".format(item))


if __name__ == "__main__":
    main()