# Open your VS code and import socket module.
# The socket module provides various objects, constants, functions and related exceptions for building full-fledged network applications including client and server programs.

Program:-
  
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname (hostname)
print("my IP address is:" + IPAddr)
