#include "Test.hpp"

void* list_files(const char* path){
  vector<string>* paths = new vector<string>();
  for(auto& file : recursive_directory_iterator(path)){
      if(file.is_regular_file()){
          paths->push_back(file.path().string());
      }
  }
  return static_cast<void*>(paths);
}

const char* get_data(void* v, int idx){
    return ((vector<string>*)(v))->at(idx).c_str();
}

int size(void* v){
    return ((vector<string>*)(v))->size();
}

int sum(int a,int b){
  return a + b;
}
void func(){
  std::cout << "Hello" << '\n';
}
