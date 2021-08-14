#pragma once
#include <iostream>
#include <filesystem>
#include <string>
#include <vector>
#include <cstring>

using std::vector;
using std::string;
using std::filesystem::recursive_directory_iterator;
using std::filesystem::directory_iterator;

#ifdef __cplusplus
  extern "C"{
#endif
void func();
int sum(int,int);
void* list_files(const char*);
const char* get_data(void* vec, int);
int size(void* v);

#ifdef __cplusplus
}
#endif
