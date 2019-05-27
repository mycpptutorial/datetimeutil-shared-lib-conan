#!/bin/bash

mkdir -rf ../build
mkdir ../build
cd ../build
conan install ..
conan build ..
