DataSet myData = ReadFromString(">s1\nA\n>s2\nA\n>s3\nG\n");
DataSetFilter myFilter = CreateFilter(myData, 1);

F81mat = {{ *, u, u, u},
          { u, *, u, u},
          { u, u, *, u},
          { u, u, u, *}};
basefreqs = {{0.25, 0.25, 0.25, 0.25}};

Model F81 = (F81mat, basefreqs);

ACCEPT_ROOTED_TREES = 1;
ACCEPT_BRANCH_LENGTHS = 1;
//Tree tr = "((s1:0.1,s2:0.1):0.1,s3:0.2):0;";
Tree tr = "((s2:0.1,s3:0.1):0.1,s1:0.2):0;";

LikelihoodFunction myLF = (myFilter, tr);
fprintf(stdout, myLF);

