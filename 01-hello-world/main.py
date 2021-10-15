import docker


def run_container():
    client = docker.client.from_env()
    client.containers.run("busybox:latest", "echo Hello World!", name="tutorial1")


if __name__ == "__main__":
    run_container()
