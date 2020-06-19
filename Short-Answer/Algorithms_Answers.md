#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Runtime is O(n) because while the loop is n cubed, the iterator, a, is being iterated by n squared each time, which leaves a runtime of just n.


b) Runtime is O(n * n/2), which simplifies to O(n^2). There are two loops with one being nested inside the other, which means for each outer loop, there is still O(n/2) runtime for the inside loop, giving O(n^2). Also, j is being iterated twice as fast as i, but that does not change the overall runtime.


c) This recursive function is being recursively called n times, which means a linear O(n) runtime. If you have an initial bunnies = 5, that means bunnyEars function will be called 5 times, so O(n) time.

## Exercise II

1. choose middle floor of n-story building
2.     drop egg
3.     if egg breaks, middle floor is too high
4.         move to middle floor between bottom and prev middle, go back to step 2
5.     if egg doesn't break,
6.         check floor above, if it breaks, this is f
7.         else, move middle floor between prev middle and top, go back to step 2

This runtime complexity would be O(logn) because each time the loop occurs the number of floors that need to be checked are eliminated in half.