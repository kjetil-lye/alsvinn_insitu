#pragma once
#include <mpi.h>


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
        p_x[0] = 0.5;
        p_x[1] = 0.75;
        p_y[0] = 0.5;
        p_y[1] = 0.75;
        p_z[0] = 0.5;
        p_z[1] = 0.5;
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
                int idx =  (delta<=0) ? 0 : s (*(values+i)-min) /delta;
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
                int id1 =  (delta1<=0) ? 0 :  (*(values1+i)-min1) /delta1;
                int id2 =  (delta2<=0) ? 0 : (*(values2+i)-min2) /delta2;
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

}//end_make_histogram

void CatalystCoProcesHistogram(void* data, void* parameters, double time,
                                          const char* variable_name,  double* variable_data, int nx, int ny, int nz,
                                          int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
                                          double by, double bz, int gpu_number )

{
                 auto my_parameters = static_cast<MyParameters*>(parameters);

                  int mpi_rank;
                  MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
                  int mpi_size;
                  MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
                  //check if we can run all in parallel:
                  int nsamples = std::stoi(my_parameters->getParameter("samples"));
                  if(mpi_size < nsamples) {
                          std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
                  }

                  // make nsamples per group, to use for normalzation:
                  if(nsamples%mpi_size!=0) {
                          std::cerr<< "warning: nsmaples not divisible by mpi_size : "<< nsamples/mpi_size<<std::endl;
                  }

                  int norm_samples = nsamples;
                  const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
                  double avrg_data[ndata];
                  double avrg_sqr_data[ndata];


                  //historgram calculcation for specifc points only;
                  const int nii = std::stoi(my_parameters->getParameter("hist_npoints"));
                  const bool twoPoint = std::stoi(my_parameters->getParameter("hist_2points"));
                  double px[nii];
                  double py[nii];
                  double pz[nii];
                  getPoints(px,py,pz, nii);
                  double *pnt_values;
                  const int pnt_values_size = nii*nsamples;


                          if(mpi_rank ==0)
                          {
                                  pnt_values = (double*)malloc(sizeof(double) * (pnt_values_size));
                          }

                          //collect data points from all frames to store all frame values for specifc points
                          for ( int i =0; i<nii; i++)
                          {
                                  int idx = getRankIndex(nx, ny, nz,  ngx, ngy, ngz, px[i], py[i], pz[i]);

                //                  std::cout<< "rank, pt " << mpi_rank << " "<< idx<<" " <<*(variable_data+idx)<<std::endl;
                                  MPI_Gather(variable_data+idx, 1,  MPI_DOUBLE,  pnt_values+(i*nsamples), 1, MPI_DOUBLE, 0,  my_parameters->getMPIComm());
                          }



                  MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());

                  double sqr_variable_data[ndata];
                  //get squared sum to use for variance, reuse variable_data to save space
                  for (int i = 0; i< ndata; ++i) {
                          sqr_variable_data[i] = variable_data[i]*variable_data[i];
                  }


                  MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, my_parameters->getMPIComm());


                  if(mpi_rank == 0)
                  {

                              //collect data points from all frames to store all frame values for specifc points
                            const std::string path = my_parameters->getParameter("hist_folder");
                           //historgram calculcation for specifc points only;
                            const int nbins = std::stoi(my_parameters->getParameter("hist_nbins"));

                                  for ( int i =0; i<nii; i++)
                                   {
                                        std::string pntname = std::to_string( px[i]).substr(0,4)+"x"+ std::to_string( py[i]).substr(0,4)+"y"+ std::to_string( pz[i]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                         auto minmax = std::minmax_element(pnt_values+(i*nsamples),pnt_values+(i+1)*nsamples );
                                      //    make_histogram( variable_name, idxOfInterest[i],  pnt_values+i*nsamples, nsamples, *(minmax.first),  *(minmax.second), nbins,  bins,  hist );
                                        if(!twoPoint)
                                        {
                                            write_histogram(  variable_name, pntname, nsamples, pnt_values+(i*nsamples), *(minmax.first),  *(minmax.second),  nbins, path);
                                          }
                                        else if(twoPoint && i <nii-1)
                                          {
                                            pntname += "_"+ std::to_string( px[i+1]).substr(0,4)+"x"+ std::to_string( py[i+1]).substr(0,4)+"y"+ std::to_string( pz[i+1]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                            auto minmax2  = std::minmax_element(pnt_values+(i+1)*nsamples, pnt_values+(i+2)*nsamples);
                                            write_2pt_histogram( variable_name, nsamples,pntname, pnt_values+(i*nsamples),*(minmax.first),  *(minmax.second), pnt_values+((i+1)*nsamples), *(minmax2.first),  *(minmax2.second),  nbins, path);

                                          }

                                  }


                                  int extend[6]  = {0,nx-1,0,ny-1,0,nz-1};//{ngx, nx+ngx, ngy, ny+ngy, ngz, 0}; //nz+ngz };

                                  if (VTKGrid == NULL)
                                  {
                                          VTKGrid = vtkImageData::New();
                                          VTKGrid->SetExtent(extend); //ngx, ngx+nx, ngy, ngy+ny, ngz, ngz+nz);
                                  }

                                  dataDescription->GetInputDescriptionByName("input")->SetGrid(VTKGrid);
                                  // For structured grids we need to specify the global data extents

                                  // Create a field associated with points
                                  vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
                                  vtkDoubleArray* field_array_var = vtkDoubleArray::New();
                                  int ntuples = nx*ny*nz;
                                  field_array_mean->SetNumberOfComponents(1);
                                  field_array_mean->SetNumberOfTuples(ntuples);
                                  field_array_var->SetNumberOfComponents(1);
                                  field_array_var->SetNumberOfTuples(ntuples);
                                  field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
                                  field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
                                  int index = 0;
                                  int idx = 0;

                                  // ignoring ghost cells (ngy is number of ghost cells in z direction)
                                  for (int z = ngz; z < nz + ngz; ++z) {
                                          // ignoring ghost cells (ngy is number of ghost cells in y direction)
                                          for (int y = ngy; y < ny + ngy; ++y) {
                                                  // ignoring ghost cells (ngx is number of ghost cells in x direction)
                                                  for (int x = ngx; x < nx + ngx; ++x) {
                                                          index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                                                          double tmp = avrg_data[index]/double(norm_samples);
                                                          field_array_mean->SetValue(idx, tmp);
                                                          //  tmp *=(avrg_data[index]/double(nsamples));
                                                          tmp =  avrg_sqr_data[index]/double(norm_samples) -tmp*tmp;
                                                          field_array_var->SetValue(idx, tmp);
                                                          idx += 1;
                                                  }
                                          }

                                  }

                                  VTKGrid->GetPointData()->AddArray(field_array_mean);
                                  VTKGrid->GetPointData()->AddArray(field_array_var);
                                  field_array_mean->Delete();
                                  field_array_var->Delete();
                          free(pnt_values);
                  }//end rank 0
    } //CatalystCoProcesHistogram





/*is undone */
    void make_pdf( const char* variable_name, const int pntidx,  double* values, const int values_size, const double min, const double max, const int nbins,  vtkFloatArray* bins, vtkIntArray* hist )
{

    const int R = 6;
    const int M = values_size;

}
