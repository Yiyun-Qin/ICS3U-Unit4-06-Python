#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, showing rgb from 0-255


def main():
    # This function shows numbers from 0-255

    # process
    for counter_r in range(256):
        for counter_g in range(256):
            for counter_b in range(256):
                print("({0}, {1}, {2})".format(counter_r, counter_g, counter_b))
    print("\nDone.")


if __name__ == "__main__":
    main()
