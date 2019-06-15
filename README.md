# datetimeutil-shared-lib-conan


```
conan export . datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable

conan remote remove datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable

conan remote add datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable https://api.bintray.com/conan/mycpptutorial/datetimeutil

conan user -p <APIKEY> -r datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable yourbintrayusername


conan install datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable --build=datetimeutil-shared-lib-conan

conan upload "datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable" -r datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable --all

```
