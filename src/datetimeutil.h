#pragma once

#ifdef WIN32
  #define HELLO_EXPORT __declspec(dllexport)
#else
  #define HELLO_EXPORT
#endif

#include <time.h>
#include <string>

HELLO_EXPORT char* time_to_string(tm* time, std::string pattern);
