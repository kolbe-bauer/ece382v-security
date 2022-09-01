#include <netinet/in.h> //structure for storing address information
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h> //for socket APIs
#include <sys/types.h>
#include <arpa/inet.h>

int main(int argc, char const* argv[])
{
	int serverSocket = socket(AF_INET, SOCK_STREAM, 0);

	// define server address
	struct sockaddr_in servAddr, clinAdder;

	servAddr.sin_family = AF_INET;
	servAddr.sin_port = htons(12000);
	servAddr.sin_addr.s_addr = inet_addr("127.0.0.2");

	// bind socket to the specified IP and port
	bind(serverSocket, (struct sockaddr*)&servAddr, sizeof(servAddr));
    printf("The server is ready to receive\n");

    while(1){
        // listen for connections
        listen(serverSocket, 5);

        // integer to hold client socket.
        int len = sizeof(clinAdder);
        int connectionSocket = accept(serverSocket, (struct sockaddr*)&clinAdder, &len);
        // printf("New socket connection %d\n",connectionSocket);

        // get string from client
		char sentence[1024];
        recv(connectionSocket, sentence, sizeof(sentence), 0);
        // printf("Print the following sentence:\n");
        // printf("%s\n",sentence);

        //convert sentence to upper case
        char serMsg[1024];
        int i;
        for (i = 0; sentence[i]!='\0'; i++) {
            if(sentence[i] >= 'a' && sentence[i] <= 'z') {
                serMsg[i] = sentence[i] - 32;
            }else{
                serMsg[i] = sentence[i];
            }
        }
        // printf("New sentence:\n%s\n",serMsg);

        //return sentence
        send(connectionSocket, serMsg, strlen(serMsg), 0);
    }

	return 0;
}
