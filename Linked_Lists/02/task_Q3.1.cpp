#include<iostream>
using namespace std;

class House{
protected:
    string fam_house ;
public:
    void house (string name){
        fam_house = name;
    }
    void house(){
        fam_house = "Snow";
    }
};

class North:public House{
public:
    void Name_House(){
        cout<<"I am Jon of house "<<fam_house<<endl;
    }

};
class South:public House{
public:
    void Name_House(){
        cout<<"I am Cersie of house "<<fam_house<<endl;
    }

};

int main() {
    North h;
    South s;
    House *name1 = &h;
    House *name2 = &s;
    //accesing function from house function from House class
    name1->house("Targaryen");
    h.Name_House();
    name1->house();//Function Overloading
    h.Name_House();
    name2->house("Lannister");
    s.Name_House();
    return 0 ;
}