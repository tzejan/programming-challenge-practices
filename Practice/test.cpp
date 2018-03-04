#include <iostream>

int main()
{
    bool cond1, cond2;

    cond1 = true;
    cond2 = true;

    // some code to modify values of cond1 and cond2

    if ((cond1 == cond2) && (cond1 == true) && (cond2 != false))
    {
        std::cout << "woo";
    }
    return 0;
}