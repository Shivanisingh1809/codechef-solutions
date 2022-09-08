Pass the Exam
Problem Code:
PASSTHEEXAM
Contest Code:
JULY221

Problem
Chef appeared for an exam consisting of 33 sections. Each section is worth 100100 marks.

Chef scored AA marks in Section 11, BB marks in section 22, and CC marks in section 33.

Chef passes the exam if both of the following conditions satisfy:

Total score of Chef is \geq 100≥100;
Score of each section \geq 10≥10.
Determine whether Chef passes the exam or not.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a single line containing 33 space-separated numbers A, B, CA,B,C - Chef's score in each of the sections.
Output Format
For each test case, output PASS if Chef passes the exam, FAIL otherwise.

Note that the output is case-insensitive i.e. PASS, Pass, pAsS, and pass are all considered same.

Constraints
1 \leq T \leq 10001≤T≤1000
0 \leq A, B, C \leq 1000≤A,B,C≤100
Sample 1:
Input
Output
5
9 100 100
30 40 50
30 20 40
0 98 8
90 80 80
FAIL
PASS
FAIL
FAIL
PASS
Explanation:
Test Case 11: Although Chef's total score is 209 \geq 100209≥100, still Chef fails the exam since his score in section 11 is \lt 10<10.

Test Case 22: Chef cleared each section's cutoff as well his total score = 120 \geq 100=120≥100.

Test Case 33: Although Chef cleared each section's cutoff but his total score is 90 \lt 10090<100. So he fails the exam.

Test Case 44: Although Chef's total score is 106 \geq 100106≥100, still Chef fails the exam since his score in section 11 is \lt 10<10.

Test Case 55: Chef cleared each section's cutoff as well his total score = 250 \geq 100=250≥100.

