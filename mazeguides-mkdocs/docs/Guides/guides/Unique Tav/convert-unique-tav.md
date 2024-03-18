---

title: How to convert mods to be compatible with Unique Tav

---

> Guide by Maze (Edited by Meowcat285)

---

!!! note
    This guide specifically covers `CovenElf’s makeup/tattoo collection`

## Step 1: Download the CovenElf’s makeup/tattoo collection

Go ahead and download `CovenElf’s makeup/tattoo collection`

![Nexus Mods download page](/assets/unique-tav/2024-03-04 15.45.41.png){ loading=lazy }

!!! note
    You can also download just makeup or just tattos, the process is the same with other mods as well

---

## Step 2: Extract the `rar` file

Right click on the `rar` file in File Explorer and select extract all

![File Browser right click menu with extract all highlighted](/assets/unique-tav/2024-03-04 15.49.16.png){ loading=lazy }

![Extracted files](/assets/unique-tav/2024-03-04 15.52.18.png){ loading=lazy }

---

## Step 3: Convert the mod

Now open the extracted folder. 

!!! warning

    Do not put the generated folder inside the data folder yet, go through the guide first

Open the generated folder and go all the way down in the folders until you see this:

![alt](/assets/unique-tav/2024-03-04 15.54.35.png){ loading=lazy }

Now open your data folder in another file explorer window:

![alt](/assets/unique-tav/2024-03-04 15.55.30.png){ loading=lazy }

Now open the generated folder, and find the folder named FACE

Path: `Data\Generated\Public\Shared\Assets\unique_tav`

![alt](/assets/unique-tav/2024-03-04 15.56.35.png){ loading=lazy }

Open the folder named `FACE`

![alt](/assets/unique-tav/2024-03-04 15.57.32.png){ loading=lazy }

You will see these 3 files. Take these two files:

![alt](/assets/unique-tav/2024-03-04 15.58.06.png){ loading=lazy }

Note down their names. For reference, I will copy them here as well

Unique Tav Face Tattoo: `Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`

Unique tav Make up: `Skin_Atlas_Head_SHR_Makeup_A_MSK.DDS`

Now go to the CovenElf folder with the files, and rename the respective files to the Unique Tav version of the files: 

![alt](/assets/unique-tav/2024-03-04 15.59.32.png){ loading=lazy }

This is here the file extension comes into play: you need to rename the last .dds on the CovenElf files to .DDS

CovenElf face tattoo: `Skin_Atlas_Head_SHR_Tattoo_A_MSK1.dds` needs to be renamed to: `Skin_Atlas_Head_SHR_Tattoo_A_MSK.DDS`

CovenElf makeup: `Skin_Atlas_Head_SHR_Makeup_A_MSK2.dds` needs to be renamed to: `Skin_Atlas_Head_SHR_Makeup_A_MSK.DDS`

When you have done that you can now go back into the game data folder, and then the FACE folder in unique tav and delete these two files:

![alt](/assets/unique-tav/2024-03-04 16.00.50.png){ loading=lazy }

When you have deleted the Unique Tav files, you then drag the renamed files from CovenElf into the Unique Tav FACE folder:

![alt](/assets/unique-tav/2024-03-04 16.01.21.png){ loading=lazy }

![alt](/assets/unique-tav/2024-03-04 16.01.40.png){ loading=lazy }

When you have done that, you have now installed CovenElf’s or any other makeup or face tattoo correctly and they should work!

---

## Part 4: Boring Tieflings

For mods like Boring Tieflings, the process is very similar, you have to find the Unique Tav equivalent of the Boring Tiefling files and rename Boring Tieflings to Unique Tav files, and replace the files!

!!! tip

    On the Boring Tieflings Nexus download page, you can go under preview files and from there you can see the path.

    ![alt](/assets/unique-tav/2024-03-04 16.05.44.png){ loading=lazy }

Now go to generated in your data folder:

![alt](/assets/unique-tav/2024-03-04 16.06.19.png){ loading=lazy }

And then find the folder named `BODY`: 

![alt](/assets/unique-tav/2024-03-04 16.06.48.png){ loading=lazy }

Open the `BODY` folder

![alt](/assets/unique-tav/2024-03-04 16.07.31.png){ loading=lazy }

Since Boring Tieflings replaces Tiefling files, you go under the `TIF` folder

![alt](/assets/unique-tav/2024-03-04 16.08.20.png){ loading=lazy }

Now depending on which Boring Tiefling file you downloaded, you choose either Male (if you downloaded the file for Boring Tiefling Male) or Female (if you downloaded the file for Boring Tiefling Female)

!!! note
    Remember this is only an example, so do not worry - you do not need to actually do this, but it will be the same concept throughout with ALL mods that replaces textures like these however there is just too many mods to cover them all, so here's a general guide on how to actually do it

I choose the Boring Tiefling female, so I open the “FEMALE” folder:

![alt](/assets/unique-tav/2024-03-04 16.09.12.png){ loading=lazy }

Now from the file preview, I could see that Boring Tiefling had two files: 

`TIF_F_NKD_Body_A.gr2 `

and

`TIF_F_Tail_A.GR2`

You then find the Unique Tav equivalent:

![alt](/assets/unique-tav/2024-03-04 16.10.14.png){ loading=lazy }

Then rename the Boring Tiefling files from:

`TIF_F_NKD_Body_A.gr2` to `UNIQUE_TIF_F_NKD_BODY_A.GR2`

and

`TIF_F_Tail_A.GR2` to `UNIQUE_TIF_F_NKD_Tail_A.GR2`

Then delete the Unique Tav files and replace them with the new renamed Boring Tiefling files.

---

> Credits:
>
> Maze, Meowcat285
>
> Kartoffel for Unique tav

**© Maze 2024, all rights reserved**