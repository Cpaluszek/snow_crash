FROM kalilinux/kali-rolling

RUN apt-get update && apt-get install curl john -y

RUN mkdir -p /password_list \
  && curl -k https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt -o /password_list/10-million-password-list-top-10000.txt

CMD ["bash"]