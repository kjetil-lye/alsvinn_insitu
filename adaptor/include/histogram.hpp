//#include "helper.hpp"

#include <mpi.h>
#include <fstream>
#include <limits>
#include <iomanip>
#include <algorithm>
#include <iostream>
#include <cmath>
#include<vector>
#include<string>

void getPoints(double* p_x, double* p_y, double* p_z, int n )
{
//read from file or something.
  double values[2] = {0.5, 0.7};

  for (unsigned int i = 0; i<n; ++i)
  {
      p_x[i] =  (i<double(n)/2.)? values[0] : values[1];
      p_y[i] =  (i%4<2)? values[0] : values[1];
      p_z[i] =  (i%2)? values[0] : values[1];

}
      /*  p_x[0] = 0.5;
        p_x[1] = 0.75;
        p_y[0] = 0.5;
        p_y[1] = 0.75;
        p_z[0] = 0.5;
        p_z[1] = 0.5;*/
}


void getRankIndex(int nx, int ny, int nz,int ngx, int ngy, int ngz,   int multiXproc, int multiYproc, int multiZproc, double x, double y, double z, int &spatialrank, int &localindex)
{
        //total numer of cells
        int nnx = nx+2*ngx;
        int nny = ny+2*ngy;
        int nnz = nz+2*ngz;
        // global indices
        int idx = nnx*multiXproc*x;
        int idy = nny*multiYproc*y;
        int idz = nnz*multiZproc*z;
        //block domain indices
        int domx = std::floor(idx/nnx);
        int domy = std::floor(idy/nny);
        int domz = std::floor(idz/nnz);

        spatialrank = domx + domy*multiXproc+domz*multiYproc*multiXproc;
        localindex = (idx%nnx) + (idy%nny)*nnx + (idz%nnz)*nnx*nny;
}


void write_histogram( const char* variable_name, const std::string pntidx,  double* values, const int values_size, const double min, const double max, const int nbins, const std::string path)
{

        //    float bins[nbins];
        int hist[nbins] = {0};
        const double delta = (max-min)/double(nbins-1);

        std::string fname = path+"hist_"+std::string(variable_name)+ pntidx+".csv";
        std::fstream outfile;
        outfile.open(fname,   std::fstream::out  );

        outfile<<" bins = ["<<min;
        for(int i =1; i< nbins; i++)
        {
                //  bins[i] = i*delta;
                //    hist[i]=0;
                outfile <<","<< min+i*(max-min)/double(nbins);
        }
        outfile<<" ]"<<std::endl;

        for(int i =0; i< values_size; i++)
        {
                int idx =  (delta<=0) ? 0 : std::round(double(values[i]-min) /delta);
                //        std::cout<< " his <<"<< idx << " nbins "<<delta<<" "<< values[i]<< " i" << i <<std::endl;
                hist[idx] += 1;
        }

        outfile<<" values = [ "<<hist[0];
        for(int i =1; i< nbins; i++)
        {
                outfile<< ", " << hist[i];
        }
        outfile<<" ]"<<std::endl;
        outfile.close();

}//end_make_histogram

void write_2pt_histogram( const char* variable_name,  const int values_size, const std::string name, double* values1,  const double min1, const double max1, double* values2, const double min2, const double max2, const int nbins, const std::string path)
{

        int hist[nbins*nbins] = {0};
        const double delta1 = (max1-min1)/double(nbins-1);
        const double delta2 = (max2-min2)/double(nbins-1);

        std::string fname = path+"hist_"+std::string(variable_name)+ name+".csv";
        std::fstream outfile;
        outfile.open(fname,   std::fstream::out  );

        outfile<<" bins1 = ["<<min1;
        for(int i =1; i<=nbins; i++)
        {
                outfile <<","<< min1+i*(max1-min1)/double(nbins);
        }
        outfile<<" ]"<<std::endl;


        outfile<<" bins2 = ["<<min2;
        for(int i =1; i<=nbins; i++)
        {
                outfile <<","<< min2+i*(max2-min2)/double(nbins);
        }
        outfile<<" ]"<<std::endl;


        for(int i =0; i< values_size; i++)
        {
                // values1[i]
                int id1 =  (delta1<=0) ? 0 :  (values1[i]-min1) /delta1;
                int id2 =  (delta2<=0) ? 0 : (values2[i]-min2) /delta2;
                int index = id1 + id2*nbins;
                hist[index] += 1;
        }



        outfile<<" values = [ "<<hist[0];
        for(int i =1; i< nbins*nbins; i++)
        {
                outfile<< ", " << hist[i];
        }
        outfile<<" ]"<<std::endl;
        outfile.close();

}//end_make_histogram


void write_timers(std::vector<double> timers, int rank, std::string path)
{
	std::string names[11] = {"total", "mpi_reduce", "square for loop" , "mpi reduce 2", "loop over histogramm points", "mpi gather", "mpi send","mpi gather 2nd point", "mpi receive", "malloc", "gridfill()"};
	std::string fname = path+"timings_rank"+std::to_string(rank)+".json";
        std::fstream outfile;
        outfile.open(fname,   std::fstream::out  );
	outfile<<"{"<<std::endl;
        outfile<<"\t"<<"\"Timing:\""<<std::endl;
	outfile<<"\t {"<<std::endl;
        for(int i =0; i< 10; i++)
        {
		outfile<<"\t"<<"\t \" " << names[i]<< "\" : "<<std::to_string(timers[i])<<","<<std::endl;
        }

	outfile<<"\t"<<"\t \" " << names[10]<<  "\" : "<<std::to_string(timers[10])<<std::endl;
	outfile<<" \t}"<<std::endl;
	outfile<<"}"<<std::endl;
        outfile.close();

}//end_make_histogram


