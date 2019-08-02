#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include "../lib/strlib.h"
#define PORT 3705

int main(int argc, char const *argv[])
{
    int server_fd, new_socket;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 8080
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                                                  &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_port = htons( PORT );

    if(inet_pton(AF_INET, argv[1], &address.sin_addr) <= 0)
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address,
                                 sizeof(address))<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address,
                       (socklen_t*)&addrlen))<0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    int valread;
    unsigned char lowProtocol;
    char InBuffer[1024] = {0};

    read(new_socket, InBuffer, 18);
    printf("%s\n", InBuffer);

    while (1)
    {
        if (!(read(new_socket, &lowProtocol, 1))) {
            printf("Connection broken 1\n");
            exit(EXIT_FAILURE);
        }
        if (!(read(new_socket, InBuffer, 1024))) {
            printf("Connection broken 2\n");
            exit(EXIT_FAILURE);
        }
        if (lowProtocol == '\1') {
            printf("(string)%s\n", InBuffer);
        } else if (lowProtocol == '\2') {
            printf("(file)%s\n", InBuffer);
        }
        memset(InBuffer, 0, sizeof(InBuffer));
    }

    return 0;
}
