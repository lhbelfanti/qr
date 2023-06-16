# QR Code Challenge

## Problem

"We found a very strange image and we suspect it is a kind of code, but we couldn't break yet. Are you capable to solve it?"

<p align="center">
    <img width="400" alt="Step 1" src="./src/res/UGY0EKrw.png" />
</p>

## Solution

To solve this problem I figured out that I could crop the image in small squares and ensemble them like a jigsaw.

After obtaining the small squares the steps were the following:

### Step 1
Obtain the first line, knowing that a QR has 3 main squares.</br>
Each piece of the puzzle had a color square that matches exactly with at most 2 more

<img width="300" alt="Step 1" src="./src/res/final/01_final.png" />

### Step 2
Get the following line to verify the algorithm was working correct

<img width="300" alt="Step 2" src="./src/res/final/02_final.png" />

### Step 3
Continue testing the algorithm, while seeing if the QR was appearing on the screen

<img width="300" alt="Step 3" src="./src/res/final/03_final.png" />

### Step 4
Complete the jigsaw part of the algorithm. And magically I saw a QR, but I needed to remove those red lines and the color squares.

<img width="300" alt="Step 4" src="./src/res/final/04_final.png" />

### Step 5
First of all I removed the red lines and then tried to remove the color squares. Unfortunately the second part broke the QR

<img width="300" alt="Step 3" src="./src/res/final/05_final.png" />

### Step 6
Lastly, I tried another approach and a clean QR was ready to scan! 

The QR is not working anymore but, after scanning it, a popup with a message appeared, and that was the code to solve the challenge.

<img width="300" alt="Step 4" src="./src/res/final/06_final.png" />
