#include<iostream>
using namespace std;

class Nummy{
public:
    int x = 100;
    int y = 200;
    // operator + denotes num1 + and Nummy nom denotes num2
    Nummy operator  + (Nummy nom) const{

        Nummy new_num  ; //basically num3
        //also nom.x and nom.y are the object passed i.e num2 and num1 is x or y
        new_num.x = x + nom.x;//if num3.x is called
        new_num.y = y + nom.y;//if num3.y is called
        return new_num;
    }
};


int main() {
  Nummy num1,num2;
  //Operator overloading
  Nummy num3 = num1 + num2;
  cout<<num3.x<<" "<<num3.y<<" "<<endl;
    return 0 ;
}