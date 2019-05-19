# datetimeutil-shared-lib-conan


```
conan export . datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable

conan remote remove datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable

conan remote add datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable https://api.bintray.com/conan/mycpptutorial/datetimeutil

conan user -p <APIKEY> -r datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable yourbintrayusername


conan install datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable --build=datetimeutil-shared-lib-conan

conan upload "datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable" -r datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable --all
```


cd '/Users/nkabiliravi/.conan/data/datetimeutil-shared-lib-conan/1.0.0/mycpptutorial/stable/build/f8bda7f0751e4bc3beaa6c3b2eb02d455291c8a2' && cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE="Release" -DCONAN_EXPORTED="1" -DCONAN_IN_LOCAL_CACHE="ON" -DCONAN_COMPILER="apple-clang" -DCONAN_COMPILER_VERSION="10.0" -DCONAN_CXX_FLAGS="-m64" -DCONAN_SHARED_LINKER_FLAGS="-m64" -DCONAN_C_FLAGS="-m64" -DCONAN_LIBCXX="libc++" -DBUILD_SHARED_LIBS="OFF" -DCMAKE_INSTALL_PREFIX="/Users/nkabiliravi/.conan/data/datetimeutil-shared-lib-conan/1.0.0/mycpptutorial/stable/package/f8bda7f0751e4bc3beaa6c3b2eb02d455291c8a2" -DCMAKE_INSTALL_BINDIR="bin" -DCMAKE_INSTALL_SBINDIR="bin" -DCMAKE_INSTALL_LIBEXECDIR="bin" -DCMAKE_INSTALL_LIBDIR="lib" -DCMAKE_INSTALL_INCLUDEDIR="include" -DCMAKE_INSTALL_OLDINCLUDEDIR="include" -DCMAKE_INSTALL_DATAROOTDIR="share" -DCMAKE_EXPORT_NO_PACKAGE_REGISTRY="ON" -Wno-dev '/Users/nkabiliravi/.conan/data/datetimeutil-shared-lib-conan/1.0.0/mycpptutorial/stable/build/f8bda7f0751e4bc3beaa6c3b2eb02d455291c8a2/datetimeutil-shared-lib-conan'
