from docker.models.networks import Network

from docker_manager import DockerManager

if __name__ == "__main__":
    NETWORK_NAME = "TestNetwork"
    docker_manager = DockerManager()
    print("Creating network...")
    docker_manager.create_network(NETWORK_NAME)
    print("List all networks...")
    network: Network
    for network in docker_manager.get_networks():
        print(network.name)
    print("Removing network...")
    docker_manager.remove_network(NETWORK_NAME)
    print("List all network...")
    for network in docker_manager.get_networks():
        print(network.name)
