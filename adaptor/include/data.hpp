#pragma once
class MyData {
public:

int getCurrentTimestep() const;
bool isEndTimestep() const;
bool isNewTimestep() const;
bool isNewVariable(const std::string new_name);

void setCurrentTimestep(int value);
void setEndTimeStep(bool value);
void setNewTimestep(bool nt);



private:
int currentTimestep = 0;
bool endTime= false;
bool newTimstep = true;
std::string var_name = "none";
};

inline int MyData::getCurrentTimestep() const
{
        return currentTimestep;
}
inline bool MyData::isEndTimestep() const
{
        return endTime;
}

inline void MyData::setCurrentTimestep(int value)
{
        currentTimestep = value;
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
                var_name= new_name;
                return true;
        }
}
