from docker.models.volumes import Volume

from docker_manager import DockerManager

if __name__ == "__main__":
    VOLUME_NAME = "TestVolume"
    docker_manager = DockerManager()
    print("Creating volume...")
    docker_manager.create_volume(VOLUME_NAME)
    print("List all volumes...")
    volume: Volume
    for volume in docker_manager.list_volumes():
        print(volume.name)
    print("Removing volume...")
    docker_manager.remove_volume(VOLUME_NAME)
    print("List all volumes...")
    for volume in docker_manager.list_volumes():
        print(volume.name)
