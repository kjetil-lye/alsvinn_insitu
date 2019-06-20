#pragma once
#include <string>
#include <map>
#include <mpi.h>
#include<exception>
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
        std::cerr<<"warning: no pipeline script"<<std::endl;
        }else{
          out= parameters.at(key);
        }

        return out;
    }

    void setMPIComm(MPI_Comm comm) {
        mpiComm = comm;
    }


    MPI_Comm getMPIComm(MPI_Comm comm) {
        return comm;
    }

private:
    std::map<std::string, std::string> parameters;

    MPI_Comm mpiComm;

};
