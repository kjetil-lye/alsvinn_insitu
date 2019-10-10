
#include<iostream>
#include<cmath>

#include<limits>

#include<Eigen/LU>

#include<Eigen/Dense>

typedef double value_t;

//value_t      legendre( unsigned int n, value_t x );


Eigen::MatrixXd getJ

std::function<int(int)> makeLambda(int a){    // (1)
    return [a](int b){ return a + b; };
}
value_t simpsonRule(const value_t a , const value_t b , std::function<value_t(value_t)>f, const unsigned int n=100)
{
  value_t integ  = 0;
  value_t h = (b-a)/double(n);
  for( unsigned int i= 0; i<n-1 ; ++i)
  {
      integ += h/6.0*(f( a+i*h )+4*f(a+(i+0.5)*h)+f(a+(i+1)*h) );
  }
  return integ;
}

value_t monteCarloMoment(const Eigen::VectorXd &lambda, const unsigned int M, const unsigned int j)
{


}
value_t recover_rho(const Eigen::VectorXd &lambda, value_t point, const int R )
{
  value_t sum = lambda(0);
  for (unsigned int k= 1; k<R; ++k)
  {
    sum += lambda(k)*std::legendre(k, point);
  }

    return std::exp(sum);
}

value_t quad_PjPk( const Eigen::VectorXd &lambda, const int M, const unsigned int j, const unsigned int k=0)
{
  auto f[&](value_t q){return recover_rho(lambda,q,R)*std::legendre(j, q )*std::legendre( k, q )};
  return simpsonRule(-1,1,f)
}


Eigen::VectorXd getF(const Eigen::VectorXd &lambda, value_t *values, const size_t values_size, const int R)
{
  Eigen::VectorXd F = Eigen::VectorXd::Ones(R);

  for (unsigned int j=0; j<R, ++j)
  {
    F(j) = quad_PjPk(lambda, M, j);
  }


}





int myNewton(value_t *values, Eigen::VectorXd &x0, Eigen::VectorXd &x, const int M, const int R, const value_t acc )
{
  value_t err = std::numeric_limits<value_t>::max();
  const int maxit = 200;
  int i = 0;

  while (err>acc && i<maxit)
  {

  Eigen::MatrixXd J =
  Eigen::VectorXd F =


    /* code */
  }



          J = f_DF(x, X,M,R)
          F = f_F(x, X,M,R)
          print(" F ", F)
          print("J", J)
          dx = np.linalg.solve(J,F)
          x -= dx
          err = np.linalg.norm(dx)
          i+=1
          print("# of Newton iterations :  ", i, " with  norm(dx) = ",err)
          fnorm = np.linalg.norm(F)
          if(fnorm < fnormold):
              xmin = x
              fnormold=fnorm
              dxnormold =err

          if(i >= maxit): #should return x with where err is smallest...
              print("reached maxit of Newton iterations :  ", i)
              print("use lambda = ", xmin,  " instead of ", x)
              x=xmin


}
