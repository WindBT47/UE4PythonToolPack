# UE4PythonToolPack

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
  - [GUI_rename_assets](#GUI_rename_assets)
  - [actor_action_util](#actor_action_util)
  - [clean_up](#clean_up)
  - [delete_empty_folder](#delete_empty_folder)
  - [delete_no_static_mesh](#delete_no_static_mesh)
  - [duplicator](#duplicator)
  - [pow_of_two](#pow_of_two)
  - [prefixer](#prefixer)
  - [removeed_unused](#removeed_unused)
  - [set_linear_color_tex](#set_linear_color_tex)
  - [world_outliner](#world_outliner)

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

### clean_up

Select the assets that you wanna classify. Then they will be put in different folders by their type.

### delete_empty_folder

Delete the empty folders.

### delete_no_static_mesh

Delete all of the StaticMeshActors which don't own static mesh.

### duplicator

Duplicate the assets by the number you input.

### pow_of_two

Texture sizes need to be a power of 2(for example, 2, 4, 8, 16). It's a script for checking the validity of the texture.

### prefixer

Add prefix for your assets by type. It follows the rule in [ue5 style guide](https://github.com/Allar/ue5-style-guide). And you can change the format in prefix_mapping.json

### removeed_unused

Remove all of the assets that are unused. Or move them into a folder named Trash.

### set_linear_color_tex

Set the properties of the textures which you want to change. Like in the mask textures, set sRGB to the False and set the compression setting to Mask.

### world_outliner

Move the actors that are in the world outliner into different folders by type.
