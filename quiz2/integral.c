#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main (int argc, char *argv[])
{
  float b;
  float a;
  float h,x,y,area;
  float integral=0;
  int i;
  
  a=atof(argv[1]);
  b=atof(argv[2]);
  h=atof(argv[3]);
  
  float col=(b-a)/h;
  
  for (i=0;i<col;i++)
    {
      x=a+i*h;
      y=(1/(sqrt(1+cos(x)*sin(x))));
      area=y*h;
      integral=integral+area;
      
    }
  printf ("%f\n",integral);
  return 0;
}
