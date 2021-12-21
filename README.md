# UE4PythonToolPack

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
  - [GUI_rename_assets](#GUI_rename_assets)
  - [actor_action_util](#actor_action_util)

This is a script tool pack which is edited in Ptyhon2.7. And the GUI is edited by QT in C++. This tool pack is designed to manage the resources inside UE4 in a quick, easy and serialized way. Python is a good programming language, sometimes it's much more convenient than C++ like in string processing. And QT is a wellknown widget toolkit for creating GUI as well as cross-platform.

## Install

First of all, install python and enable Python plugin in UE4. The scripts are in the folder named opms.

![avatar](https://docs.unrealengine.com/4.27/Images/ProductionPipelines/ScriptingAndAutomation/Python/install-python-plugin.webp)

Then run the Python script which you need in UE4.

![avatar](https://docs.unrealengine.com/4.27/Images/ProductionPipelines/ScriptingAndAutomation/Python/python-console-input.webp)

## Usage

Here are some introductions about each script.

### GUI_rename_assets

Select the assets that you wanna rename, and type a keyword and a new word. The keyword in the selected assets will be replaced with the new word.

### actor_action_util

Select the mesh/meshes and a material. And the materials of the mesh/meshes will be replaced by the selected material.
