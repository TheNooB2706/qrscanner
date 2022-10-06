# QRscanner
A tool to decode QR code in clipboard image and copy the result to clipboard. Works on Linux (X11) and Windows. Intended to solve the problem of scanning on-screen QR code without taking out other devices.

![](../assets/demo.gif?raw=true)

# Installation and usage
## Downloading precompiled binary
You can get precompiled binary at the [release](https://github.com/TheNooB2706/qrscanner/releases) page of this repository. Download the file relevant to your operating system. The binary are compiled using [pyinstaller](https://github.com/pyinstaller/pyinstaller).

## Windows
The precompiled binary for Windows is packed as "one folder" for faster load time, hence it is uploaded as a zip archive to the release page. Download the zip file and extract to any convenient place.
### Binding to shortcut key
This section of the guide shows how to bind the program to a shortcut key which will trigger the execution.

Create a shortcut of the binary `qrscanner.exe` to desktop by right clicking and "Send to Desktop".

![](../assets/createdesktopshortcut.png?raw=true)

On the desktop, right click on the created shortcut and click "Properties".

![](../assets/properties.png?raw=true)

Append ` -bind` to the "Target" field.

Then, click on "Shortcut key" field and press your key combination.

~~You can also make the created shortcut hidden to prevent it from cluttering the desktop.~~ Keybinding breaks after reboot when you set the shortcut to hidden.

![](../assets/hidden.png?raw=true)

If you prefer, you may bind the shortcut key with third-party programs such as [AutoHotkey](https://www.autohotkey.com/) instead as well.

### Screenshot and copy to clipboard
By default, the shortcut key `Alt-PrintScreen` will screenshot the current active window and copy it to clipboard. This can be used in conjunction with this program to scan QR code on screen, which is the intended use case of this program.

Some other default shortcut keys:  
* `PrintScreen` will screenshot the whole screen and copy to clipboard.
* `Win-Shift-S` allows select and screenshot custom region on screen and copy to clipboard.

### Missing DLLs
If you get any error messages about missing DLLs when using the prebuilt binary, try installing [vcredist](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170).

## Linux
Download the binary to any convenient place. You may install it to `/usr/bin` if you want.

You might need to install zbar shared library.  
Debian/Ubuntu and derivatives:  
```
sudo apt install libzbar0
```

Additionally, `xclip` needs to be installed:  
```
sudo apt install xclip
```

### Binding to shortcut key
The exact procedure might vary depending on different desktop environment. You may want to search online for DE specific guide.

**KDE**:  
Custom shortcut can be set by going to System Settings > Shortcuts > Custom Shortcuts. Click Edit > New > Global Shortcut > Command/URL. Name the new shortcut with anything you like.

![](../assets/newshortcutkde.png?raw=true)

Next, go over the "Trigger" tab and choose your key combination.

At the "Action" tab, set the command to the following:  
```
/path/to/qrscanner -bind
```  
Replace the path with actual path.

### Screenshot and copy to clipboard
I use [flameshot](https://flameshot.org/) as the primary screenshot tool on Linux, which has feature to copy the screenshot to clipboard.

## Running the script directly
The precompiled binaries are made for convenience purpose. You may of course not use the precompiled binary. Clone this repository and install the dependencies in `requirements.txt`

# Additional information
This (tiny) project is made for my own use. Not a lot of effort is put into the code so don't expect good code quality. Any improvements or contributions are welcomed.

## Wayland support
The programs utilize `xclip` to get clipboard image in Linux, as ImageGrab is not available on Linux. As its name suggests, `xclip` is for X Window System only. As I am still only using X11, it is hard for me to implement Wayland support (Not impossible, but remember this is a "free-time code" made in an afternoon). Any contribution with this regard is appreciated.

## Command line argument
There's only one argument for this program: `-bind`, which is used to enable notification when the program is ran.

# License
[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)