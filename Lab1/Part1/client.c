#include <netinet/in.h> //structure for storing address information
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h> //for socket APIs
#include <sys/types.h>
#include <arpa/inet.h>

int main(int argc, char const* argv[])
{
	int clientSocket = socket(AF_INET, SOCK_STREAM, 0);

	struct sockaddr_in servAddr;

	servAddr.sin_family = AF_INET;
	servAddr.sin_port = htons(12000);
	servAddr.sin_addr.s_addr = inet_addr("127.0.0.2");

	int connectStatus = connect(clientSocket, (struct sockaddr*)&servAddr, sizeof(servAddr));

	if (connectStatus == -1) {
		printf("Error...\n");
	}

	else {
        char* sentence = "Input lowercase sentence:";
		char modified[1024];

		send(clientSocket, sentence, strlen(sentence), 0);
        recv(clientSocket, modified, sizeof(modified), 0);

		printf("From Server: %s\n", modified);
	}

	return 0;
}
