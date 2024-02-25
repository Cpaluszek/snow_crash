#!/bin/bash

GREEN='\033[92m'
RESET='\033[0m'

scp -P 4242 level02@$IP_ADDRESS:~/level02.pcap .

echo -e "${GREEN}Capturing data from packet capture file and saving them${RESET}"
tshark -Tfields -e data -r level02.pcap > captured_data.txt
sleep 2

echo -e "${GREEN}Launching python script to decode and isolate password${RESET}"
python3 print_decoded_data.py
sleep 2
