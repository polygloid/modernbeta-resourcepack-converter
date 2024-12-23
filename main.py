import os
import shutil

def copy_textures(file_map, base_directory='.'):
        
        for file1, file2 in file_map.items():
            # construct full paths for source and output files
            full_file1 = os.path.join(base_directory, file1)
            full_file2 = os.path.join(base_directory, file2)
            print(full_file1)
            print(full_file2)

        for file1, file2 in file_map.items():
            try:
                # check if it exists
                if not os.path.exists(full_file1):
                    print(f"Source file not found. Skipping...")

                if os.path.exists(full_file2):
                    os.remove(full_file2)
                    print(f"Deleted file {full_file2}")

                shutil.copy(full_file1,full_file2)
                print(f"Copied and renamed '{file1}' to '{file2}'")
            except Exception as imaginegettingerrors:
                print(f"Error processing {file1} -> {file2}: {imaginegettingerrors}")

item_file_map = {
    "apple.png": "magma_cream.png",
    "golden_apple.png":"glistering_melon_slice.png",
    "mushroom_soup.png": "blaze_rod.png",
    "bread.png": "nautilus_shell.png",
    "porkchop.png":"nether_brick.png",
    "cod.png": "rabbit_foot.png",
    "cooked_cod.png": "rabbit_hide.png",
    "bow.png": "iron_horse_armor.png"
}

block_file_map = {
}

if __name__ == "__main__":
    resource_pack = input("Resource pack name: ")
    new_resource_pack = resource_pack + "_modernbeta"

    while True: # create new pack from old one, if already exists ask user if they want to replace it
        if not os.path.exists(new_resource_pack):
            shutil.copytree(resource_pack,new_resource_pack)
            break
        else:
            delete_copy = input(f"{new_resource_pack} already exists. Replace? (y/N): ").strip().lower()
            if delete_copy and delete_copy[0] == "y": # makes sure delete copy exists aswell
                shutil.rmtree(new_resource_pack)
                print("Old pack removed")
            else:
                print("Cancelled operation (coward)")
                break

    # me omw to force users to put the resource pack over the server resources instead
    # of letting them use it standalone
    remove_paths = [f"{new_resource_pack}\\assets\\minecraft\\blockstates",
                    f"{new_resource_pack}\\assets\\minecraft\\lang",
                    f"{new_resource_pack}\\assets\\minecraft\\models"]
    for path in remove_paths:
        shutil.rmtree(path)
        print(f"Removed {path}")
    

    copy_textures(item_file_map, f"{new_resource_pack}\\assets\\minecraft\\textures\\item")
    #copy_textures(block_file_map, f"{new_resource_pack}\\assets\\minecraft\\textures\\block")