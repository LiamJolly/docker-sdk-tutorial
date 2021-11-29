from typing import List

import docker
from docker.models.containers import Container
from docker.models.networks import Network
from docker.models.volumes import Volume


class DockerManager:
    def __init__(self):
        self.client = docker.client.from_env()

    def get_containers(self) -> List[Container]:
        """
        List all containers
        :return: a list of containers
        """
        return self.client.containers.list(all=True)

    def get_container_by_name(self, name) -> Container:
        """
        Find a container by its name
        :param name: the container name to look for
        :return: the required container
        """
        return self.client.containers.get(name)

    def remove_container(self, name):
        """
        Remove a container by its name
        :param name: The name of the container to remove
        """
        self.get_container_by_name(name).remove()

    def create_volume(self, name, driver="local", driver_opts=None, labels=None) -> Volume:
        """
        Create a volume
        :param name: The name of the volume
        :param driver: The type of driver to use
        :param driver_opts: Additional options
        :param labels: Labels for the volume
        :return: The created Volume
        """
        if driver_opts is None:
            driver_opts = {}
        if labels is None:
            labels = {}
        return self.client.volumes.create(name=name, driver=driver, driver_opts=driver_opts, labels=labels)

    def get_volume(self, volume_name) -> Volume:
        """
        Get a volume by name
        :param volume_name: The volume name to find
        :return: An instance of the volume
        """
        return self.client.volumes.get(volume_name)

    def get_volumes(self) -> List[Volume]:
        """
        List all available volumes
        :return: a list of volumes
        """
        return self.client.volumes.list()

    def remove_volume(self, volume_name):
        """
        Remove the volume with the given name
        :param volume_name: The name of the volume to remove
        """
        self.get_volume(volume_name).remove()

    def get_networks(self) -> List[Network]:
        return self.client.networks.list()

    def get_network(self, network_id) -> Network:
        return self.client.networks.get(network_id=network_id)

    def create_network(self, name) -> Network:
        return self.client.networks.create(name)

    def remove_network(self, network_id):
        self.get_network(network_id).remove()
