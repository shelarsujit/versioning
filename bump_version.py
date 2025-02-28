import argparse
from _version import MAJOR, MINOR, PATCH

def write_version(major, minor, patch):
    with open("_version.py", "w") as f:
        f.write(f"MAJOR = {major}\nMINOR = {minor}\nPATCH = {patch}\n")

def auto_bump_patch():
    write_version(MAJOR, MINOR, PATCH+1)

def bump_major():
    write_version(MAJOR+1, 0, 0)

def bump_minor():
    write_version(MAJOR, MINOR+1, 0)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--major', action='store_true')
    parser.add_argument('--minor', action='store_true')
    args = parser.parse_args()
    if args.major:
        bump_major()
    elif args.minor:
        bump_minor()
    else:
        auto_bump_patch()
