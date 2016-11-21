
//--------------------- 3 HACER PISTON MOVIBLE --------------------------------- 

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
using namespace std;

// global constants
const int N = 3;
const double G = 9.81; // m/s^2
const double DT = 0.005; // m/s^2
const double K = 300.0; // N/m
const double LX = 6.0; // m
const double LY=12.0; //m




//---------- estructura del piston ----------------------------------------

struct Piston {
  double Pos_old = 0, Pos = 8 ,  PV = 0,  PF = 0;
  double Mass = 20;
  void Parranque(double dt);
  void Ptimestep(double dt);
};

void Piston::Parranque(double dt)
{
   Pos_old = Pos - dt*PV + PF*dt*dt/(2*Mass);   
}

void Piston::Ptimestep(double dt)
{
  double TMP;

  TMP = Pos;
  Pos = 2*Pos - Pos_old + PF*dt*dt/(Mass);   
  PV = (Pos - Pos_old)/(2*dt);
  Pos_old = TMP;
}


// ---------------- body class -------------------------------

struct Body {
  double Rxold = 0, Ryold = 0, Rx = 0, Ry = 0, Vx = 0, Vy = 0, Fx = 0, Fy = 0;
  double mass = 1;
  double rad = 0;
  void arranque(double dt);
  void timestep(double dt);
};


void Body::arranque(double dt)
{
  Rxold = Rx - dt*Vx + Fx*dt*dt/(2*mass);   
  Ryold = Ry - dt*Vy + Fy*dt*dt/(2*mass);   
}

void Body::timestep(double dt)
{
  double tmp;

  tmp = Rx;
  Rx = 2*Rx - Rxold + Fx*dt*dt/(mass);   
  Vx = (Rx - Rxold)/(2*dt);
  Rxold = tmp;

  tmp = Ry;
  Ry = 2*Ry - Ryold + Fy*dt*dt/(mass);   
  Vy = (Ry - Ryold)/(2*dt);
  Ryold = tmp;
}

//----------- function declarations ------------------------------


void compute_forces(Body bodies[],Piston piston[]);

void start (Body bodies[],Piston piston[], double dt);
void evolve(Body bodies[],Piston piston[], double dt);

void init_gnuplot(void);
void print_to_gnuplot(Body bodies[],Piston piston[]);


//------------ MAIN - FUNCION PRINCIPAL ---------------------------------------------
int main(void)
{
 
  srand(0); //random seed

  std::ofstream fout("datos.txt");
  Body bodies[N];
  Piston piston[N];
  
  for(int i=0;i<N;i++){
    
  bodies[i].rad = 0.3;
  bodies[i].Rx = 1 + double(rand())/RAND_MAX;
  bodies[i].Ry = 1 + double(rand())/RAND_MAX;
  bodies[i].Vx = 0;
  bodies[i].Vy = 0;

  }

  
  compute_forces(bodies,piston);

  init_gnuplot();

  start(bodies,piston, DT);

  for (int it = 0; it < 5000; ++it) {
    fout << DT*it << "  " << bodies[0].Ry << std::endl; //---->aqui es donde se imprime los datos para graficar. 
    compute_forces(bodies,piston);
    evolve(bodies,piston, DT);
    print_to_gnuplot(bodies,piston);
  }

  fout.close();

  return 0;
}



//------------- Defincion de funciones-------------------------

// ------------ funcion de fuerzas-----------------------------



void compute_forces(Body bodies[],Piston piston[])
{
  int ii;
  double delta;

  // reset forces
  piston[0].PF=0.0;
  for (ii = 0; ii < N; ++ii) {
    bodies[ii].Fx = 0.0;
    bodies[ii].Fy = 0.0;
  }

  // Fuerza gravitacional Piston
    piston[0].PF += -piston[0].Mass*G;




  // add force with bottom wall
  for (ii = 0; ii < N; ++ii) {
    delta = bodies[ii].rad - bodies[ii].Ry;
    if (delta > 0) {
      bodies[ii].Fy += K*delta;
    }
  } 
 // Fuerza con el piston 
   for (ii = 0; ii < N; ++ii) {
    delta = bodies[ii].rad + bodies[ii].Ry - piston[0].Pos;
    if (delta > 0) {
      bodies[ii].Fy += -K*delta;
      piston[0].PF += K*delta;
    }
  } 


  // add force with right wall
  for (ii = 0; ii < N; ++ii) {
    delta = bodies[ii].rad + bodies[ii].Rx - LX;
    if (delta > 0) {
      bodies[ii].Fx += -K*delta;
    }
  } 

  // add force with left wall
  for (ii = 0; ii < N; ++ii) {
    delta = bodies[ii].rad - bodies[ii].Rx;
    if (delta > 0) {
      bodies[ii].Fx += +K*delta;
    }
  } 

  // fuerza with other bodies
  int jj;
  double Rijx, Rijy, Rij, Fx, Fy;
  for (ii = 0; ii < N; ++ii) {
    for (jj = ii+1; jj < N; ++jj) {
      Rijx = bodies[ii].Rx - bodies[jj].Rx;
      Rijy = bodies[ii].Ry - bodies[jj].Ry;
      Rij = std::sqrt(Rijx*Rijx + Rijy*Rijy);
      delta = bodies[ii].rad + bodies[jj].rad - Rij;
      if (delta > 0) {
	Fx = K*delta*Rijx/Rij;
	Fy = K*delta*Rijy/Rij;
	bodies[ii].Fx += Fx;
	bodies[ii].Fy += Fy;
	bodies[jj].Fx -= Fx;
	bodies[jj].Fy -= Fy;
      }
    }
  }  
}

//----- funciones de arranque ------------------------
void start(Body bodies[],Piston piston[], double dt)
{
  
  int ii;
  piston[0].Parranque(dt);
  for (ii = 0; ii < N; ++ii) {
    bodies[ii].arranque(dt);
  }
}

void evolve(Body bodies[],Piston piston[], double dt)
{

  int ii;
  piston[0].Ptimestep(dt);
  for (ii = 0; ii < N; ++ii) {
    bodies[ii].timestep(dt);
  }
}

//--------para dibujar --------------------------------
void init_gnuplot(void)
{
  std::cout << "set size ratio -1" << std::endl;
  std::cout << "set parametric" << std::endl;
  std::cout << "set trange [0:1]" << std::endl;
  std::cout << "set xrange [-1:" << LX << "]" << std::endl;
  std::cout << "set yrange [-1: "<< LY << "]" << std::endl;
}


void print_to_gnuplot(Body bodies[], Piston piston[])
{
  std::cout << "plot "; 
  std::cout << piston[0].Pos ;
  for (int ii = 0; ii < N; ++ii) {
    std::cout << bodies[ii].Rx << " + " << bodies[ii].rad << "*cos(t*2*pi) , "
	      << bodies[ii].Ry << " + " << bodies[ii].rad << "*sin(t*2*pi) , ";
    
    
  }
  std::cout << " 0, 0"; 
  std::cout << std::endl;
}
