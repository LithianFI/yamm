import os
from mod import Mod


class Yamm:
    running = True
    mods_list = []

    def __init__(self):
        try:
            self.mods_folder = os.getcwd() + '/test'
            print("Mods folder found in " + self.mods_folder)
            mods_in_directory = os.listdir(self.mods_folder)
            for d in mods_in_directory:
                new_mod = Mod(d, 1, self.mods_folder + '/' + d)
                self.mods_list.append(new_mod)
                print(new_mod.name + ', ' + str(new_mod.priority) + ', ' + new_mod.path)
        except ValueError:
            print("Mods folder not found")

    def list_mods(self):
        print("Mods Listed")

    def monitor_folder(self):
        while self.running == True:
            return


if __name__ == "__main__":
    Yamm().list_mods()
