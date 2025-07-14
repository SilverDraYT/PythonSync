# Changelog

This has been started halfway (or almost at the ending of this little proyect so this will start from this last change)

## [] - 00-00-0000
### [UNRELEASED]
### Added
### Changed
### Fixed
### Removed


## [1.0.1] - 05-07-2025

### Added
- A logfile of the new archives that are copied or deleted (If more than one move is done in the same day the new move is written on the bottom of the file)
### Changed
- Now file_organizer has an aditional option called divider (only in copy_files), it makes possible to check and use the modified time of a file to copy it (currently only using it on pctoremote)
- Changed Launch.bat for Launcher.exe written in C++
### Fixed
- In Launcher.exe where it didnt detect the 'Enter' as an input
### Removed
- The Launch.bat file removed
---

## [1.0.0] - 26-06-2025

### Added
- README.md
### Changed
In 'pctoremote' and 'remotetopc'.
- How to take the variables from 'config.ini'. Now is used 'configparser'. 
### Fixed
- Error in 'remotetopc.py' where there was no extension selected for the 'copy_files' function.
- Code in 'file_organizer.py' on the function copy_files that didnt work well with the remotetopc.