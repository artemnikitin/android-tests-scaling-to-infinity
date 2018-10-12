#!/usr/bin/env python

from __future__ import print_function

import argparse
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--emulator", type=str, default="", help="Provide name for Android emulator")
    args = parser.parse_args()

    if args.emulator == "":
        print("Please, provide a name for an emulator!")
        exit(1)

    string_to_wait_for = "{}:5555	device".format(args.emulator)
    print("Waiting for: {}".format(string_to_wait_for))

    counter = 0
    devices_list = execute("adb devices")
    while string_to_wait_for not in devices_list:
        time.sleep(10)
        execute("adb kill-server")
        execute("adb connect {}:5555".format(args.emulator))
        devices_list = execute("adb devices")
        counter += 1
        if counter == 30:
            print("Can not connect to an emulator! Exiting...")
            exit(-1)
    print(execute("adb devices"))


def execute(cmd):
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


if __name__ == "__main__":
    main()
