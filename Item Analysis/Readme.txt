---Item Analysis---

This program produces TEX output from the Maths Competition Item Analysis Files.

For each grade, it combines the Individual and Pair item analysis files 
into a single table in a TEX file.

This program consists of the following files:
 ItemAnalysis.exe     - performs the conversion for a single grade
 ItemAnalysis.C       - C program which was compiled to produce ItemAnalysis.exe
 RunMe.bat            - calls ItemAnalysis.exe with the correct parameters for each grade.

You should use the program RunMe.bat

Input files: 
  Place the files INDGR8.ITM, PRGR8.ITM, ... INDGR12.ITM, PRGR12.ITM in the same
  directory as the program RunMe.bat and ItemAnalysis.exe.

Output files:
  The output will be placed in the files ALLGR8.ITM, ... ALLGR12.ITM

Alternatively you can edit the file RunMe.bat to change these default file names, 
but this is not recommended.

By Ian Webb, January 2001
Updated 2011

------------------
SAMPLE INPUT DATA:

"","","20010325","",1,"1",1,0,67,7,10,4,11,0,0,0,0,1.0000,"",0,0,1,0,0,57,54,47,45,20,2,4,5,6,7,0,2,3,6,23,0,2,3,3,6,7,4,7,8,9
"","","20010325","",2,"3",3,2,9,10,72,6,0,0,0,0,0,1.0000,"",0,0,0,2,5,0,4,2,6,19,0,2,6,13,13,66,58,53,38,22,0,2,5,8,6,0,0,0,1,0
"","","20010325","",3,"1",1,1,82,1,10,4,2,0,0,0,0,1.0000,"",0,0,0,2,2,65,54,59,52,42,0,2,0,0,1,1,5,4,10,14,0,5,3,2,3,0,0,0,2,3
...


--------------------------
CORRESPONDING OUTPUT DATA:

Question  &            & 1    & 2    & 3    & 4    & 5    & Abstain\cr
          &            &      &      &      &      &      &    \cr
\qquad  1 & Individual &[67]  &  7   & 10   &  4   & 11   &  0 \cr
          & Pairs      &[79]  &  6   &  6   &  5   &  4   &  0 \cr
          &            &      &      &      &      &      &    \cr
\qquad  2 & Individual &  9   & 10   &[72]  &  6   &  0   &  2 \cr
          & Pairs      &  8   &  9   &[75]  &  8   &  0   &  0 \cr
          &            &      &      &      &      &      &    \cr
\qquad  3 & Individual &[82]  &  1   & 10   &  4   &  2   &  1 \cr
          & Pairs      &[86]  &  0   &  7   &  5   &  2   &  0 \cr
          &            &      &      &      &      &      &    \cr
...
--------------------------