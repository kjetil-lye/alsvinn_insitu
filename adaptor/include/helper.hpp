

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



 
void fillGrid(int mpi_rank, int numProcS, int multiXproc,int multiYproc, int multiZproc, const char* variable_name, int nx, int ny, int nz, int ngx, int ngy, int ngz, double avrg_data[], double avrg_sqr_data[], int norm_samples)
{

        int mpi_statRank; // is the same as the spatialRank
        MPI_Comm_rank(coproc_comm, &mpi_statRank);


        vtkMultiPieceDataSet* multiPiece = vtkMultiPieceDataSet::SafeDownCast(VTKGrid->GetBlock(0));
        vtkDataSet* dataSet = vtkDataSet::SafeDownCast(multiPiece->GetPiece(mpi_statRank));

        int x_dom = mpi_statRank%multiXproc;
        int y_dom = (mpi_statRank/multiXproc)%multiYproc;
        int z_dom = mpi_statRank/multiYproc/multiXproc;
        int ntuples = multiXproc*multiYproc*multiZproc*nx*ny*nz;

        if (!dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()))
        {  // Create a field associated with points
                vtkDoubleArray* field_array_mean = vtkDoubleArray::New();
                field_array_mean->SetNumberOfComponents(1);
                field_array_mean->SetNumberOfTuples(ntuples);
                field_array_mean->SetName( (std::string(variable_name)+"_mean").c_str());
                dataSet->GetPointData()->AddArray(field_array_mean);
                field_array_mean->Delete();

        }

        if (!dataSet->GetPointData()->GetArray((std::string(variable_name)+"_var").c_str()))
        {    // Create a field associated with points
                vtkDoubleArray* field_array_var = vtkDoubleArray::New();

                field_array_var->SetNumberOfComponents(1);
                field_array_var->SetNumberOfTuples(ntuples);
                field_array_var->SetName( (std::string(variable_name)+"_var").c_str() );
                dataSet->GetPointData()->AddArray(field_array_var);
                field_array_var->Delete();


        }

        vtkDoubleArray* field_array_mean = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray((std::string(variable_name)+"_mean").c_str()));
        vtkDoubleArray* field_array_var = vtkDoubleArray::SafeDownCast(dataSet->GetPointData()->GetArray( (std::string(variable_name)+"_var").c_str()));

        int localIndex = 0;
        int globalIndex = 0;



// ignoring ghost cells (ngy is number of ghost cells in z direction)
        for (int z = ngz; z < nz + ngz; ++z) {
                // ignoring ghost cells (ngy is number of ghost cells in y direction)
                for (int y = ngy; y < ny + ngy; ++y) {
                        // ignoring ghost cells (ngx is number of ghost cells in x direction)
                        for (int x = ngx; x < nx + ngx; ++x) {

                                localIndex = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                                globalIndex = (nz <2) ? (y-ngy  )*nx + (x -ngx  ) :  (z-ngz)*nx*ny + (y-ngy  )*nx + (x -ngx  );
                                double tmp = avrg_data[localIndex]/double(norm_samples);
                                field_array_mean->SetValue(globalIndex, tmp);
                                tmp = (avrg_sqr_data[localIndex]<1e-10) ? -tmp*tmp : avrg_sqr_data[localIndex]/double(norm_samples) -tmp*tmp;
                                field_array_var->SetValue(globalIndex, tmp);
                                //    std::cout<< tmp<<std::endl;
                        }
                }

        }
        //     std::cout<< " MAX global "<< globalIndex <<" with local "<<localIndex << "with ntuples: "<<ntuples <<std::endl;

}
