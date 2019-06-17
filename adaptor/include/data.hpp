#pragma once
class MyData {
public:

    int getCurrentTimestep() const;
    bool getEndTimestep() const;
    void setCurrentTimestep(int value);
    void setEndTimestep(bool value);

private:
    int currentTimestep = 0;
    bool endTimestep= false;
};

inline int MyData::getCurrentTimestep() const
{
    return currentTimestep;
}
inline bool MyData::getEndTimestep() const
{
    return endTimestep;
}

inline void MyData::setCurrentTimestep(int value)
{
    currentTimestep = value;
}

inline void MyData::setEndTimestep(bool value)
{
    endTimestep = value;
}
