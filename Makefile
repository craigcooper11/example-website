run: clean
	podman-compose up -d

clean:
	podman-compose down
	podman rmi -a -f