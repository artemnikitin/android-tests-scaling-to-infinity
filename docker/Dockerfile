# MAINTAINER hi@artemnikitin.com

FROM ubuntu:16.04

ENV ANDROID_HOME /android-sdk
ENV PATH $PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools

# Android license hashes
ENV LICENSE_HASH 8933bad161af4178b1185d1a37fbf41ea5269c55
ENV PREVIEW_LICENSE_HASH 84831b9409646a918e30573bab4c9c91346d8abd
ENV EXTRA_LICENSE_HASH d975f751698a77b662f1254ddbeed3901e976f5a

# Basic setup with JDK
RUN apt-get update && apt-get --no-install-recommends -y install \
    wget \
    unzip \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    default-jdk \
    python \
    && apt-get clean && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Setup Android SDK 
RUN mkdir -p $ANDROID_HOME && mkdir -p $ANDROID_HOME/licenses/ \
    && echo $LICENSE_HASH >> $ANDROID_HOME/licenses/android-sdk-license \
    && echo $PREVIEW_LICENSE_HASH >> $ANDROID_HOME/licenses/android-sdk-preview-license \
    && echo $EXTRA_LICENSE_HASH >> $ANDROID_HOME/licenses/intel-android-extra-license \
    && wget --quiet --output-document=android-sdk.zip https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip \
    && unzip -qq android-sdk.zip -d $ANDROID_HOME \
    && rm android-sdk.zip \
    && (echo y; echo y; echo y; echo y; echo y; echo y) | sdkmanager --licenses
