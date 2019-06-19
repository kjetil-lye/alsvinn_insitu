#pragma once
class MyData {
public:

    int getCurrentTimestep() const;
    bool getEndTimestep() const;
    void setCurrentTimestep(int value);
    void setEndTimeStep(int value);

private:
    int currentTimestep = 0;
    int endTimestep= -1;
};

inline int MyData::getCurrentTimestep() const
{
    return currentTimestep;
}
inline bool MyData::getEndTimestep() const
{
    return endTimestep==currentTimestep;
}

inline void MyData::setCurrentTimestep(int value)
{
    currentTimestep = value;
}

inline void MyData::setEndTimeStep(int value)
{
    endTimestep = value;
}
