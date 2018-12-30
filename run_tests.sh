#!/usr/bin/env bash

cd /tool
./android_emulator_waiter.py -e android-emulator

cd /app
./gradlew clean testDebugUnitTest connectedAndroidTest
