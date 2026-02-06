#!/usr/bin/python3
"""
Module defining an abstract base class Animal
with an abstract method sound.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animal with an abstract method sound."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal and implements sound."""

    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal and implements sound."""

    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"
