# OpenShowCueSystem
A Python-based Cue Management Library for Stage Managers


## Install OpenSCS
1. Download the Latest Release: https://github.com/iainrosen/OpenSCS/releases
2. Open and extract the contents of the downloaded archive
3. If you don't have Pythonv2.7 Installed: Run the installer from the OpenSCS folder
4. OpenSCS is now installed!


## Create Your First Show
  OpenSCS uses raw files to manage and save your cues, which are stored in the OpenSCS folder.
1. Double-click to run the ```mainstage.py``` file. This is your Command Line Interface (CLI), and helps you manage your cues.
2. You will be greeted with a prompt this will look similar to this ```MainstageCLI>>>```
3. To start your first show, type ```new``` and follow the prompts
4. The CLI will enter Open Show mode, and you can now begin building your show

## Create Cues
1. Once in Open Show mode, you can not start to build your show
2. To start writing cues, type ```new```
3. At the first prompt, enter the cue number. The cue number can include one number pass the decimal. Example: ```1.1``` or ```3.8```
4. At the second prompt, enter the cue description. This can be something like ```Lights Fade Stage Left``` or ```SFX Cue 8 GO```
5. Repeat this process until you are out of cues to enter
6. To exit cue recording mode, type ```end``` under the ```Cue Number: ``` prompt

## Playback Mode
1. In Open Show mode, start the playback of your cues by typing ```play```
2. The ```>>>``` indicates which cue is current
3. Press ```[ENTER]``` to move down the list
4. Type anything and ```[ENTER]``` to exit playback

## Deleting Cues
1. To delete a cue, ensure you are in Open Show mode and type ```del```
2. Enter the number of the cue you wish to delete a press enter

## Creating an example cue list
  You can create an randomly generated cue list for testing the program or demonstration. To do so, just run ```examplecreator.py``` and wait for the ```Cues Created:``` message to appear. The example cues are now ready to playback. You can open them in the Mainstage CLI using the show name ```example```
