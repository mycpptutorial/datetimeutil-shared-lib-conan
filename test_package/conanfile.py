class DatetimeUtilSharedLibConanTest(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "datetimeutil-shared-lib-conan/1.0.0@mycpptutorial/stable"
    generators = "cmake"

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
