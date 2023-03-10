# Unreal Engine 4 Material Assigner Plugin
# ue-material-actor-assigner

This plugin allows you to quickly assign a selected material to all static mesh actors in the currently selected levels.
# Requirements
* Unreal Engine 4.26
* Python 3.7
* Unreal Engine Python API

# Installation
1. Clone or download this repository
2. Copy the "MaterialAssigner" folder to the "Plugins" directory in your Unreal Engine project.

# Usage

1. Open your Unreal Engine Project
2. Select a Material asset in the Content Browser.
3. Select the Static Mesh actors in the level that you want to assign the material to.
4. In the main menu go to **File > Execute Python Script"
5. The material will be assigned to all selected Static Mesh actors

# Notes
* If no Static Mesh actors are selected, the plugin will not do anything
* If more than one Material asset is selected, the plugin will only use the first one
* If a Static Mesh actor already has a material assigned to it, the plugin will overwrite it with the new material
