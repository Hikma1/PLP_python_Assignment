# week5_classes.py

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def info(self):
        return f"{self.brand} {self.model}"

# Derived class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)   # Call the parent constructor
        self.os = os
        self.storage = storage
    
    def call(self, number):
        print(f"📞 Calling {number} using {self.brand} {self.model}...")
    
    def install_app(self, app_name):
        print(f"⬇️ Installing {app_name} on {self.brand} {self.model}...")
    
    def info(self):
        # Polymorphism: redefining the parent method
        return f"{self.brand} {self.model} ({self.os}, {self.storage}GB)"


# --- Main Program ---
if __name__ == "__main__":
    phone1 = Smartphone("Apple", "iPhone 15", "iOS", 256)
    phone2 = Smartphone("Samsung", "Galaxy S24", "Android", 512)
    
    print(phone1.info())
    phone1.call("123-456-789")
    phone1.install_app("WhatsApp")
    
    print(phone2.info())
    phone2.call("987-654-321")
