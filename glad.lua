project "glad"

dofile(_BUILD_DIR .. "/static_library.lua")

configuration { "*" }

uuid "AA63205E-D54C-4A38-AB01-E406ED9DDDDD"

includedirs {
  ".",
}

files {
  "src/glad.c",
}

if (_PLATFORM_ANDROID) then
end

if (_PLATFORM_COCOA) then
end

if (_PLATFORM_IOS) then
end

if (_PLATFORM_LINUX) then
end

if (_PLATFORM_MACOS) then
end

if (_PLATFORM_WINDOWS) then
end

if (_PLATFORM_WINUWP) then
end
