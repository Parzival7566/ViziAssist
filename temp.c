#include "stdio.h"
#include "unistd.h"
#include "stdlib.h"

float gputemp = 0;
float cputemp = 0;
int count = 0;

int main() {
    char* cpu;
    char* gpu;
    cpu = (char*)malloc(sizeof(char)*6);
    gpu = (char*)malloc(sizeof(char)*6);
    

    while (1) {
        FILE* fcputemp = fopen("/sys/devices/virtual/thermal/thermal_zone1/temp", "r");
        FILE* fgputemp = fopen("/sys/devices/virtual/thermal/thermal_zone2/temp","r");
        if (!fcputemp || !fgputemp ) {
            printf("Something went wrong\n");
            exit(EXIT_FAILURE);
        }
        
        cputemp = atoi(fgets(cpu, 6, fcputemp))/1000;
        gputemp = atoi(fgets(gpu, 6, fgputemp))/1000;
        
        printf("\rCpu : %.2f, Gpu : %.2f. Elapsed time : %d", cputemp, gputemp, count);
        fflush(stdout);
        
        fclose(fcputemp);
        fclose(fgputemp);
        
        count++;
        sleep(1);
    }
}
