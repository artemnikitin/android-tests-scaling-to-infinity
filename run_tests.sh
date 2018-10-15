#!/usr/bin/env bash

cd /tool
./android_emulator_waiter.py -e my_emulator_name

cd /app
./gradlew clean testDebugUnitTest connectedAndroidTest
