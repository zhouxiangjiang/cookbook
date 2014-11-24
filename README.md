cookbook
========

Python/Web/Java/C Cookbook

- [Quick Start on OS X](https://github.com/leven-cn/cookbook/wiki/Quick-Start-on-OS-X/)
- [Quick Start with Bash](https://github.com/leven-cn/cookbook/wiki/Quick-Start-with-Bash/)
- [Getting Started with Linux](https://github.com/leven-cn/cookbook/wiki/Getting-Started-with-Linux/)

## Setup

### Ubuntu

Supported version: `12.04.2`, `12.04.3`, `12.04.4`, `14.04.1`.

```bash
sudo apt-get update
sudo apt-get install python3 git

git config --global user.name 'Your Name'
git config --global user.email your-github-email

git clone https://github.com/leven-cn/cookbook.git
cd cookbook
python3 admin.py setup
```

### OS X with MacPorts

Supported version: `10.8`, `10.9`, `10.10`.

```bash
sudo port install python34 git

git config --global user.name 'Your Name'
git config --global user.email your-github-email

git clone https://github.com/leven-cn/cookbook.git
cd cookbook
python3.4 admin.py setup
```
