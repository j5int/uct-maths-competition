"""
Utility to import CSV format Item Analysis files of statistics on the multiple choice
questions in the competition, and output a summary table in TeX format
"""
import sys
import unicodecsv


class MultipleChoiceStats:
    # indexed from 0 to 29

    def __init__(self, filename):
        self.questions = dict()
        with open(filename, 'rb') as csv_file:
            csv_reader = unicodecsv.reader(csv_file)
            q = 1
            for row in csv_reader:
                self.questions[q] = {
                    'correct': row[6],
                    'abstain': row[7],
                    'choice1': row[8],
                    'choice2': row[9],
                    'choice3': row[10],
                    'choice4': row[11],
                    'choice5': row[12]}
                q += 1

def print_header():
    print "Question   &            &  1   &  2   &  3   &  4   &  5   & Abstain\\cr"
    print "           &            &      &      &      &      &      &        \\cr"


def print_question_output(question, individual_stats, pair_stats):
    """
    Print the TEX output to this question. The first line is for individuals and the next for pairs:
    """
    iq = individual_stats.questions[question]
    print '\\qquad %2d & Individuals' % question,
    for c in range(1, 6):
        if c == int(iq['correct']):
            print '&[%2s] ' % iq['choice%s' % c],
        else:
            print '& %2s  ' % iq['choice%s' % c],
    print '& %2s     \\cr' % iq['abstain']

    pq = pair_stats.questions[question]
    print '          & Pairs      ',
    for c in range(1, 6):
        if c == int(pq['correct']):
            print '&[%2s] ' % pq['choice%s' % c],
        else:
            print '& %2s  ' % pq['choice%s' % c],
    print '& %2s     \\cr' % pq['abstain']

    print '          &             &      &      &      &      &      &        \\cr'


def main():
    if len(sys.argv) < 3:
        print "Usage: python ItemAnalysis <individuals file> <pairs file>"
        exit()
    individual_stats = MultipleChoiceStats(sys.argv[1])
    pair_stats = MultipleChoiceStats(sys.argv[2])

    print_header()

    for question in range(1, 31):
        print_question_output(question, individual_stats, pair_stats)


if __name__ == "__main__":
    main()


"""
-----------------------------------------------------
SAMPLE INPUT DATA (individuals only - a similar file is supplied for the pairs):

"","","20010325","",1,"1",1,0,67,7,10,4,11,0,0,0,0,1.0000,"",0,0,1,0,0,57,54,47,45,20,2,4,5,6,7,0,2,3,6,23,0,2,3,3,6,7,4,7,8,9
"","","20010325","",2,"3",3,2,9,10,72,6,0,0,0,0,0,1.0000,"",0,0,0,2,5,0,4,2,6,19,0,2,6,13,13,66,58,53,38,22,0,2,5,8,6,0,0,0,1,0
"","","20010325","",3,"1",1,1,82,1,10,4,2,0,0,0,0,1.0000,"",0,0,0,2,2,65,54,59,52,42,0,2,0,0,1,1,5,4,10,14,0,5,3,2,3,0,0,0,2,3
...

-----------------------------------------------------
CORRESPONDING OUTPUT DATA:

Question  &            &  1   &  2   &  3   &  4   &  5   & Abstain\cr
          &            &      &      &      &      &      &        \cr
\qquad  1 & Individual &[67]  &  7   & 10   &  4   & 11   &  0     \cr
          & Pairs      &[79]  &  6   &  6   &  5   &  4   &  0     \cr
          &            &      &      &      &      &      &        \cr
\qquad  2 & Individual &  9   & 10   &[72]  &  6   &  0   &  2     \cr
          & Pairs      &  8   &  9   &[75]  &  8   &  0   &  0     \cr
          &            &      &      &      &      &      &        \cr
\qquad  3 & Individual &[82]  &  1   & 10   &  4   &  2   &  1     \cr
          & Pairs      &[86]  &  0   &  7   &  5   &  2   &  0     \cr
          &            &      &      &      &      &      &        \cr
...
"""
