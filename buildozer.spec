[app]
title = My Android Game
package.name = mypygamegame
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0
orientation = portrait
fullscreen = 1

# Icon configuration
icon.filename = icon.png

# Crucial Pygame requirements
requirements = python3,pygame,sdl2_ttf,sdl2_image,sdl2_mixer

# Android specific profiles
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
