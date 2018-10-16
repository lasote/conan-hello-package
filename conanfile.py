from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "Hello"
    version = "0.1"
    license="MIT"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/memsharded/conan-hello.git"
    exports_sources = "*"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib",  keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
