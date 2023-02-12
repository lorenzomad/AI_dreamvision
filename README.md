# AI_dreamvision
Application that uses Craiyon APIs to generate dreams starting from a prompt. 
The user will be able to use the app as a dream journal where they can log their dreams, and n image for the dream is automatically generated.

The objective is to create an app that will run on android and iOS.

The app is built in python using Kivy. 

# Architecture

The application is based on a frontend and a backend.

## frontend
the frontend consists in two pages that run through KivyMD (material design version of kivy) and have access to functions implemented in python in the backend:

- dream generation: the main page where the user can describe and generate a dream.
- dream gallery: where the user has access to the library of past dreams and can visualize them or delete them.

## backend

The backend implements the functions to:
- generate the dream through calls to the Craiyon APIs, provided by the Craiyon.py project
- save the dream to the SQL DB
- save the images to memory

# Screenshots

Dream generation page:

<img width="244" alt="image_1" src="https://user-images.githubusercontent.com/106270843/217652624-511dcfb3-cad5-4211-88c8-ce23bcf8e5df.png">


Dream gallery:

<img width="248" alt="image_2" src="https://user-images.githubusercontent.com/106270843/217652653-e1a21d3a-08cc-4b22-bf30-beea8f13c9f8.png">


The project has continous integration and building for pushes on the main branch: 
Continuous testing and automated building of the apk file with buildozer for kivy
[![Build](https://github.com/lorenzomad/AI_dreamvision/actions/workflows/main.yml/badge.svg)](https://github.com/lorenzomad/AI_dreamvision/actions/workflows/main.yml)


# Debug functions
'''adb logcat *:S python:D