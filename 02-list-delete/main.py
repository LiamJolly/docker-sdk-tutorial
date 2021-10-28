import sys
from typing import List

import docker
from docker.errors import NotFound
from docker.models.containers import Container


class DockerManager:
    def __init__(self):
        self.client = docker.client.from_env()

    def list_containers(self) -> List[Container]:
        return self.client.containers.list(all=True)

    def list_container_names(self) -> List[str]:
        container_names = []
        container: Container
        for container in self.list_containers():
            container_names.append(container.name)
        return container_names

    def get_container_by_name(self, name) -> Container:
        return self.client.containers.get(name)

    def remove_container(self, name):
        container: Container = self.get_container_by_name(name)
        container.remove()


if __name__ == "__main__":
    docker_manager = DockerManager()
    print("The following containers are running:")
    for container_name in docker_manager.list_container_names():
        print(container_name)
    container_name = input("Please type the name of the container you wish to delete:")
    try:
        if not container_name:
            sys.exit()
        docker_manager.remove_container(container_name)
        print(f"Removed {container_name}")
        print("The following containers are running:")
        for container_name in docker_manager.list_container_names():
            print(container_name)
    except NotFound:
        print(f"Container {container_name} does not exist")
