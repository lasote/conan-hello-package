from conans import ConanFile, CMake, tools
import os


class HelloReuseConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        # equal to ./bin/greet, but portable win: .\bin\greet
        if not tools.cross_building(self.settings):
            self.run(os.sep.join([".", "bin", "greet"]))
