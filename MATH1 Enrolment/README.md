MATH1 Enrolment
Problem Code:
M1ENROL
Contest Code:
START46

Problem
For the upcoming semester, the admins of your university decided to keep a total of XX seats for the MATH-1 course. A student interest survey was conducted by the admins and it was found that YY students were interested in taking up the MATH-1 course.

Find the minimum number of extra seats that the admins need to add into the MATH-1 course to make sure that every student who is interested in taking the course would be able to do so.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of two-space separated integers on a single line, XX and YY — the current number of seats up for enrolment and the number of students interested in taking up the course in the upcoming semester, respectively.
Output Format
For each test case, output on a new line the minimum number of seats required to be added.

Constraints
1 \leq T \leq 1001≤T≤100
1 \leq X, Y \leq 10^51≤X,Y≤10 
5
 
Sample 1:
Input
Output
4
1 1
12 34
50 49
49 50
0
22
0
1
Explanation:
Test case 11: Exactly 11 seat is available for enrolment, and exactly 11 student is interested in taking up the course, hence addition of more seats is not required.

Test case 22: 1212 seats are available for enrolment but 3434 students are interested in taking up the course, hence the admins would have to add 34-12=2234−12=22 more seats to make sure that every student interested in the course gets a seat.

Test case 33: 5050 seats are available for enrolment and 4949 students are interested in taking up the course, hence addition of more seats is not required.

Test case 44: 4949 seats are available for enrolment, but 5050 students are interested in taking up the course, hence the admins would have to add 50-49=150−49=1 more seat to make sure that every student interested in the course gets a seat.
