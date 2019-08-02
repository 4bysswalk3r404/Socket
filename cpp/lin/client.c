#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#define PORT 3705

void Input(char* buffer)
{
    char c;
    void* BufferStart = buffer;
    while(c = getchar())
    {
        if ((c == '\n') || (c == '\0')) {
            *buffer = '\0';
            break;
        } else {
            *buffer = c;
            buffer++;
        }
    }
    buffer = BufferStart;
}

void ProtoChange(char* buffer, char* protocol)
{
    if ((buffer[0] == 'u') && (buffer[1] == 's') && (buffer[2] == 'e'))
    {
        if (buffer[4] == 's' && buffer[5] == 't' && buffer[6] == 't' && buffer[7] == 'r' && buffer[8] == 'i' && buffer[9] == 'n' && buffer[10] == 'g')
            protocol = "string";
        else if (buffer[4] == 'f' && buffer[5] == 'i' && buffer[6] == 'l' && buffer[7] == 'e')
            protocol = "file";
    }
}

int main(int argc, char const *argv[])
{
    int sock = 0, valread;
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

    char* protocol = "string";

    char* Sending = (char*)malloc(sizeof(char) * 1024);
    void* SendingStart = Sending;

    while (1)
    {
        printf("(%s)", protocol);

        Input(Sending);
        Sending = SendingStart;
        ProtoChange(Sending, protocol);

        send(sock, Sending, strlen(Sending), 0);
        memset(Sending, 0, sizeof(Sending));
    }
    return 0;
}
