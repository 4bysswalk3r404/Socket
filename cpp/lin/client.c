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
    int sock = 0;
    struct sockaddr_in serv_addr;
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, argv[1], &serv_addr.sin_addr) <= 0)
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }

    char* protocol = (char*)malloc(sizeof(char) * 10);
    SetStr(protocol, "string");

    char* Sending = (char*)malloc(sizeof(char) * 1024);
    void* SendingStart = Sending;

    send(sock, argv[1], 18, 0);

    while (1)
    {
        printf("(%s)", protocol);

        Input(Sending);
        Sending = SendingStart;

        if (SameStr(Sending, "use", 3))
        {
            Sending = SendingStart + 4;
            if (SameStr(Sending, "string", 6)) {
                SetStr(protocol, "string");
            } else if (SameStr(Sending, "file", 4)) {
                SetStr(protocol, "file");
            }
        }
        Sending = SendingStart;

        if (SameStr(protocol, "string", 6)) {
            send(sock, "\1", 1, 0);
            send(sock, Sending, strlen(Sending), 0);
        } else if (SameStr(protocol, "file", 4)) {
            send(sock, "\2", 1, 0);
            send(sock, Sending, strlen(Sending), 0);
        }
        memset(Sending, 0, sizeof(Sending));
    }
    return 0;
}
