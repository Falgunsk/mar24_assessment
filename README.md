# mar24_assessment

Q1.Vohra went to a movie with his friends in a Wave theater and during break time he
bought pizzas, puffs and cool drinks. Consider the following prices :
Rs.100/pizza
Rs.20/puffs
Rs.10/cooldrink
Generate a bill for What Vohra has bought.
Input:
Enter the no of pizzas bought:10
Enter the no of puffs bought:12
Enter the no of cool drinks bought:5
Output :
Bill Details
No of pizzas:10
No of puffs:12
No of cooldrinks:5
Total price=1290
Q2. To calculate the total number of steps taken to climb a certain number of stairs.
The user is prompted to input the total number of stairs (m) and the number of stairs
covered in each step (n).
Example:-
Enter the number of stairs:13
Enter the number of steps:2
Total steps taken:7
Q3.You want to buy a particular stock at its lowest price. Science the stock market isunpredictable , you steal the price plans of a company for this stock for the next N
days.Find the best price you can get to buy this stock to achieve maximum profit.
Note:-The initial price of the stock is 0.
Input Specification
Input:- N_number of days
Input:- Array representing change in stock price for the day
Output Specification
Your function must return the best price to buy the stock at.
Example:-
Input 1: 5
Input 2: -39957,-17136,35466,21820,-26711
Output:- -80794
Q4.There are a total n number of Monkeys sitting on the branches of a huge Tree. As
travelers offer Bananas and Peanuts, the Monkeys jump down the Tree. If every Monkey
can eat k Bananas and j Peanuts. If the total m number of Bananas and p number of
Peanuts are offered by travelers, calculate how many Monkeys remain on the Tree after
some of them jumped down to eat.
At a time one Monkey gets down and finishes eating and go to the other side of the
road. The Monkey who climbed down does not climb up again after eating until the otherMonkeys finish eating.
Monkeys can either eat k Bananas or j Peanuts. If for last Monkey there are less than
k Bananas left on the ground or less than j Peanuts left on the ground, only that
Monkey can eat Bananas(<k) along with the Peanuts(<j).
Write code to take inputs as n, m, p, k, j and return the number of Monkeys left on
the Tree.
Where, n= Total no of Monkeys
k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last
may get less than k Bananas)
j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last
may get less than j Peanuts)
m = Total number of Bananas
p = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility
of k and j having a value zero
Input:
Input Values
20
2
3
12
12
Output:
Number of Monkeys left on the tree:10
Note: Kindly follow the order of inputs as n,k,j,m,p as given in the above example.
And output must include the same format as in above example(Number of Monkeys left
on the Tree:)
For any wrong input display INVALID INPUT
Q5. Selection of MPCS exams include a fitness test which is conducted on ground. Therewill be a batch of 3 trainees, appearing for running test in track for 3 rounds. You
need to record their oxygen level after every round. After trainee are finished with
all rounds, calculate for each trainee his average oxygen level over the 3 rounds and
select one with highest oxygen level as the most fit trainee. If more than one traineeattains the same highest average level, they all need to be selected.Display the most
fit trainee (or trainees) and the highest average oxygen level.
Note:
The oxygen value entered should not be accepted if it is not in the range between 1
and 100.
If the calculated maximum average oxygen value of trainees is below 70 then declare
the trainees as unfit with meaningful message as “All trainees are unfit.
Average Oxygen Values should be rounded.
Example 1:
INPUT VALUES
95
92
95
92
90
92
90
92
90
OUTPUT VALUES
Trainee Number : 1
Trainee Number : 3
Note:
Input should be 9 integer values representing oxygen levels entered in order as
Round 1
Oxygen value of trainee 1
Oxygen value of trainee 2
Oxygen value of trainee 3
Round 2
Oxygen value of trainee 1
Oxygen value of trainee 2
Oxygen value of trainee 3
Round 3
Oxygen value of trainee 1
Oxygen value of trainee 2
Oxygen value of trainee 3
Q6. You are tasked with a complex matrix operation. You will need to input the size ofthe matrix and then provide the element of the matrix
The main matrix must then be divided into two submatrices: one for even-indexed
elements and the other for odd-indexed elements
Following this,you are required to sort both the even and odd matrices in ascending
order
Finally , you must calculate and print the sum of the second largest numbers from bothmatrices.
Example:-
Enter the size of the array:-5
Enter the element at the 0th index:3
Enter the element at the 1st index:4
Enter the element at the 2nd index:1
Enter the element at the 3rd index:7
Enter the element at the 4th index:9
After sorting:
Sorted even array: 1 3 9
Sorted odd array: 4 7
The sum of the second largest numbers from both matrices is:7
Q7.Given a value N, if we want to make change for N Rupees, and we have infinite
supply of each Coin C = {C1, C2, …., Cm} valued coins. In how many ways can we make
the change? The order of coins doesn't matter.
Example 1:
Let total sum be N = 5 and the types of coins C = {1, 2}
For the given values, the possible changes must be arranged keep in mind that the sum
of the change must be 5.
{1, 1, 1, 1, 1}
{1, 1, 1, 2}
{1, 2, 2}
We can generate 3 such ways where the rupees can be rearranged to give the sum of 5.
Hence, the output must be 3.
Example 2:
Let N = 4 and C = {1, 2, 3}
For the given values, the possible changes must be arranged keeping in mind that the
sum of the change must be 5.
{1, 1, 1, 1}
{1, 1, 2}
{2, 2}
{1, 3}
We can generate 4 such ways where the rupees can be rearranged to give the sum of 5.
Hence, the output must be 4.
Q8. Given a sequence of numbers. Find all leaders in the sequence. An element is
called a leader if it is strictly greater than all elements to its right side.
Input
arr[] = {23, 22, 24,8 9, 10}
Output
10, 24
Q9.Given two strings. Check whether both the strings are anagrams of each other or not.[Anagram strings are those strings that have the same characters, only the order of
characters may be different ]
Input
str1 = 'coding', str2 = 'ingodc'
str1 = 'hello' , str2 = 'hoeli'
Output
"Yes"
"No"
Q10.Jarvis is weak in computing palindromes for Alphanumeric characters. While Ironmanis busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in
computing palindromes. You are given a string S containing alphanumeric characters.
Find out whether the string is a palindrome or not. If you are unable to solve it thenit may result in the death of Iron Man.
Test Case 1:-
Input:
S = “I am :IronnorI Ma, i”
Output:
YES
Explanation:
Ignore all the symbols and whitespaces S = “IamIronnorIMai”. Now, Check for
palindrome ignoring uppercase and lowercase English letter.
Test Case 2:-
Input:
S = Ab?/Ba
Output:
YES
Explanation:
Here with any amount of rotation s2 can’t be obtained by s1.
Your Task:
This is a function problem. The input is already taken care of by the driver code. Youonly need to complete the function saveIronman() that takes an string (ch), and returnthe true if the string is a palindrome and false if the string is not a palindrome.
The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Space Complexity: O(1).
Note: N = |s1|.
Constraints:
1 ≤ |S| ≤ 100000
Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and
whitespaces.
Explanation:
Ignore all the symbols and whitespaces S = “IamIronnorIMai”. Now, Check for
palindrome ignoring uppercase and lowercase English letter.
Test Case 2:-
Input:
S = Ab?/Ba
Output:
YES
Explanation:
Here with any amount of rotation s2 can’t be obtained by s1.
Your Task:
This is a function problem. The input is already taken care of by the driver code. Youonly need to complete the function saveIronman() that takes an string (ch), and returnthe true if the string is a palindrome and false if the string is not a palindrome.
The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Space Complexity: O(1).
Note: N = |s1|.
Constraints:
1 ≤ |S| ≤ 100000
Note: Consider alphabets and numbers only for palindrome check. Ignore symbols and
whitespaces.
