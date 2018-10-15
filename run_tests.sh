#!/usr/bin/env bash

./tool/android_emulator_waiter.py -e my_emulator_name

./app/gradlew clean testDebugUnitTest connectedAndroidTest
