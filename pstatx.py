# Copyright 2023 Elijah Gordon (NitrixXero) <nitrixxero@gmail.com>

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from stat import *
from os import stat, chmod, getcwd, getlogin, name, path
from sys import argv, exit
from pwd import getpwuid
from time import ctime
from argparse import ArgumentParser


def pstatx(filename):
    print("-- Filename: ( {0} )".format(filename))
    print("-- Directory: ( {0} )".format(S_ISDIR(stat(filename).st_mode)))
    print("-- Character special device file: ( {0} )".format(S_ISCHR(stat(filename).st_mode)))
    print("-- Path is a block special device file: ( {0} )".format(S_ISBLK(stat(filename).st_mode)))
    print("-- File: ( {0} )".format(S_ISREG(stat(filename).st_mode)))
    print("-- FIFO or named pipe: ( {0} )".format(S_ISFIFO(stat(filename).st_mode)))
    print("-- Symbolic link: ( {0} )".format(S_ISLNK(stat(filename).st_mode)))
    print("-- Path is a socket: ( {0} )".format(S_ISSOCK(stat(filename).st_mode)))
    print("-- Door: ( {0} )".format(S_ISDOOR(stat(filename).st_mode)))
    print("-- Event port: ( {0} )".format(S_ISPORT(stat(filename).st_mode)))
    print("-- Whiteout: ( {0} )".format(S_ISWHT(stat(filename).st_mode)))
    print("-- File permission bits: ( {0} )".format(oct(S_IMODE(stat(filename).st_mode))))
    print("-- Bit mask for file type: ( {0} )".format(oct(S_IFMT(stat(filename).st_mode))))
    print("-- Mode: ( {0} )".format(filemode(stat(filename).st_mode)))
    print("-- Protection bits: ( {0} )".format(stat(filename).st_mode))
    print("-- Inode number: ( {0} )".format(stat(filename).st_ino))
    print("-- Device: ( {0} )".format(stat(filename).st_dev))
    print("-- Number of hard links: ( {0} )".format(stat(filename).st_nlink))
    print("-- Numerical user ID: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_gid))
    print("-- Numerical group ID: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_uid))
    print("-- Size of file, in bytes: ( {0} )".format(stat(filename).st_size))
    print("-- Time of most recent access: ( {0} )".format(ctime(stat(filename).st_atime)))
    print("-- Time of most recent content modification: ( {0} )".format(ctime(stat(filename).st_mtime)))
    print("-- Platform dependent; time of most recent metadata change on Unix: ( {0} )".format(ctime(stat(filename).st_ctime)))
    print("-- Most recent access in nanoseconds: ( {0} )".format(stat(filename).st_atime_ns))
    print("-- Most recent content modification in nanoseconds: ( {0} )".format(stat(filename).st_mtime_ns))
    print("-- Most recent metadata change in nanoseconds: ( {0} )".format(stat(filename).st_ctime_ns))
    print("-- Number of 512-byte blocks allocated for file: ( {0} )".format(stat(filename).st_blocks))
    print("-- Filesystem blocksize for efficient file system I/O: ( {0} )".format(stat(filename).st_blksize))
    print("-- Type of device if an inode device: ( {0} )".format(stat(filename).st_rdev))
    print("-- Login name: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_name))
    print("-- Optional encrypted password: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_passwd))
    print("-- User name or comment field: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_gecos))
    print("-- User home directory: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_dir))
    print("-- User command interpreter: ( {0} )".format(getpwuid(stat(filename).st_uid).pw_shell))
    print("-- Socket: ( {0} )".format(stat(filename).st_mode & S_IFSOCK == S_IFSOCK))
    print("-- Symbolic lynk: ( {0} )".format(stat(filename).st_mode & S_IFLNK == S_IFLNK))
    print("-- Regular file: ( {0} )".format(stat(filename).st_mode & S_IFREG == S_IFREG))
    print("-- Block device: ( {0} )".format(stat(filename).st_mode & S_IFBLK == S_IFBLK))
    print("-- Directory: ( {0} )".format(stat(filename).st_mode & S_IFDIR == S_IFDIR))
    print("-- Character device: ( {0} )".format(stat(filename).st_mode & S_IFCHR == S_IFCHR))
    print("-- Fifo or named pipe: ( {0} )".format(stat(filename).st_mode & S_IFIFO == S_IFIFO))
    print("-- Name of OS: ( {0} )".format(name))
    print("-- Name of the logged in user: ( {0} )".format(getlogin()))
    print("-- Current working directory: ( {0} )".format(getcwd()))


def main():
    parser = ArgumentParser(description="File Statistics Tool")
    parser.add_argument("-f", "--filename", help="Path to the file for statistics.")
    parser.add_argument("-v", "--version", action="store_true", help="Show version information.")
    args = parser.parse_args()

    if args.version:
        print("File Statistics Tool v1.0")
        return

    if args.filename:
        if path.exists(args.filename):
            pstatx(args.filename)
        else:
            print("Error: The specified file does not exist.")
            return
    else:
        parser.print_help()
        exit(1)


if __name__ == "__main__":
        main()
