# Early Preparation
If you would like to start preparing for this course in advance, I would suggest doing the following:
1. Install [Android Studio](https://developer.android.com/studio) on your local machine.
2. Watch the [Android App Development Tutorial](https://www.youtube.com/watch?v=tZvjSl9dswg) by Caleb Curry. This will more or less cover 25% of the course material. It will also prepare you to complete the first lab.
3. Familiarize yourself with the [Android API](https://developer.android.com/reference).
4. After steps 1-3, you can start practicing by creating simple apps such as a to-do list.
# Troubleshooting
If you are having problems with running demo programs or using Android Studio in general, please refer to the below notes.
## Demo Programs
If you are attempting to run the demo programs from class on your local computer, you will almost always have to:
1. Upgrade the Gradle until no more runtime errors occur.
2. Rebuild the Project 
3. Sync Projects with Gradle Files
## Android Emulator
1. You must ensure that your device supports Virtualization in the BIOS. 
2. Setting the emulated device to cold boot generally tends to prevent the emulator from bricking.
3. Sometimes you may have to periodically wipe the data on your emulator if random problems continue to persist.
4. In the absolute worst-case scenario, Android Studio is available on the RemoteLab. Please refer to the instructor's tutorial on how to set it up accordingly.
## Espresso Testing
1. Ensure that you have followed the [Espresso Setup Instructions](https://developer.android.com/training/testing/espresso/setup).
2. If you have run into the problem where there is no test directory, you must manually add **androidTest** directory. Everything should start to work after this.
## Exponentially Large Files
Make sure that you clean your project prior to submitting. This will simply delete class files which are generated upon compiling the program again.
