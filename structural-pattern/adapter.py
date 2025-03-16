class LegacyApp:
    def process_data(self):
        return "LegacySystem: processing data and uploading formatted data..."
class ModernApp:
    def transform_data(self):
        return "ModernSystem: transforming data and uploading formatted data..."
class ProblematicClientCode:
    def __init__(self,app):
        self.app=app
    def main(self):
        # only supports modern app
        self.app.transform_data()

class LegacyAppAdapterObjectComposition(ModernApp):
    def __init__(self,legacy_app: LegacyApp) -> None:
        self.legacy_app = legacy_app
    def transform_data(self):
        return self.legacy_app.process_data()
        
class LegacyAppAdapterInheritance(LegacyApp, ModernApp):
    # method of target ModernApp
    def transform_data(self):
        return self.process_data()
        

class FixClientCode:
    def __init__(self, app) -> None:
        self.app=app
    def main(self):
        print(self.app.transform_data())

if __name__ == "__main__":
    # Problem
    # ProblematicClientCode(LegacyApp()).main()
    # AttributeError: 'LegacyApp' object has no attribute 'transform_data'
    
    # Fix - Adapter
    # Inheritance
    FixClientCode(LegacyAppAdapterInheritance()).main()
    # Object Composition
    FixClientCode(LegacyAppAdapterObjectComposition(LegacyApp())).main()
