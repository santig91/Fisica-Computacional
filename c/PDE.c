#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){

  int i;
  int n_points=1000;
  float u_initial;
  int delta_x=1;
  float delta_t=0.0005;
  float c=1;
  float r=c*delta_t/delta_x;
 
  for (i=0;i<n_points;i++)
  {
    u_initial=exp(-((i-0.3)*(i-0.3))/0.01); 
    printf("%f\n",u_initial);
  }
  return 0;
}
