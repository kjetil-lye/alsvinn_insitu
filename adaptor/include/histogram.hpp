#pragma once
#include <mpi.h>
#include <fstream>

int getRankIndex(int nx, int ny, int nz, int ngx, int ngy, int ngz, double x, double y, double z)
{
        int ix = nx*x+ngx;
        int iy = ny*y+ngy;
        int iz = nz*z+ngz;
        return iz * (nx + 2 * ngx) * (ny + 2 * ngy) + iy * (nx + 2 * ngx) + ix;
}


void getPoints(double* p_x, double* p_y, double* p_z, int n)
{
//read from file or something.
      double values[2] = {0.5, 0.7};

      for (unsigned int i = 0; i<n; ++i)
      {
      p_x[i] =  (i<double(n)/2.)? values[0] : values[1];
      p_y[i] =  (i%4<2)? values[0] : values[1];
      p_z[i] =  (i%2)? values[0] : values[1];

      }
}



void write_histogram( const char* variable_name, const std::string pntidx,   const int values_size,double* values, const double min, const double max, const int nbins, const std::string path)
{

        //    float bins[nbins];
        int hist[nbins] = {0};
        const double delta = (max-min)/double(nbins-1);

        std::string fname = path+"hist_"+std::string(variable_name)+ pntidx+".csv";
        std::fstream outfile;
        outfile.open(fname,   std::fstream::out  );

        outfile<<" bins = ["<<min;
        for(int i =1; i<= nbins; i++)
        {
                outfile <<","<< min+i*(max-min)/double(nbins);
        }
        outfile<<" ]"<<std::endl;

        for(int i =0; i<= values_size; i++)
        {
                int idx =  (delta<=0) ? 0 :  (values[i] - min) /delta;
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
                int id1 =  (delta1<=0) ? 0 :  (values1[i]-min1) /delta1;
                int id2 =  (delta2<=0) ? 0 : (values2[i]-min2) /delta2;
                int index = id1 + id2*nbins;
                hist[index] += 1;
        //        std::cout<< fname << " " << *(values1+i)<<std::endl;
        //          std::cout<< fname << " " <<  *(values2+i)<<std::endl;

        }



        outfile<<" values = [ "<<hist[0];
        for(int i =1; i< nbins*nbins; i++)
        {
                outfile<< ", " << hist[i];
        }
        outfile<<" ]"<<std::endl;
        outfile.close();

}//end_make_histogram

/*
void make_histogramVTK( const char* variable_name, const int pntidx,  double* values, const int values_size, const double min, const double max, const int nbins,  vtkFloatArray* bins, vtkIntArray* hist )
{
        const double delta = (max-min)/double(nbins-1);
        bins->SetNumberOfComponents(1);
        bins->SetNumberOfTuples(nbins);
        bins->SetName( ("bins"+std::string(variable_name)+  std::to_string(pntidx)).c_str());

        hist->SetNumberOfComponents(1);
        hist->SetNumberOfTuples(nbins);
        hist->SetName( ( "hist_"+std::string(variable_name)+ std::to_string(pntidx)).c_str());
        for(int i =0; i< nbins; i++)
        {
                bins->SetValue(i, i*delta);
                hist->SetValue(i, 0);
        }

        for(int i =0; i< values_size; i++)
        {
                int idx = std::floor((*(values+i)-min) /delta);
                int tmp = hist->GetValue(idx)+1;
                hist->SetValue(idx,  tmp);
              //  std::cout<< " value : "<< tmp<< " idx "<< idx<<std::endl;
              //    std::cout<< " value : "<< *(values+i)<< " detal "<<delta<< " min: "<<min <<" max: "<<max << " divided : "<< (*(values+i)-min)/delta<< " idx "<< idx;
        }

}//end_make_histogramVTK



//is undone
    void make_pdf( const char* variable_name, const int pntidx,  double* values, const int values_size, const double min, const double max, const int nbins,  float* bins, int* hist )
{

    const int R = 6;
    const int M = values_size;

}*/
