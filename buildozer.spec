[app]
title = Battery Tracker
package.name = batterytracker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0
android.permissions = FOREGROUND_SERVICE, WAKE_LOCK
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a