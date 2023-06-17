<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="media/qr-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="media/qr-light.png">
    <img alt="QR - Program to solve the QR Code Challenge" src="media/qr-dark.png">
  </picture>

  <br />

  ![GitHub repo size](https://img.shields.io/github/repo-size/lhbelfanti/qr?style=for-the-badge)
  ![License](https://img.shields.io/github/license/lhbelfanti/qr?style=for-the-badge)
</div>

---

# QR Code Challenge

## Problem

"We found a very strange image and we suspect it is a kind of code, but we couldn't break yet. Are you capable to solve it?"

<p align="center">
    <img width="400" alt="Step 1" src="./src/res/qr.png" />
</p>

## Solution

To solve this problem I figured out that I could crop the image in small squares and ensemble them like a jigsaw.

**To do so, I used the data structure: Tree.**

After obtaining the small squares the steps were the following:

### Step 1
Obtain the first line, knowing that a QR has 3 main squares.</br>
Each piece of the puzzle had a color square that matches exactly with at most 2 more

<img width="300" alt="Step 1" src="./media/steps/step_01.png" />

### Step 2
Get the following line to verify the algorithm was working correct

<img width="300" alt="Step 2" src="./media/steps/step_02.png" />

### Step 3
Continue testing the algorithm, while seeing if the QR was appearing on the screen

<img width="300" alt="Step 3" src="./media/steps/step_03.png" />

### Step 4
Complete the jigsaw part of the algorithm. And magically I saw a QR, but I needed to remove those red lines and the color squares.

<img width="300" alt="Step 4" src="./media/steps/step_04.png" />

### Step 5
Removing the red lines

<img width="300" alt="Step 5" src="./media/steps/step_05.png" />

### Step 6
Tried to remove the color squares without success

<img width="300" alt="Step 6" src="./media/steps/step_06.png" />

### Step 7
Lastly, I tried another approach and a clean QR was ready to scan! 

<img width="300" alt="Step 7" src="./media/steps/step_07.png" />

The QR is not working anymore but, after scanning it, a popup with a message appeared, and that was the code to solve the challenge.

## Installation

To run this program locally, download the repository and run the file [setup.sh](./setup.sh). This file will do the whole installation for you.