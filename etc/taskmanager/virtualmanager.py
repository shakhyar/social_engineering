from virtualhost import *

#TODO: To make changes in the virtualhost program, because when I request for other id than 1, it returns None, but they have been entered earlier
#TODO: Make the virutal engine fully functional by adding a manager class
#TODO: Add all methods like:
#? To get server name and description to show in their own notebook home page
#? To take entry for new notebook
#TODO: To finally get the whole module function, perform test

#! Not completed yet / Not for deployment


vManager = VirtualUnit()
vManager.create_table(True)
#vManager.data_entry(1, "myserver1", "mydescription1", 1)
#vManager.data_entry(2, "myserver2", "mydescription2", 2)
#vManager.data_entry(3, "myserver3", "mydescription3", 3)
print(vManager.get_virtual_host_id(0))

class VManagement:
    def __init__(self):
        pass


    def verify_if_server_exists(self, id):
        if vManager.get_virtual_host_id(id):
            print("Server found")

        else:
            print("Server not found")

fc = VManagement()

print(vManager.read(-10))