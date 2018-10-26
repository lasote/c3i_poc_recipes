<a href="http://jfrog.com"><img src="https://res-2.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_120,w_120,f_auto,b_white,q_auto:eco/v1397198554/51281b50b797124bebc82ab956d93893.jpg" width=100></a><a href="https://bintray.com/conan/conan-center"><img src="https://support.jfrog.com/resource/1534758892000/BR_JFC_Resource/img/Bintray.png" width=100></a>


# C3I: Creating binaries for your Conan recipes

You con contribute to the JFrog Bintray "conan-center" central repository by submitting a Pull Request to this repository:

- Fork this repository
- Add a new `c3i.json` file poiting to your repository containing the recipe in a folder "package_name/package_version/username". E.g `mylibrary/1.8.1/myusername` you can use any `myusername`, for example your github nickname.
   
 ```json
 {
 "url": "https://github.com/bincrafters/conan-gtest.git",
 "commit": "9d4cfda8a4922229c9e105522830f007d5fe1c8f"
 }
```
- Submit a pull request (one package change => one PR)

Conan will generate more than a hundred binary packages for the mainstream configurations, and once accepted, the recipe and all the packages will be upload to the [conan-center] repository.

# About JFrog Bintray

You can create your personal [Bintray account](https://bintray.com) free repositories for many different package managers, as Debian, Docker, NPM... including also Conan repositories.



