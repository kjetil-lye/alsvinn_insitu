#include "helper.hpp"


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


void getRankIndex(int nx, int ny, int nz,int ngx, int ngy, int ngz,   int multiXproc, int multiYproc, int multiZproc, double x, double y, double z, int &spatialrank, int &localindex)
{
        int nnx = nx+2*ngx;
        int nny = ny*2*ngy;
        int nnz = nz*2*ngz;

        int idx = nnx*multiXproc*x;
        int idy = nny*multiYproc*y;
        int idz = nnz*multiZproc*z;
//  std::cout<< "nx "<< nx<<" x "<<x <<" idx "<<idx<<std::endl;
//  std::cout<< "ny "<< ny<<" y "<<y <<" idx "<<idy<<std::endl;
//  std::cout<< "nz "<< nz<<" z "<<z <<" idx "<<idz<<std::endl;
        int domx = std::floor(idx/nnx);
        int domy = std::floor(idy/nny);
        int domz = std::floor(idz/nnz);

        spatialrank = domx +domy*(multiXproc)+domz*(multiXproc)*(multiXproc);
        localindex = (idx%nnx) + (idy%nny)*nnx + (idz%nnz)*nnx*nny;

        //std::cout<<" local points index "<< localindex<<std::endl;
        //  std::cout<<" local points rank "<< spatialrank<<std::endl;
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
                int id2 =  (delta2<=0) ? 0 : (values2[i])-min2) /delta2;
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



void CatalystCoProcessHistogram(void* data, void* parameters, double time,
                                const char* variable_name,  double* variable_data, int nx, int ny, int nz,
                                int ngx, int ngy, int ngz, double ax, double ay, double az, double bx,
                                double by, double bz, int gpu_number )

