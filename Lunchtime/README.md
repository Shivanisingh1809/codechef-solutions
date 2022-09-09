Lunchtime
Problem Code:
LTIME
Contest Code:
LTIME107



Problem
Chef has his lunch only between 11 pm and 44 pm (both inclusive).

Given that the current time is XX pm, find out whether it is lunchtime for Chef.

Input Format
The first line of input will contain a single integer TT, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, containing one integer XX.
Output Format
For each test case, print in a single line \texttt{YES}YES if it is lunchtime for Chef. Otherwise, print \texttt{NO}NO.

You may print each character of the string in either uppercase or lowercase (for example, the strings \texttt{YeS}YeS, \texttt{yEs}yEs, \texttt{yes}yes and \texttt{YES}YES will all be treated as identical).

Constraints
1 \leq T \leq 121≤T≤12
1 \leq X \leq 121≤X≤12
Sample 1:
Input
Output
3
1
7
3
YES
NO
YES
Explanation:
Test case 11: Lunchtime is between 11 pm and 44 pm (both inclusive). Since 11 pm lies within lunchtime, the answer is \texttt{YES}YES.

Test case 22: Lunchtime is between 11 pm and 44 pm (both inclusive). Since 77 pm lies outside lunchtime, the answer is \texttt{NO}NO.

Test case 33: Lunchtime is between 11 pm and 44 pm (both inclusive). Since 33 pm lies within lunchtime, the answer is \texttt{YES}YES.
