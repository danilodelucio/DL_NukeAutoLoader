<img width="700" height="152" alt="DL_NukeAutoLoader Logo" src="https://github.com/user-attachments/assets/8e3d329d-5986-4d9c-9ff3-81cb6f90891b" />

**Automatically loads gizmos, Nuke files (.nk/.nkind), and Python scripts into the Nuke toolbar.**

---

Supports:
- loose gizmos in the root folder.
- subfolders as categories.
- multiple nested levels.

<img width="907" height="653" alt="folder and tool" src="https://github.com/user-attachments/assets/253bd886-10f9-4e95-978f-1e22c270045a" />

# ☢️ Compatibility
**DL_NukeAutoLoader** was created and tested in Nuke 12.1v5 (Python 2.7.16), and Nuke Indie 16.0v7 (Python 3.11.7), so it's designed to work with all versions of Nuke.

# ⚙️ How to Install

<details>
  <summary>1. Downloading the tool</summary>
  <br>
  
At the top of this page, click on the green button and download the **zip** file.<br>

<img width="450" height="360" alt="image" src="https://github.com/user-attachments/assets/1fa644a6-e830-4107-b501-c700cc24f36c" /><br>
  
Save it anywhere on your computer, then extract its content. <br> 

<img width="244" height="103" alt="image" src="https://github.com/user-attachments/assets/8f3db51c-c398-4b8b-b9df-a63f3ca24b17" /><br>

For better convenience, I suggest renaming the folder by removing the "**-main**" from the filename. You should have something like this.<br>

<img width="607" height="365" alt="image" src="https://github.com/user-attachments/assets/5a055201-4cbd-4c28-be4d-07c2f6729fea" /><br>

</details>

<details>
  <summary>2. Nuke Setup</summary>
   <br>

Open your `.nuke/init.py` file in a text editor. Paste the line below and update the directory to the location where you saved the `DL_NukeAutoLoader` folder.

`nuke.pluginAddPath("C:/path/to/DL_NukeAutoLoader")`

</details>

<details>
  <summary>3. Custom Folder Setup</summary>
   <br>
   
Open the `custom_path.json` file and add the directory where all the tools (gizmos, NK files or Python scripts) reside.<br>

<img width="274" height="221" alt="image" src="https://github.com/user-attachments/assets/18a985b4-655b-4499-aa01-e5860ca5bc08" />


<img width="404" height="97" alt="image" src="https://github.com/user-attachments/assets/459e89ef-313a-4c9a-84fd-fb32b05b4aa2" /><br>

Open Nuke and you should see the **DL_NukeAutoLoader** icon appear in the toolbar.<br>

<img width="173" height="342" alt="image" src="https://github.com/user-attachments/assets/939a4ec4-e2c6-431a-a8d1-35669e448073" />

</details>


# Support me! ☕

![Supporters Page](https://danilodelucio.com/wp-content/uploads/2025/12/supporter-badges.jpg)

## Enjoying this tool?
Support me with a coffee on my [Supporters](https://www.danilodelucio.com/supporters) page — get a badge and join the wall of supporters! 😎

You can also ⭐ _star this repository_ ⭐ — it helps a lot with visibility and motivates me to keep developing tools for VFX.

Sharing this project or sending me a positive message would help me in the same way.
