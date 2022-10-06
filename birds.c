#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

#define N 2
#define L 1000
#define V 0.5

double Bird_Gen(double brd[][4]);
void Save_Bird(double brd[][4], FILE *fp);
void print2D(double arr[][3], int x, int y);

int main(){
  srand(time(0));

  FILE *fp =fopen("coordBirds.dat", "w+");

  double brd[N][4];
  Bird_Gen(brd);

  Save_Bird(brd, fp);
  printf("Bird Generati\n");
}

double Bird_Gen(double brd[][4]){
  for(int i=0; i<N; i++){
    for(int j=0; j<4; j++){
      if(j==0){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(L));}
      else if(j==1){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(L));}
      else if (j==2){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(360));}
      else if (j==3){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(V))+V/2;}
    }
  }
}

void Save_Bird(double brd[][4], FILE *fp){
  for(int i=0; i<N; i++){
    fprintf(fp, "%lf\t%lf\t%lf\t%lf\n", brd[i][0], brd[i][1], brd[i][2], brd[i][3]);
  }
}

void print2D(double arr[][3], int x, int y){
  for(int i=0; i<x; i++){
    for(int j=0; j<y; j++){
        printf("%lf\n", arr[i][j]);
    }
  }
}
