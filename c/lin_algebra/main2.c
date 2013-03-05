#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_cblas.h>
#include <gsl/gsl_blas.h>
#include <gsl/gsl_eigen.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    fp=fopen(argv[1],"r");
   
    int i=0,j=0;
    int n=0,m=0;
    int count=3;
    gsl_matrix * sigmap = gsl_matrix_alloc (count, count);
    if ( fp != NULL )
      {
        size_t i, countt, size = 10000;
        double *x = malloc(size * sizeof(*x));
        double *y = malloc(size * sizeof(*y));
	double *z = malloc(size * sizeof(*z));


        if ( x != NULL && y != NULL && z != NULL )
        {
           
            for ( countt = 0; countt < size; ++countt )
            {
	      if ( fscanf (fp ,"%lf%lf%lf", &x[countt], &y[countt], &z[countt]) != 3 )
                {
                    break;
                }
            }
 
        }
	double sigma[count][count];
	for (i=0;i<count;i++)
	  {
	    for(j=0;j<count;j++)
	      {
		sigma[i][j]=(x[i]-((x[i]+y[i]+z[i])*0.333333))*(x[j]-((x[j]+y[j]+z[j])*0.333333))+(y[i]-((x[i]+y[i]+z[i])*0.333333))*(y[j]-((x[j]+y[j]+z[j])*0.333333))+(z[i]-((x[i]+y[i]+z[i])*0.333333))*(z[j]-((x[j]+y[j]+z[j])*0.333333));
		
	      }
	  }

	//	for (i=0;i<count;i++)
	//{
	  // for(j=0;j<count;j++)
	  //{
	  //  double t;
	  //  t=sigma[i][j];
	      //gsl_matrix_set(sigmap,i,j,sigma[i][j]);
	  //}
	  //}
    
      }
        return 0;
}
       



