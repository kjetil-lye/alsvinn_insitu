#pragma once
#include <string>
#include <map>
#include <mpi.h>
#include <exception>
#include <iostream>
//! Simple example parameter class that can be used
class MyParameters {
public:

void setParameter(const std::string& key, const std::string& value) {
        parameters[key] = value;
}

std::string getParameter(const std::string& key) const {
        std::string out ="none";
        if ( parameters.find(key) == parameters.end() ) {
                std::cerr<<"! warning: missing parameter: "<<key <<std::endl;
        }else{
                try{
                        out= parameters.at(key);
                }catch(const std::exception& e) {
                        std::cerr<<"in get_parameter: caught exception: "<< e.what()<<std::endl;
                }
        }

        return out;
}

void setMPIComm(MPI_Comm comm) {
        mpiComm = comm;
}


MPI_Comm getMPIComm() {
        return mpiComm;
}
MPI_Comm* getMPICommPtr() {
        return &mpiComm;
}


private:
std::map<std::string, std::string> parameters;


MPI_Comm mpiComm;


};
