# fastsim (COMP 211 Checkoff 3: Python Libraries Implemented in C)

## Intro

I chose to explore the topic of implementing Python libraries in C. I chose this topic because I wanted to get exposure on the inner working of some of the most widely used libraries.

## What I Explored

I narrowed my topic to calling C from Python, and the general idea of a mixed implementation of code across the two languages. I wanted to see if it was possible to get the best of both worlds: the ease of Python and the efficieny of C. I created an experiment to test summing the elements of an array through two approaches: one purely in Python, and one where a Python program calls a C function from a shared library. I then checked and compared the speed of the two implementations.

## Discoveries

At first I thought that a Python program that calls C functions for calculation would be strictly faster than doing the calculations purely in Python. Through the experiment, I found that is not always the case. While the Python program calling a C function was around 30 times faster than a pure Python program when the array had 10,000 elements, it was half as fast as the pure program when the array had 10 elements. This showed me the overhead costs when using ctypes, how to compare algorithm performance, and that the context is important when thinking of having a Python program call C functions.

## How to Run

1. Clone repository from GitHub
2. Create and activate the virtual environment
3. Navigate to the project directory
4. Compile the C shared library
5. Run the benchmark program
6. Enter the number of elements that should be randomly generated for the test array when prompted
7. Wait for program to return, as it might take a few seconds

## Slides

[Slides (PDF)](docs/comp211-checkoff/Checkoff3-Slides.pdf)