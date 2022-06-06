import sys


def main():
    with open('in.txt', 'r') as in_file:
        in_file = [x.strip() if 'Mozilla/' not in x
                   else x[:x.index('Mozilla/') - 1].strip()
                   for x in in_file.readlines()]

    in_file = [tuple(x.split('- -')) for x in in_file]
    in_file = sorted(in_file, key=lambda x: x[0])
    in_file = ['-'.join(x) for x in in_file]
    in_file = [x.replace(' -0700]', ']') for x in in_file]
    [print(x) for x in in_file]


if __name__ == '__main__':
    sys.exit(main())
