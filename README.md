# snow_crash

## How to run the project

- update the `IP_ADDRESS`in the `Dockerfile`
- `docker build -t kali .`
- `docker run -it --rm --name kali kali`

## How to access the snow_crash server from within the Docker container
- `ssh level00@$IP_ADDRESS -p <ssh_port>`
Level00 password: `level00`

## How to run the scripts for the levels requiring that
- `/root/levels`

## Levels
- [level00](./levels/level00/level00.md)
- [level01](./levels/level01/level01.md)
- [level02](./levels/level02/level02.md)
- [level03](./levels/level03/level03.md)
- [level04](./levels/level04/level04.md)
- [level05](./levels/level05/level05.md)
- [level06](./levels/level06/level06.md)
- [level07](./levels/level07/level07.md)
- [level08](./levels/level08/level08.md)
- [level09](./levels/level09/level09.md)
