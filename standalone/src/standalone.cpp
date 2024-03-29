#include <iostream>
#include <dll_adaptor.hpp>
#include <netcdf.h>
#include <sstream>
#include <exception>
#include <vector>
#include <map>

struct DataField {

        std::string name = "not set";
        size_t nx{1};
        size_t ny{1};
        size_t nz{1};
        double ax = 0, ay = 0, az = 0;
        double bx = 1, by = 1, bz = 1;
        std::vector<double> data;
};

#define NETCDF_SAFE_CALL(x) { \
                auto error = x; \
                if (error!=NC_NOERR) { \
                        std::stringstream error_message; \
                        error_message << "NetCDF error in call to\n\t" << #x << "\n\nError code: " << error \
                                      << "\n\nError message: " << nc_strerror(error); \
                        throw std::runtime_error(error_message.str()); \
                } \
}

//to mimic simulation
std::vector<DataField> read_file(const std::string& file_name) {
        std::vector<DataField> datafields;

        int file;

        std::cout << file_name << std::endl;
        NETCDF_SAFE_CALL(nc_open(file_name.c_str(), NC_NOWRITE, &file));

        int number_of_variables;
        NETCDF_SAFE_CALL(nc_inq_nvars(file, &number_of_variables));

        std::vector<int> variable_ids(number_of_variables, -42);

        NETCDF_SAFE_CALL(nc_inq_varids(file, &number_of_variables,
                                       variable_ids.data()));


        for (int varid : variable_ids) {
                //std::cout << "varid " << varid << std::endl;
                std::vector<char> name_vector(NC_MAX_NAME, 0);

                NETCDF_SAFE_CALL(nc_inq_varname(file, varid, name_vector.data()));

                std::string name(name_vector.data());

                if (name == "time") {
                        continue;
                }


                datafields.push_back(DataField());

                auto& field = datafields.back();

                field.name = name;

                int number_of_dimensions = 1;
                NETCDF_SAFE_CALL(nc_inq_varndims(file, varid, &number_of_dimensions));

                std::vector<int> dimension_ids(number_of_dimensions, 0);

                NETCDF_SAFE_CALL(nc_inq_vardimid(file, varid, dimension_ids.data()));

                std::vector<size_t> v_len(number_of_dimensions, 1);

                for (int dim = 0; dim < number_of_dimensions; ++dim) {
                        NETCDF_SAFE_CALL(nc_inq_dimlen(file, dimension_ids[dim], &v_len[dim]));
                }

                size_t total_size = 1;

                for (size_t l : v_len) {
                        total_size *= l;
                }

                field.data.resize(total_size, 0.0);

                NETCDF_SAFE_CALL(nc_get_var_double(file, varid, field.data.data()));

                field.nx = v_len[0];

                if (number_of_dimensions > 1) {
                        field.ny = v_len[1];
                }

                if (number_of_dimensions > 2) {
                        field.nz = v_len[2];
                }

        } //end for over variables ids

        NETCDF_SAFE_CALL(nc_close(file));

        return datafields;
}//end read_file


int main(int argc, char** argv) {
        if (argc < 2) {
                std::cout << "Usage: \n\t" << argv[0] << " <filename.nc>  <pipelinescript.py> \n";
                return EXIT_FAILURE;
        }
        const double endTime = 0.1;
        std::string stmp = std::to_string(endTime);
        char const *end_time = stmp.c_str();


        MPI_Init(NULL, NULL);
        const std::string file_name = argv[1];
        auto fields = read_file(file_name);

        std::cout << "read file" << std::endl;
//initialized paramaters as a "MyParameters" object,  writer
        auto parameters = make_parameters();
        set_parameter(parameters, "basename", "standalone_base");
        set_parameter(parameters, "pipelineScript", "/home/ramona/MasterthesisLOCAL/coding/alsvinn_insitu/scripts/gridwriter.py");
        set_parameter(parameters, "endTime", end_time);

        //create returns a myData object
        auto data = create("standalone", "v0.0.1", parameters);

        //setup communictaion /(defines mpiComm=MPI_COMM_WORLD (communication between all processes) in MyParameters)
        set_mpi_comm(data, parameters, MPI_COMM_WORLD);


        int timeStep= 0;
        double time = timeStep * 0.1;

        while(time <endTime)
        {
                // use a time step length of 0.1
                timeStep += 1;
                time = timeStep * 0.1;

                new_timestep(data, parameters,time, timeStep);
                std::cout << timeStep << std::endl;
                std::cout << "size of fields: " << fields.size() << std::endl;

                for (auto& field : fields) {
                        std::cout<<"name of field: " <<field.name<<std::endl;
                        //    std::cout<<"infields"<<std::endl;
                        CatalystCoProcess(data,
                                          parameters,
                                          time,
                                          field.name.c_str(),
                                          field.data.data(),
                                          field.nx,
                                          field.ny,
                                          field.nz,
                                          0,
                                          0,
                                          0,
                                          field.ax,
                                          field.ay,
                                          field.az,
                                          field.bx,
                                          field.by,
                                          field.bz,
                                          -1);

                }

                end_timestep(data, parameters, time, timeStep);
        }


        delete_parameters(parameters);
        delete_data(data);
        MPI_Finalize();


        return EXIT_SUCCESS;
}
