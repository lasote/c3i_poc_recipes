<a href="http://jfrog.com"><img src="https://res-2.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_120,w_120,f_auto,b_white,q_auto:eco/v1397198554/51281b50b797124bebc82ab956d93893.jpg" width=100></a><a href="https://bintray.com/conan/conan-center"><img src="https://support.jfrog.com/resource/1534758892000/BR_JFC_Resource/img/Bintray.png" width=100></a><a href="https://conan.io"><img src="https://files.startupranking.com/startup/thumb/58827_bd1ac1623dea41fd4a3293a79b54836dca168619_conan_m.png" width=100></a>


## C3I: Generate automatically binaries for your Conan recipes at Bintray:conan-center

You can contribute with your Conan package to the JFrog Bintray "conan-center" central repository by submitting a Pull Request to this repository:

- Fork this repository
- Add a new `c3i.json` file poiting to your repository containing the recipe in a folder "package_name/package_version/username". E.g `mylibrary/1.8.1/myusername` you can use any `myusername`, for example your github nickname.
   
 ```json
 {
 "url": "https://github.com/bincrafters/conan-gtest.git",
 "commit": "9d4cfda8a4922229c9e105522830f007d5fe1c8f"
 }
```
- Submit a pull request (one package change => one PR)

Conan will generate more than a hundred binary packages for the mainstream configurations, and once accepted, the recipe and all the packages will be upload to the [conan-center](https://bintray.com/conan/conan-center) repository.

- GCC: 4.9, 5, 6, 7
- Clang: 3.8, 3.9, 4.0
- Visual Studio: 10, 12, 14 (with different runtimes "MT", "MD", "MTd", "MDd")
- Apple-clang: =  8.1, 9.0, 10.0

For each version, `x86, x86_64` and `Release, Debug` packages


# About JFrog Bintray
JFrog Bintray is a cloud platform that gives you full control over how you publish, store, promote, and distribute software. As a universal distribution platform, Bintray supports all file formats and offers advanced integration with common development technologies including:

- Docker
- Conan
- Debian
- Maven
- RPM
- npm
- NuGet
- Vagrant
- Opkg

You can create your personal [Bintray account](https://bintray.com) free repositories for many different package managers, as Debian, Docker, NPM... including also Conan repositories for Open Source projects.



