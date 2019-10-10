#include <mpi.h>
#include <fstream>
#include <algorithm>
#include <limits>


inline int getSpatialRank(int globalR, int numProcS){
        return globalR%numProcS;
};

inline int getStatisticalRank(int globalR, int numProcS){
        return globalR/numProcS;
};


/*
   void addsquared(double *, double *, int *, MPI_Datatype *);

   void addsquared(double *in, double *out, int *len, MPI_Datatype *)
   {
        int i;
        for ( i=0; i<*len; i++ )
                out[i] += in[i]*in[i];
   }
 */
