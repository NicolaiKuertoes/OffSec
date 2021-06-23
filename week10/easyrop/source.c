#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main() {
	char buf[32];
	
    setvbuf(stdin, 0, _IONBF, 0);
    setvbuf(stdout, 0, _IONBF, 0);
    
	puts("Welcome to the echo service 2.0!");
    printf("printf is at %p\n", printf);
	while(*buf != '\n') {
		read(STDIN_FILENO, buf, 1024);
		puts(buf);
	}
	
	return 0;
}
