from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here.
    count = 0
    while x > 0:
        count += x & 1
        x >>= 1

    return count


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
