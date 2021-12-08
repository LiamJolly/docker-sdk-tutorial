from docker.models.networks import Network
from docker.models.volumes import Volume

from docker_manager import DockerManager

if __name__ == "__main__":
    docker_manager = DockerManager()
    network_name = "test_network"
    volume_name = "test_volume"
    container_name = "test_container"
    print("Creating network")
    docker_manager.create_network(network_name)
    print("Created network")
    print("Networks:")
    network: Network
    for network in docker_manager.get_networks():
        print(network.name)
    print("Creating volume")
    docker_manager.create_volume(volume_name)
    print("Created volume")
    print("Volumes:")
    volume: Volume
    for volume in docker_manager.get_volumes():
        print(volume.name)
    print("Creating container")
    docker_manager.run_container("busybox", name=container_name, command="echo Hello world!",
                                 volume_name=volume_name, bind="/opt/test", network_name=network_name, detach=False)
