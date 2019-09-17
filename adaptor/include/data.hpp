#pragma once
class MyData {
public:

int getCurrentTimestep() const;
double getCurrentTime() const;
bool isEndTimestep() const;
bool isNewTimestep() const;
bool isNewVariable(const std::string new_name);
void setNewVariable(const std::string new_name);
void setCurrentTimestep(int value);
void setCurrentTime(double value);
void setEndTimeStep(bool value);
void setNewTimestep(bool nt);



private:
int currentTimestep = 0;
double currentTime =0.0;
bool endTime= false;
bool newTimstep = true;
std::string var_name = "none";
};

inline int MyData::getCurrentTimestep() const
{
        return currentTimestep;
}

inline double MyData::getCurrentTime() const
{
        return currentTime;
}


inline bool MyData::isEndTimestep() const
{
        return endTime;
}

inline void MyData::setCurrentTimestep(int value)
{
        currentTimestep = value;
}

inline void MyData::setCurrentTime(double value)
{
        currentTime = value;
}


inline void MyData::setEndTimeStep(bool value)
{
        endTime = value;
}

inline bool MyData::isNewTimestep() const
{
        return newTimstep;
}

inline void MyData::setNewTimestep(bool nt)
{
        newTimstep = nt;
}

inline bool MyData::isNewVariable(const std::string new_name)
{
        if (var_name == new_name) {
                return false;
        }else{
              //  var_name= new_name;
                return true;
        }
}

inline void MyData::setNewVariable(const std::string new_name)
{
      var_name= new_name;
}
