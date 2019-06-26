









/home/ramona/MasterthesisLOCAL/coding/alsvinn/build/alsuqcli/alsuqcli














for(int i=0; i<numScripts; i++)
{
        vtkCPPythonScriptPipeline* pipeline =d
                                              vtkCPPythonScriptPipeline::New();
        pipeline->Initialize(scripts[i]);
        Processor->AddPipeline(pipeline);
        pipeline->Delete();
}

const int endTime = std::stoi(my_parameters->getParameter("endTime"));
MyData *my_data = new MyData;
my_data->setEndTimeStep(endTime);



int ns[6]  = {nx,ngx,ny,ngy,nz,ngz};
for (size_t i = 0; i < 6; i++)
        std::cout << ns[i] << ' ';
std::cout<<std::endl; */

std::cout <<"size of vairable data " << sizeof(&variable_data)<<std::endl;



const int maxIndex = nx*ny*nz;     // (nz+ngz-1)*(nx+2*ngx)*(ny+2*ngy)+(ny+ngy-1)*(nx*2*ngx)+(nx+ngx-1); //nx*ny*nz
// Create a field associated with points
vtkDoubleArray* field_array = vtkDoubleArray::New();

field_array->SetNumberOfComponents(1);
field_array->SetNumberOfTuples(maxIndex);
field_array->SetName(variable_name);
std::cout << "h " <<3<< std::endl;
int index = 0;
for (int z = ngz; z < nz + ngz; ++z) {
        // ignoring ghost cells (ngy is number of ghost cells in y direction)
        for (int y = ngy; y < ny + ngy; ++y) {
                // ignoring ghost cells (ngx is number of ghost cells in x direction)
                for (int x = ngx; x < nx + ngx; ++x) {
                        index = z * (nx + 2 * ngx) * (ny + 2 * ngy) + y * (nx + 2 * ngx) + x;
                        field_array->SetValue(index, variable_data[index]);
                        std::cout << "z " <<z<< std::endl;
                        std::cout << "x " <<x<< std::endl;
                        std::cout << "y " <<y<< std::endl;
                        std::cout << "index " <<index<< std::endl;
                }
        }

}
