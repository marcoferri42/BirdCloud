#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

#define N 100
#define L 10
#define V 0.5

// Generate birds with radom stats
//    stat 0: x position 
//    stat 1: y position 
//    stat 2: velocity vector direction
//    stat 3: velocity vector intensity
void birdGen(double brd[][4]){
  printf("generation-started\n");
  srand(time(0));
  for(int i=0; i<N; i++){
    for(int j=0; j<4; j++){
      if(j==0){       brd[i][j]= (float)rand()/(float)(RAND_MAX/(L));}
      else if(j==1){  brd[i][j]= (float)rand()/(float)(RAND_MAX/(L));}
      else if (j==2){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(360));}
      else if (j==3){ brd[i][j]= (float)rand()/(float)(RAND_MAX/(V))+V/2;}
    }
  }
}

// Save birdData to file
void persist(double brd[][4]){
  FILE *fp = fopen("coordBirds.dat", "w+");

  for(int i=0; i<N; i++){
    fprintf(fp, "%lf\t%lf\t%lf\t%lf\n", brd[i][0], brd[i][1], brd[i][2], brd[i][3]);
  }
  printf("birds-saved\n");
}

int main(){
  double birds[N][4];

  birdGen(birds);
  persist(birds);
  
  return 0;
}

// Theese birds love your console
void print2D(double arr[][3], int x, int y){
  for(int i=0; i<x; i++){
    for(int j=0; j<y; j++){
        printf("%lf\n", arr[i][j]);
    }
  }
}
