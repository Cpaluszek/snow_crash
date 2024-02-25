# Level02

- log in into level02 using the flag found in level01: 
    - `su level02`
    - `password: f2av5il02puano7naaf6adaaf`
- `ls` => `level02.pcap`

## What a .pcap file is ?

## Ok we found a .pcap file, let's read it !
- it ends up with not being able to read this file from within the server
- we can prelevate it from our host (or Docker continer) using `scp`protocol, as we do in this [script](scripts/extracting_packages_data_and_decoding.sh)
- once in possesion of the file we can open it and read the packages data fields captured in it with wireshark
(wireshark is not that intuitive. [Here the best tuto playlist we found](https://www.youtube.com/watch?v=OU-A2EmVrKQ&list=PLW8bTPfXNGdC5Co0VnBK1yVzAwSSphzpJ) )
- we find "Password: " in package `No.43`

## Actually we struggled in finding the password, so we went with tshark
- tshark allows to extract the hexadecimal representation of the data fields of all the packages contained in the package capture: `tshark -Tfields -e data -r level02.pcap > captured_data.txt` =>
 [we do that in the script](scripts/extracting_packages_data_and_decoding.sh)
- with the hexadecimal representation we can't do a lot
- so we created a python [script](scripts/print_decoded_data.py) that makes some nice things for us:
    - Read the content of the "captured_data" file
    - Convert hexadecimal string to bytes
    - Decode bytes using ascii encoding and ignoring the error for not valid ascii characters
    - Print the decoded string containing the password "ft_wandrNDRelL0L" => still not the good password for accessing flag02
    - let the DELETE(\x7f) char make his job, that is removing the character that is before it
    - isolate the correct password



