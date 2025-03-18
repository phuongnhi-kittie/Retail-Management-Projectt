class Employee:
    def __init__(self, id ,name, phone, designation, address, username, password):
        self.id = id
        self.name = name
        self.phone = phone
        self.designation = designation
        self.address = address
        self.username = username
        self.password = password
    def echo_password(self):
        return "*"*len(self.password)
    def __str__(self):
        info = f"Information of Employee: \n +id: {self.id} \n +name: {self.name} \n +phone: {self.phone} \n +designation: {self.designation} \n +address: {self.address} \n +username: {self.username} \n + password: {self.password}"
        return info