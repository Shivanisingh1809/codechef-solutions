Age Limit
Problem Code:
AGELIMIT
Contest Code:
START42


Problem
Chef wants to appear in a competitive exam. To take the exam, there are following requirements:

Minimum age limit is XX (i.e. Age should be greater than or equal to XX).
Age should be strictly less than YY.
Chef's current Age is AA. Find whether he is currently eligible to take the exam or not.

Input Format
First line will contain TT, number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three integers X, Y,X,Y, and AA as mentioned in the statement.
Output Format
For each test case, output YES if Chef is eligible to give the exam, NO otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

Constraints
1 \leq T \leq 10001≤T≤1000
20 \leq X \lt Y \leq 4020≤X<Y≤40
10 \leq A \leq 5010≤A≤50
Sample 1:
Input
Output
5
21 34 30
25 31 31
22 29 25
20 40 15
28 29 28
YES
NO
YES
NO
YES
Explanation:
Test case 11: The age of Chef is 3030. His age satisfies the minimum age limit as 30 \ge 2130≥21. Also, it is less than the upper limit as 30 \lt 3430<34. Thus, Chef is eligible to take the exam.

Test case 22: The age of Chef is 3131. His age satisfies the minimum age limit as 31 \ge 2531≥25. But, it is not less than the upper limit as 31 \nless 3131≮31. Thus, Chef is not eligible to take the exam.

Test case 33: The age of Chef is 2525. His age satisfies the minimum age limit as 25 \ge 2225≥22. Also, it is less than the upper limit as 25 \lt 2925<29. Thus, Chef is eligible to take the exam.

Test case 44: The age of Chef is 1515. His age does not satisfy the minimum age limit as 15 \lt 2015<20. Thus, Chef is not eligible to take the exam.
