# Shared Docker Volumes 

`data/input.txt` is read inside the container -- container produces `output.txt` -- accessible via host OS

```
$ docker build -t foo-bar . 
$ docker run -d -v ~/git/spike-docker-volumes/data:/data foo-bar
```
