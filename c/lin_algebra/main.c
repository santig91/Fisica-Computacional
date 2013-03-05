//
//  main.c
//  Taller3
//
//  Created by Santiago Grass Penagos on 2/03/13.
//  Copyright (c) 2013 Santiago Grass Penagos. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_linalg.h>
#include <gsl/gsl_matrix.h>
#include <gsl/gsl_cblas.h>
#include <gsl/gsl_blas.h>

int main(int argc, char *argv[])
{
    FILE *fp;
    fp=fopen(argv[1],"r");
   
    int i=0,j=0;
    int n=0,m=0;


   
    if ( fp != NULL )
    {
        size_t i, count, size = 100;
        double *x = malloc(size * sizeof(*x));
        double *y = malloc(size * sizeof(*y));

        if ( x != NULL && y != NULL )
        {
           
            for ( count = 0; count < size; ++count )
            {
                if ( fscanf (fp ,"%lf%lf", &x[count], &y[count]) != 2 )
                {
                    break;
                }
            }
         
	    // for ( i = 0; i < count; ++i )
            //{
	    // printf("x = %f, y = %f\n", x[i], y[i]);
            //}
        
        }
      
        n=100;
        m=3;
     
        float matriz [n][m];
        float tmatriz[m][n];
        for (i=0;i<n; i++)
        {
                
                matriz [i][0] =1;
                matriz [i][1] =x[i];
                matriz [i][2]=0.5*powf(x[i],2);
        }
       
        for (i=0;i<n;i++)
        {
                tmatriz[0][i]=matriz[i][0];
                tmatriz[1][i]=matriz[i][1];
                tmatriz[2][i]=matriz[i][2];
        }
        
        //float c[n][n];

    	gsl_matrix * c = gsl_matrix_alloc (n, n);

	 for(i=0;i<n;i++){ //row of first matrix
	 for(j=0;j<n;j++){  //column of second matrix
            int sum=0;
               int k;
	      for(k=0;k<n;k++)
	          sum=sum+tmatriz[i][k]*matriz[k][j];
	     gsl_matrix_set(c,i,j,sum);
	  }
        }

      
        
	for(i=0;i<n;i++)
        {
	for(j=0;j<n;j++)
	{
	  //      printf("%f",matriz[i][j]);
	  printf("%f",gsl_matrix_get(c,i,j));
	}
	printf("\n");
        }
// Define the dimension n of the matrix
	// and the signum s (for LU decomposition)
	
	int s;

	// Define all the used matrices

	gsl_matrix * inverse = gsl_matrix_alloc (n, n);
	gsl_permutation * perm = gsl_permutation_alloc (n);

	// Fill the matrix m

	// Make LU decomposition of matrix m
	gsl_linalg_LU_decomp (c, perm, &s);

	// Invert the matrix m
	gsl_linalg_LU_invert (c, perm, inverse);
	float D[n];

	 for(i=0;i<n;i++){ //row of first matrix
            for(j=0;j<n;j++){  //column of second matrix
                int sum=0;
                int k;
                for(k=0;k<n;k++)
                    sum=sum+matriz[i][k]*y[i];
		D[i]=sum;
            }
	    float m[3];
	 for(i=0;i<n;i++){ //row of first matrix
            for(j=0;j<n;j++){  //column of second matrix
                int sum=0;
                int k;
                for(k=0;k<n;k++)
		  sum=sum+gsl_matrix_get(inverse,i,j)*D[i];
		m[i]=sum;
            }
	    printf("m1=%f, m2=%f, m3=%f", m[1],m[2],m[3]);
        }
		

	 
    }
    }
    return 0;
}
                    
