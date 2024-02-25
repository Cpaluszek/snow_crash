FROM kalilinux/kali-rolling

# TODO: set the correct IP address depending on the one dispayed in snow_crash iso
ENV IP_ADDRESS=172.16.197.128

RUN apt-get update && apt-get install john python3 openssh-client wireshark tshark -y

RUN mkdir -p /root/levels
COPY ./levels /root/levels
RUN chmod -R +x /root/levels/*

CMD ["bash"]