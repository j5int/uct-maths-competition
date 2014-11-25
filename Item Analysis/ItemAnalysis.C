/* ITEM ANALYSIS-TO-TEX CONVERTOR FOR MATHS COMPETITION */

#include <stdio.h>
#include <stdlib.h>

#define INDIVIDUALS_FILE_NAME argv[1]
#define PAIRS_FILE_NAME argv[2]

int QUIT_WITH_MSG(char *error_message, char *param1, char *param2) { fprintf(stderr,"%s %s %s\n", error_message, param1, param2); exit(1);}

int main(int argc, char *argv[])
{
  FILE *individuals_file,
       *pairs_file,
       *output_file;

  int i, grade, question, correct_answer, dummy_var, dum,
    ind_answer[6],
    pair_answer[6];

  char dums[100];

  /* ----------------------------------------------------------
   * Open the input files
   * ---------------------------------------------------------- */

  if (argc != 3)
  {
    QUIT_WITH_MSG("Usage: itemanal <ind_file>.itm <pr_file>.itm > <output>.tex", "", "");
  }

  individuals_file = fopen(INDIVIDUALS_FILE_NAME, "r");

  if(individuals_file==NULL)
  {
    QUIT_WITH_MSG("The individuals input file didn't open:", INDIVIDUALS_FILE_NAME, "");
  }

  pairs_file = fopen(PAIRS_FILE_NAME, "r");

  if(pairs_file==NULL)
  {
    fclose(individuals_file);
    QUIT_WITH_MSG("The pairs input file didn't open:", PAIRS_FILE_NAME, "");
  }

  printf("Question  &            & 1    & 2    & 3    & 4    & 5    & Abstain\\cr\n");
  printf("          &            &      &      &      &      &      &    \\cr\n");

  /* ----------------------------------------------------------
   * Process the questions in sequence
   * ---------------------------------------------------------- */

  for(question = 1; question<=30; question++)
  {

    /* Ignore the first 26 or 27 places on each row: */

    if(question < 10)
    {
      for(i=0; i<26; i++)
      {
	fgetc(individuals_file);
	fgetc(pairs_file);
      }
    }
    else
    {
      for(i=0; i<27; i++)
      {
	fgetc(individuals_file);
	fgetc(pairs_file);
      }
    }

    /* Read the individual and pair responses to this question: */

    fscanf(individuals_file,
      "%d,%d,%d,%d,%d,%d,%d,%s\n",
      &correct_answer,
      &(ind_answer[0]),
      &(ind_answer[1]),
      &(ind_answer[2]),
      &(ind_answer[3]),
      &(ind_answer[4]),
      &(ind_answer[5]),
      dums);

    fscanf(pairs_file,
      "%d,%ld,%d,%d,%d,%d,%d,%s\n",
      &dum,
      &(pair_answer[0]),
      &(pair_answer[1]),
      &(pair_answer[2]),
      &(pair_answer[3]),
      &(pair_answer[4]),
      &(pair_answer[5]),
      dums);


    /* -----------------------------------------------------------
     * Print the TEX output to this question.
     * The first line is for individuals and the next for pairs:
     * ----------------------------------------------------------- */

    /* Individuals: */

    printf("\\qquad %2d & Individual ", question);

    for(i=1; i<=5; i++)
    {
      if(i == correct_answer)
	printf("&[%2d]  ", ind_answer[i]);
      else
	printf("& %2d   ", ind_answer[i]);
    }

    printf("& %2d \\cr\n",ind_answer[0]);

    /* Pairs: */

    printf("          & Pairs      ");

    for(i=1; i<=5; i++)
    {
      if(i == correct_answer)
	printf("&[%2d]  ", pair_answer[i]);
      else
	printf("& %2d   ", pair_answer[i]);
    }
    printf("& %2d \\cr\n",pair_answer[0]);

    printf("          &            &      &      &      &      &      &    \\cr\n");
  }

  fclose(individuals_file);
  fclose(pairs_file);
  QUIT_WITH_MSG("Successfully created TEX output from files:",
    INDIVIDUALS_FILE_NAME, PAIRS_FILE_NAME );

}


/* -----------------------------------------------------
 * SAMPLE INPUT DATA:

"","","20010325","",1,"1",1,0,67,7,10,4,11,0,0,0,0,1.0000,"",0,0,1,0,0,57,54,47,45,20,2,4,5,6,7,0,2,3,6,23,0,2,3,3,6,7,4,7,8,9
"","","20010325","",2,"3",3,2,9,10,72,6,0,0,0,0,0,1.0000,"",0,0,0,2,5,0,4,2,6,19,0,2,6,13,13,66,58,53,38,22,0,2,5,8,6,0,0,0,1,0
"","","20010325","",3,"1",1,1,82,1,10,4,2,0,0,0,0,1.0000,"",0,0,0,2,2,65,54,59,52,42,0,2,0,0,1,1,5,4,10,14,0,5,3,2,3,0,0,0,2,3
...

*/

/* -----------------------------------------------------
 * CORRESPONDING OUTPUT DATA:

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
--------------------------------------------------------- */
