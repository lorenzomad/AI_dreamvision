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


Dream gallery:


The project has continous integration and building for pushes on the main branch: 
Continuous testing and automated building of the apk file with buildozer for kivy
[![Build](https://github.com/lorenzomad/AI_dreamvision/actions/workflows/main.yml/badge.svg)](https://github.com/lorenzomad/AI_dreamvision/actions/workflows/main.yml)
