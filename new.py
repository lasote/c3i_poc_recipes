#!/usr/bin/env python
import os
import sys

err_msg = "'new.py lib/1.0@user/channel'"
json_template = """{
"url": "https://github.com/{OWNER}/{REPO}.git",
"commit": "{COMMIT_HASH}",
"pure_c": true,
"shared_available": true,
"header_only": false
}
"""


def parse_ref(ref):
    chunks = ref.split("@")
    if len(chunks) != 2:
        print("Invalid reference, Use {}".format(err_msg))
        exit(-1)
    name, version = chunks[0].split("/")
    user, channel = chunks[1].split("/")
    if channel != "stable":
        print("Channel has to be stable to be in conan-center")
        exit(-1)
    return name, version, user, channel


def run():
    if len(sys.argv) != 2:
        print("Invalid parameter, Use {}".format(err_msg))
        exit(-1)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    name, version, user, channel = parse_ref(sys.argv[1])
    dest_dir = os.path.join(dir_path, "index", name, version, user, channel)
    if os.path.exists(dest_dir):
        print("The reference already exists!")
        exit(-1)
    os.makedirs(dest_dir)
    file_path = os.path.join(dest_dir, "c3i.json")
    with open(file_path, "w") as f:
        f.write(json_template)

    print("""
'{}' generated, remember to edit it:

- url: Use the URL to clone containing the "conanfile.py"
- commit: The commit containing the version to add. No matter in which branch.
- header_only: If the library is header only specify 'true' without quotes, 'false' otherwise.
- pure_c: If the library is only C and not C++, use 'false' without quotes if the library is C++.
- shared_available: If you use the "shared" option in your recipe. 'false' without quotes if the library doesn't support shared.

""".format(file_path))


if __name__ == "__main__":
    run()

