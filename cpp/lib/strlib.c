#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>

int StrSize(char* buffer)
{
    int i;
    for (i = 0; *buffer != '\0'; i++)
        buffer++;
    return i;
}

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

void SetStr(char* from, char* to)
{
    void* FromStart = from;
    int _strlen = StrSize(to);
    for (int i = 0; i < _strlen; i++)
    {
        *from = *to;
        from++;
        to++;
    }
    *from = '\0';
    from = FromStart;
}

int SameStr(char* base, char* sub, int num)
{
    int same = 0;
    for (int i = 0; i < num; i++)
    {
        if (*base == *sub)
            same++;
        base++;
        sub++;
    }
    if (same == num)
        return 1;
    return 0;
}
