from conans import ConanFile


class GladConan(ConanFile):
    name = "glad"
    version = "0.1"
    url = "https://github.com/Esri/glad/tree/runtimecore"
    license = "https://github.com/Esri/glad/blob/runtimecore/LICENSE"
    description = "An OpenGL and OpenGL ES shader front end and validator."

    # RTC specific triple
    settings = "platform_architecture_target"

    def package(self):
        base = self.source_folder + "/"
        relative = "3rdparty/glad/"

        # headers
        self.copy("*.h*", src=base, dst=relative)

        # libraries
        output = "output/" + str(self.settings.platform_architecture_target) + "/staticlib"
        self.copy("*" + self.name + "*", src=base + "../../" + output, dst=output)
