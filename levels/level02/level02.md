# Level02

- log in into level02 using the flag found in level01: 
    - `su level02`
    - `password: f2av5il02puano7naaf6adaaf`
- `ls` => `level02.pcap`

## What a .pcap file is ?

A .pcap (short for packet capture) file is a common file format used to store network traffic captured by packet sniffing software or hardware. It contains a record of network packets that were intercepted and recorded during data transmission over a network.

Each packet in a .pcap file typically includes various pieces of information such as source and destination IP addresses, port numbers, protocol type (e.g., TCP, UDP), packet size, timestamp, and the actual payload data.

## Important: what packages data fields contain in .pcap?
- In TCP protocol transmissions:
The data field typically contains the payload of the TCP segment. This payload can include application data such as web pages, email content, file transfers, or any other data being transmitted over the TCP connection.
- In other protocols like UDP:
The data field similarly contains the payload of the UDP datagram. This payload can include various types of application data, such as streaming media, DNS queries, or other application-specific data.

=>We have just TCP protocol packages. So maybe sensitive information having been sent, like password !

## Ok we found a .pcap file, let's read it !
- it ends up with not being able to read this file from within the server
- we can prelevate it from our host (or Docker continer) using `scp`protocol, as we do in this [script](scripts/extracting_packages_data_and_decoding.sh)
- once in possesion of the file we can open it and read the packages data fields captured in it with wireshark
(wireshark is not that intuitive. [Here the best tuto playlist we found](https://www.youtube.com/watch?v=OU-A2EmVrKQ&list=PLW8bTPfXNGdC5Co0VnBK1yVzAwSSphzpJ) )
- we find "Password: " in package `No.43`. Bingo !

## Actually we struggled in finding the password, so we went with tshark
- tshark allows to extract the hexadecimal representation of the data fields of all the packages contained in the package capture: `tshark -Tfields -e data -r level02.pcap > captured_data.txt` =>
 [we do that in the script](scripts/extracting_packages_data_and_decoding.sh)
- with the hexadecimal representation we can't do a lot
- so we created a python [script](scripts/print_decoded_data.py) that makes some nice things for us:
    - Read the content of the "captured_data" file
    - Convert hexadecimal string to bytes
    - Decode bytes using ascii encoding and ignoring the error for not valid ascii characters
    ```
    decoded_bytes.decode('ascii', errors='ignore')
'%%&\x18 #\'$&\x18 #\'$ \x01#\x01\'\x01\x18\x01 \x0038400,38400#\x00SodaCan:0\'\x00\x00DISPLAY\x01SodaCan:0\x18\x00xterm\x03\x01"\x1f\x05!\x03\x01""\x03\x01\x00\x00\x03b\x03\x04\x02\x0f\x05\x00\x00\x07b\x1c\x08\x02\x04\tB\x1a\n\x02\x7f\x0b\x02\x15\x0f\x02\x11\x10\x02\x13\x11\x02\x12\x02\x1f\x1f\x00\x001\x05!"\x01\x03"\x01\x07!\x03\x01\x00"\x01\x00""\x03\x03\x03\x04\x0f\x07\x1c\x08\x04\t\x1a\n\x7f\x0b\x15\x0f\x11\x10\x13\x11\x12\r\nLinux 2.6.38-8-generic-pae (::ffff:10.1.1.2) (pts/10)\r\n\n\x01\x00wwwbugs login: l\x00le\x00ev\x00ve\x00el\x00lX\x00X\r\x01\x00\r\nPassword: ft_wandr\x7f\x7f\x7fNDRel\x7fL0L\r\x00\r\n\x01\x00\r\nLogin incorrect\r\nwwwbugs login: 
``` => `Password: ft_wandr\x7f\x7f\x7fNDRel\x7fL0L`    
- \x7f is the DELETE character, even removing it we have "ft_wandrNDRelL0L", that's still not the good password for accessing flag02.
    - and if we consider the DELETE char as its function ? => each time a DELETE char is present we delete the char that is before it. So:
    - let the DELETE(\x7f) char make his job, that is removing the character that is before it
    - isolate the correct password: `ft_waNDReL0L`

Done !