{

        auto my_parameters = static_cast<MyParameters*>(parameters);

        std::string mb = my_parameters->getParameter("multiblock");
        const int multiXproc = std::stoi(mb.substr(0,1) );
        const int multiYproc = std::stoi(mb.substr(2,1) );
        const int multiZproc = std::stoi(mb.substr(4,1) );
        const int numProcS = multiXproc*multiYproc*multiZproc;

        int mpi_rank;
        MPI_Comm_rank(my_parameters->getMPIComm(), &mpi_rank);
        int mpi_size;
        MPI_Comm_size(my_parameters->getMPIComm(), &mpi_size);
        int mpi_spatialRank;          // is the same as the sampleRank
        MPI_Comm_rank(spatialComm, &mpi_spatialRank);
        int mpi_spatialSize;          // is the same as number of samples
        MPI_Comm_size(spatialComm, &mpi_spatialSize);


        //check if we can run all in parallel:
        int nsamples = std::stoi(my_parameters->getParameter("samples"));
        if(mpi_size < nsamples) {
                std::cerr<< "warning: not enough mpi nodes,  reduce sample size to number of mpi nodes: "<< mpi_size<<std::endl;
        }


        int norm_samples = nsamples;
        const size_t ndata = (ngx*2+nx)*(ny+2*ngy)*(nz+2*ngz);
        double avrg_data[ndata];
        double avrg_sqr_data[ndata];


        MPI_Reduce(variable_data, avrg_data, ndata, MPI_DOUBLE, MPI_SUM, 0,spatialComm);

        double sqr_variable_data[ndata];
        //get squared sum to use for variance, reuse variable_data to save space
        for (int i = 0; i< ndata; ++i) {
                sqr_variable_data[i] = variable_data[i]*variable_data[i];
        }

        MPI_Reduce(&sqr_variable_data, avrg_sqr_data, ndata, MPI_DOUBLE, MPI_SUM, 0, spatialComm);



        const int nii = std::stoi(my_parameters->getParameter("hist_npoints"));
        const bool twoPoint = std::stoi(my_parameters->getParameter("hist_2points"));
        double *pnt_values;
        double *pnt_values2;
        const int pnt_values_size = nsamples;
        int locPntIndex[nii];
        double px[nii];
        double py[nii];
        double pz[nii];
        getPoints(px,py,pz, nii);


        if(mpi_spatialRank ==0)
        {
                pnt_values = (double*)malloc(sizeof(double) * (pnt_values_size));
                if( twoPoint)
                {
                        pnt_values2 = (double*)malloc(sizeof(double) * (pnt_values_size));
                }
        }

        //collect data points from all frames to store all frame values for specifc points
        const std::string path = my_parameters->getParameter("hist_folder");
        //historgram calculcation for specifc points only;
        const int nbins = std::stoi(my_parameters->getParameter("hist_nbins"));

        //  std::cout<<"rank       "<< mpi_rank<<"  - "<< getSpatialRank(mpi_rank, numProcS)<< "  - "<< mpi_spatialRank<<std::endl;

        //MPI_Barrier(spatialComm);


        for ( int i =0; i<nii; i++)
        {
                int pointSR = 0;
                int locPntIndex = 0;
                int pointSR2 = 0;
                int locPntIndex2 = 0;

                getRankIndex(nx, ny, nz,ngx,ngy,ngz,  multiXproc, multiYproc, multiZproc, px[i], py[i], pz[i], pointSR,  locPntIndex);


                if( twoPoint && i <nii-1)
                {
                        getRankIndex( nx, ny, nz,ngx,ngy,ngz, multiXproc, multiYproc, multiZproc, px[i+1], py[i+1], pz[i+1], pointSR2,  locPntIndex2);
                  }

                //      std::cout<<" local points index "<< locPntIndex <<" ndata "<< ndata<<std::endl;
                //      std::cout<<" local points rank       "<< pointSR<<"  - "<< getSpatialRank(mpi_rank, numProcS)<<std::endl;



                if(pointSR ==  getSpatialRank(mpi_rank, numProcS) )
                {

                        //       std::cout<<"rank       "<< mpi_rank<<"  - "<< getSpatialRank(mpi_rank, numProcS)<< "  - "<< mpi_spatialRank<<std::endl;
                        MPI_Gather(variable_data+locPntIndex, 1,  MPI_DOUBLE,  pnt_values, 1, MPI_DOUBLE, 0,  spatialComm);
                        if(mpi_spatialRank ==0)
                        {
                                //          std::cout<<"rank       "<< mpi_rank<< " gaather       "<< pnt_values[0] <<"  - "<<  pnt_values[1]  <<"  - "<<  pnt_values[2] <<"  - "<<  pnt_values[3]<<std::endl;
                                if (!twoPoint)
                                {
                                    std::string pntname = std::to_string( px[i]).substr(0,4)+"x"+ std::to_string( py[i]).substr(0,4)+"y"+ std::to_string( pz[i]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                    auto minmax = std::minmax_element(pnt_values, pnt_values+pnt_values_size );
                                    write_histogram(  variable_name,  pntname,  pnt_values, pnt_values_size, *(minmax.first),  *(minmax.second),  nbins, path);
                                }
                                else if( pointSR != pointSR2 && i <nii-1 )     //only have to send it to different node if ppoints are not on same!
                                {
                                        MPI_Send(pnt_values, pnt_values_size, MPI_DOUBLE, pointSR2, 0, MPI_COMM_WORLD);
                                }
                        }
                }


                if(twoPoint && i <nii-1 && pointSR2 ==  getSpatialRank(mpi_rank, numProcS))
                {

                          MPI_Gather(variable_data+locPntIndex2, 1,  MPI_DOUBLE,  pnt_values2, 1, MPI_DOUBLE, 0,  spatialComm);

                          if(mpi_spatialRank ==0)
                          {
                                  std::string pntname = std::to_string( px[i]).substr(0,4)+"x"+ std::to_string( py[i]).substr(0,4)+"y"+ std::to_string( pz[i]).substr(0,4)+"z_";
                                  pntname += "_"+ std::to_string( px[i+1]).substr(0,4)+"x"+ std::to_string( py[i+1]).substr(0,4)+"y"+ std::to_string( pz[i+1]).substr(0,4)+"z_"+std::to_string(time).substr(0,4);
                                  auto minmax2  = std::minmax_element(pnt_values2, pnt_values2+nsamples );
                                  if(pointSR != pointSR)
                                  {
                                    MPI_Recv(pnt_values, pnt_values_size, MPI_DOUBLE, pointSR, 0, MPI_COMM_WORLD,   MPI_STATUS_IGNORE);
                                 }
                                  auto minmax = std::minmax_element(pnt_values, pnt_values+pnt_values_size );
                                  write_2pt_histogram(  variable_name,  pnt_values_size, pntname, pnt_values, *(minmax.first),  *(minmax.second),  pnt_values2, *(minmax2.first),  *(minmax2.second),  nbins, path);
                          }

                }
        }          //end for nii



        if(mpi_spatialRank == 0)
        {

                int mpi_statRank;                   // is the same as the getSpatialRank
                MPI_Comm_rank(coproc_comm, &mpi_statRank);


                if (VTKGrid == NULL)
                {

                        int x_dom = mpi_statRank%multiXproc;
                        int y_dom = (mpi_statRank/multiXproc)%multiYproc;
                        int z_dom = mpi_statRank/multiYproc/multiXproc;

                        int extend[6];                   // ={0,0,0,0,0,0}; //  = {0, multiXproc*nx-1,0,multiYproc*ny-1,0,multiZproc*nz-1};

                        extend[0] = x_dom*nx;
                        extend[1] = ( x_dom+1)*nx-1;
                        extend[2] = y_dom*ny;
                        extend[3] = ( y_dom+1)*ny-1;
                        extend[4] = z_dom*nz;
                        extend[5] = ( z_dom+1)*nz-1;

                        vtkImageData* VTKImage = vtkImageData::New();
                        VTKImage->SetOrigin(0, 0, 0);
                        VTKImage->SetExtent(extend);

                        VTKGrid = vtkMultiBlockDataSet::New();
                        vtkNew<vtkMultiPieceDataSet> multiPiece;
                        multiPiece->SetNumberOfPieces(numProcS);
                        multiPiece->SetPiece( mpi_statRank, VTKImage);


                        VTKGrid->SetNumberOfBlocks(1);
                        VTKGrid->SetBlock(0, multiPiece.GetPointer());
                }

                fillGrid(mpi_rank, numProcS, multiXproc,multiYproc, multiZproc, variable_name,  nx,  ny,  nz, ngx,  ngy,  ngz, avrg_data, avrg_sqr_data, norm_samples);



        }          //end rank 0

}     //CatalystCoProcessHistogram