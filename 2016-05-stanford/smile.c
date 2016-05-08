#include <unistd.h>
#include <stdio.h>

int main() {
    while(1) {
        printf(":) ");
        fflush(stdout);
        sleep(1);
    }
}
