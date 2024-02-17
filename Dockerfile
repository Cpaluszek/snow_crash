FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install john -y

CMD ["bash"]