# frames

An array is given. The next argument is the length of the array and the last is the length of the frame.
Moving on the array (by the given third element - moving the frame), select the largest difference inside the frame between max and min value.

For example: 
    (array, length of array, step/length of the frame)
    ([2, -5, 8, 15, 2, 4], 6, 3)

    [2, -5, 8] -> max = 8, min = -5 -> difference(max - min) = 13
    [-5, 8, 15] -> max = 15, min = -5 -> difference = 20
    [8, 15, 2] -> max = 15, min = 2 -> diffrence = 13
    [15, 2, 4] -> max = 15, min = 2 -> diffrence = 13
    [2, 4] -> max = 4, min = 2 -> diffrence = 2
    [4] -> max = 4, min = 4 -> diffrence = 0

    result: 20