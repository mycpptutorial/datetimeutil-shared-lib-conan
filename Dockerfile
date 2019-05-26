FROM python:latest
RUN apt-get update
RUN apt-get -y install g++
RUN apt-get -y install cmake
RUN pip install conan
COPY . /usr/src/mycpptutorial/datetimeutil-shared-lib-conan
RUN rm -rf /usr/src/mycpptutorial/datetimeutil-shared-lib-conan/build > /dev/null
RUN mkdir -p /usr/src/mycpptutorial/datetimeutil-shared-lib-conan/build
WORKDIR /usr/src/mycpptutorial/datetimeutil-shared-lib-conan/build
RUN conan install ..
RUN conan build ..
