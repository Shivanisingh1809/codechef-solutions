Interior Design
Problem Code:
INTRDSGN
Contest Code:
LTIME110


Problem
Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.

For the first style, tiling the floor will cost X_1X 
1
​
  rupees and painting the walls will cost Y_1Y 
1
​
  rupees.

For the second style, tiling the floor will cost X_2X 
2
​
  rupees and painting the walls will cost Y_2Y 
2
​
  rupees.

Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line of input, containing 44 space-separated integers X_1, Y_1, X_2, Y_2X 
1
​
 ,Y 
1
​
 ,X 
2
​
 ,Y 
2
​
  as described in the statement.
Output Format
For each test case, output on a new line the amount Chef will pay for interior design.

Constraints
1 \leq T \leq 1001≤T≤100
1 \leq X_1, Y_1, X_2, Y_2 \leq 1001≤X 
1
​
 ,Y 
1
​
 ,X 
2
​
 ,Y 
2
​
 ≤100
Sample 1:
Input
Output
4
10 20 9 25
10 20 9 20
10 20 20 10
100 43 85 61
30
29
30
143
Explanation:
Test case 11: The first style costs 10 + 20 = 3010+20=30 rupees, and the second costs 9 + 25 = 349+25=34 rupees. The first is cheaper, so Chef will pay 3030 rupees.

Test case 22: The first style costs 10 + 20 = 3010+20=30 rupees, and the second costs 9 + 20 = 299+20=29 rupees. The second is cheaper, so Chef will pay 2929 rupees.

Test case 33: The first style costs 10 + 20 = 3010+20=30 rupees, and the second costs 20 + 10 = 3020+10=30 rupees. Both styles cost the same, so Chef is always going to pay 3030 rupees.

Test case 44: The first style costs 100 + 43 = 143100+43=143 rupees, and the second costs 85 + 61 = 14685+61=146 rupees. The first is cheaper, so Chef will pay 143143 rupees.
