from typing import Any, Dict, List, Self

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

class Argument:
    def __init__(self, text: str = None, required: bool = True) -> None:
        self.text = text
        self.required = required

class Command:
    def __init__(self, commands: list|str, args: list, description: str) -> None:
        self.commands = commands if isinstance(commands, list) else [commands]
        self.args = args
        self.description = description

class Feature:
    def __init__(self, name, /, description) -> None:
        self.name = name
        self.description = description

class Module:
    def __init__(
        self: Self,
        name: str,
        *,
        description: str = '',
        author: str = '',
        version: Any = None,
        commands: List[Command] = None,
        features: List[Feature] = None
    ) -> None:
        self.commands = commands if commands else []
        self.features = features if features else []
        self.name = name
        self.description = description
        self.author = author
        self.version = version

    def add_command(self: Self, command: Command, /):
        self.commands.append(command)
        return self
    
    def get_commands_count(self) -> int:
        return len(self.commands)

    def get_commands(self) -> List[Command]:
        return self.commands

    def add_feature(self: Self, feature: Feature, /):
        self.features.append(feature)
        return self
    
    def get_features_count(self) -> int:
        return len(self.features)

    def get_features(self) -> List[Feature]:
        return self.features

@singleton
class HelpList:
    modules: Dict[str, Module]

    def __init__(self) -> None:
        self.modules = {}
    
    def add_module(self, module: Module, /) -> Self:
        self.modules[module.name] = module
        return self
        
def display_help(self) -> Dict[str, Any]:
        total_modules = len(self.modules)
        total_commands = sum(module.get_commands_count() for module in self.modules.values())
        
        return {
            "total_modules": total_modules,
            "total_commands": total_commands,
            "modules": {module.name: [command.commands for command in module.get_commands()] for module in self.modules.values()}
        }
