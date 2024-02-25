# snow_crash

## How to run the project

- update the `IP_ADDRESS`in the `Dockerfile`
- `docker build -t kali .`
- `docker run -it --rm --name kali kali`

## How to access the snow_crash server from within the Docker container
- `ssh level00@$IP_ADDRESS -p 4242`

## How to run the scripts for the levels requiring that
- `/root/levels`

## Levels
- [level00](./levels/level00/level00.md)
- [level01](./levels/level01/level01.md)
- [level02](./levels/level02/level02.md)
- [level03](./levels/level03/level03.md)
- [level04](./levels/level04/level04.md)
