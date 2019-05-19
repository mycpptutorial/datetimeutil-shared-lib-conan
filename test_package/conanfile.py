import os

from conans import ConanFile, CMake, tools

class DatetimeUtilSharedLibConanTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run(".%sexample" % os.sep)
