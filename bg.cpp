#include <iostream>
#include <stdio.h>  // For popen()
#include <string>

extern "C" const char* cmdrun(const char* cmd) {
    static std::string result;
    result.clear();

    FILE* pipe = popen(cmd, "r");
    if (!pipe) return "popen failed!";
    
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe) != nullptr) {
        result += buffer;
    }

    pclose(pipe);
    return result.c_str();
}
