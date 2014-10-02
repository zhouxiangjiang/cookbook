Linux Cookbook
========

- [Getting Started](#getting-started)
- [Bash](#bash)
- [Regular Expression](#regular-expression)_

## Getting Started

```bash
sudo shutdown -h|-r now

# Package Management on Debian/Ubuntu
sudo apt-get update
sudo apt-get install|remove|purge <pkg ...>

cd [~|-|..|<dir>]
pwd
ls [-l|-a|-r]
less <file>
ln -s <src> <symlink>
cp|mv [-r|-u] <src> <dst>
rm [-r|-f] <file ...>|<dir>
mkdir [-p] <dir>
rmdir <empty-dir>
wc -l <file>
head|tail -n <num> <file>
tail -f <file>

which|man <cmd>

# gzip & bz2
tar xzvf tar.gz|tgz
tar xjvf tar.bz2
tar czvf tar.gz|tgz <file ...>|<dir>
tar czvf tar.bz2 <file ...>|<dir>

# root Permission
sudo <cmd>
sudo visudo

# New User/Group
#
# NOTE: `useradd` and `groupadd` are low-level utilities. On Debian, `adduser`
# and `addgroup` should be used instead.
#
# By default, each normal user in Debian is given a corresponding group with
# the same name, and the system users are placed in the `nogroup` group.
sudo [--system] adduser <user>
sudo passwd <user>
sudo [--system] addgroup <group>

# Add existing user to group (re-login required)
sudo adduser <user> <group> # for Debian/Ubuntu
sudo gpasswd -a <user> <group> # for all Linux, as well as Debian/Ubuntu

# Change File Ownership
sudo chown <owner>[:<group>] <file ...>

# Search File
find <dir> <text-expr> [<logic-opertor ...>] <act>
    -name <file-pattern>
    -type f|d|l|b|c
    -size <N>c|k|M|G
    -empty
    -cmin [-|+]<N-min>
    -ctime [-|+]<N-day>
    -inum <inode>

    -and
    -or
    -not
    ()

    -print
    -delete
    -ls
    -exec <cmd> '{}' ';'|+

# Search File Contents
grep <pattern> <file>

# Date & Time
date <+format>
    %% - '%'
    %H - hour (00-23)
    %I - hour (01-12)
    %M - minute (00-59)
    %S - second (00-59)
    %T - %H:%M:%S
    %R - %H:%M
    %y - year (00-99)
    %Y - year (0000-9999)
    %m - month (01-12)
    %d - day of month (01-31)
    %D - %m/%d/%y
    %u - day of week (1-7, 1=Monday)
    %w - day of week (0-6, 0=Sunday)
    %n - newline ('\n')
    %t - tab ('\t')

# Join Files
#
# Say we have a large file that has been split into multiple parts, and we want
# to join them back together. If the files were named:
#     movie.mp4.001, movie.mp4.002 ... movie.mp4.099
cat movie.mp4.0* > movie.mp4

# Mount ISO
mount -t iso9660 -o loop <img>.iso <mnt-point>

# Mount CD-ROM
sudo mkdir /mnt/cdrom
sudo mount -t iso9660 -o loop /dev/cdrom /mnt/cdrom

# Unmount before eject CD-ROM
sudo umount /dev/cdrom
sudo rmdir /mnt/cdrom

# CD-ROM => ISO
dd if=/dev/cdrom of=<dst>.iso

# Local files => ISO
genisoimage -o <dst>.iso -R -J <dir>
    -R # Rock Ridge extension, support long file names and POSIX-style file permissions
    -J # Joliet extension, support long file names in Windows

# Blank/Write CD-ROM
wodim dev=/dev/cdrom blank=fast
wodim dev=/dev/cdrom <dst>.iso

# Environment Variables
echo $PWD   # current directory
echo $USER  # current user name
echo $HOME  # home directory of current user

# Process Management
killall -9 <process-name>
kill -9 <pid>
ps aux
top

# Network Interface
#
# NOTE: `ifconfig` uses obsolete kernel interface `ioctl()` to get full address
# information, which limits hardware addresses to 8 bytes!
ip addr show [dev <if-dev>]                         # ifconfig
netstat -ie                                         # ifconfig
sudo ip addr add <ipv4>[/prefix>] dev <if-dev>      # sudo ifconfig <if-dev> add <ipv4>
sudo ip addr del <ipv4>/<prefix=32> dev <if-dev>    # sudo ifconfig <if-dev> del <ipv4>
sudo ip link set <if-dev> up|down                   # sudo ifconfig <if-dev> up|down
sudo ip addr add 192.168.0.77/24 dev eth0           # sudo ifconfig eth0 192.168.0.77 netmask 255.255.255.0

# Network Routing
#
# NOTE: `route` is obsolete. Use `ip route` instead.
ip route show [dev <if-dev>]                        # route
netstat -re                                         # route
sudo ip route add default via <ipv4> dev <if-dev>   # sudo route add default dev <if-dev>
sudo ip route add|del 192.168.0.77/24 dev eth0      # sudo route add|del -net 192.168.0.77/24 dev <if-dev>

# Network Troubleshouting
ping <ip>
sudo sysctl -w net.ipv4.icmp_echo_ignore_all=1                  # Disable ping (temporary)
sudo echo 'net.ipv4.icmp_echo_ignore_all=1' >> /etc/sysctl,conf # Disable ping (permanent)
dig
traceroute <ip>                                                 # trace routing
```

### Network Configuration

```
# Debian: /etc/network/interfaces
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
    address 192.168.1.2
    netmask 255.255.255.0
    gateway 192.168.1.1
    dns-nameservers <dns-ip ...>

auto eth1
iface eth1 inet dhcp
```

## Bash

### Key Bindings

- `Tab` - Completion
- `Ctrl+D` - `exit` or EOF
- `Crrl+C` - SIGTERM
- `Ctrl+A` / `Ctrl+E` - Go to Beginning / End of Command Line
- `Ctrl+U` / `Ctrl+K` - Cut from Current Position to Beginning / End of Command Line
- `Ctrl+Y` - Paste
- `Ctrl+L` - `clear`
- `Ctrl+R` - History Search, `Ctrl+C` to Quit
- `Ctrl+Z` - SIGSTP

### Expansion

```bash
$ echo text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
text /home/ly/a.txt a b A B C a 2 ly

$ echo "text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER"
text ~/*.txt {a,b} {A..C} a 2 ly

$ echo 'text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER'
text ~/*.txt {a,b} {A..C} $(echo a) $((1+1)) $USER
```

### I/O Redirection

```bash
# Redirect stderr
ls -l /bin/usr 2> ls-error.log

# Redirect stdout and stderr
ls -l /bin/usr &> ls.log  # Bash 4.0+
ls -l /bin/usr > ls.log 2>&1

# Sometimes "silence is golden"
ls -l /bin/usr > /dev/null 2>ls.log
```

### File Testing Operator

```bash
-e exist
-s NOT empty
-f regular file
-d directory
-S socket
-p named pipe
-h symbolic link
-r readable
-w writable
-nt newer than
-ot older than
-ef hard link
```

### Text Processing

```bash
# Subtitute
str="a-b-c"
echo ${str/-/_}_d   # a_b-c_d
echo ${str//-/_}_d  # a_b_c_d

# Substring
str="abcdef"
echo ${str:1}       # a
echo ${str:2:2}     # bc

# Testing Operator
-z empty
-n NOT empty
```

## Regular Expression

- `*` - Any numbers of characters
- `?` - Any single character
- `[abc]` - Any character in set of `abc`
- `[!abc]` - Any character NOT in set of `abc`
- `[:alpha:]` - Any letter
- `[:lower:]` - Any lower-case letter
- `[:upper:]` - Any upper-case letter
- `[:digit:]` - Any digit
- `[:alnum:]` - `[[:alpha:][:digit:]]`
- `[:word:]` - `[[:alnum:]_]*`
- `[:blank:]` - `Space` + `Tab`
- `^abc` - Any line started with `abc`
- `abc$` - Any line ended with `abc`
- `+` - More than once
- `{n}`, `{n,m}` - From (n) to (m) times


## References

- [Ubuntu Doc](https://help.ubuntu.com/)
- The Linux Command Line (2012)
- The Linux Commnad Line, 2nd Edition (2013)
