# Sign-Language
A project using OpenCV and Mediapipe, that detects exact matrix positions of hands and uses known database of movements to interpret the tracked positions of hands into words. Converts sign into understandable language.

Main Library Used:
Mediapipe- Accurate and reliable
             Built-in detection / Already made code and no need for training
             Code is easy enough to understand with help of AI such as GPT or DeepSeek
             It is an open source documentation, and enough sample codes and tutorials available to modify code to suit my purpose

I put the main idea into works n made note of different libraries I would need to install for use. I made use of ChatGPT to help me with this, and then checked with DeepSeek.
I learnt about MediaPipe, a ML based library by google, which provides ready-made models of code for real-time detection of body parts such as face and hands. The code helps track movements of said body part without me needing to train it to do so. As this is a project based on Sign Language, I made use of the feature tracking hands appearing in a webcam using 21 points (called landmarks) through each hand and storing x,y,z coordinates.

Looked around for different Mediapipe codes, and researched a bit as to how I can change it....Made note of code variations and referred to codes by other programmers on GitHUb to see how I could modify the code to suit my purpose of detecting hand gestures through a webcam.
In short, I followed references, understood them, and modified the logic.

The file SignLangDemo1.mp4 depicts my final trial of the inital code, however it uses only one hand. This was done for simplicity, and I later extended the system to support multi-hand tracking by updating MediaPipe parameters and adding iterations. (While alphabets in sign language can be conveyed using a single hand, both hands are often required to hold complete conversations)


I started with a simple procedural version, then refactored it into a class once I understood the pipeline.

