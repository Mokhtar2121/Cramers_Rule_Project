# Definition 

Cramer’s rule is a definite formula used for a system of
linear equations with number of equations equal to number of unknowns.
This formula is valid only when the system has unique solution.
 
Let Ax = b,
where A is a n×n matrix that has non-zero determinant, and x is the column
vector of unknown variables. Let C be the same matrix as A, but the i-th
column in A is replaced by the column b for all i = 1,2,..n. The rule states
that: x<sub>i</sub> = det(C<sub>i</sub>)
/det(A) , where i = 1,2,3,..n.

# Implementation

*  Requesting the number of varibles from the user.
*  Creating the 2D matrix and an array to save the valuse of the equations.
*  Getting the data from the user and saving it in the data structures.
*  Getting the determinant of the original matrix.
*  Calculating the value of each x<sub>i</sub> following the rule we methioned above after sloving for  det(C<sub>i</sub>).

