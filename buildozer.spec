[app]
title = Aditya Pro Player
package.name = adityapro
package.domain = org.aditya
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.1.0,kivymd,yt-dlp,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
