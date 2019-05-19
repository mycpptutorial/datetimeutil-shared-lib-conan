from conans import ConanFile, CMake, tools


class CpprestsdkConan(ConanFile):
    name = "datetimeutil-shared-lib-conan"
    version = "1.0.0"
    license = "MIT"
    author = "Nasim Kabiliravi <conanrepos@gmail.com>"
    url = "https://github.com/mycpptutorial/datetimeutil-shared-lib-conan"
    description = "A C++ sample to learn how to create shared library and make it as a conan package."
    topics = ("C++ Shared Library", "conan", "package manager", "cpp", "C++ tutorial", "Conan Package Manager")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/mycpptutorial/datetimeutil-shared-lib-conan.git")
        self.run("cd datetimeutil-shared-lib-conan")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="datetimeutil-shared-lib-conan")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["datetimeutil-shared-lib-conan"]
