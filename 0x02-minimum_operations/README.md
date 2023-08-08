## Minimun Operations 

### Task
- In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.


### Example
- n = 9
- H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH
- Number of operations: 6

### Algorithm
- If n is less than or equal to 1, return 0.
- set a variable to store the number of operations
- set a variable to store the number of characters
- set a variable to store the copied characters
- loop while the number of characters is less than n
- if n is divisible by the number of characters, copy all characters to clip, and paste by adding the clipped number of characters to the number of characters and increment the number of operations by 2 for copy and paste
- else, paste by adding the number of clipped characters to the number of characters and increment the number of operations by 1 for paste
