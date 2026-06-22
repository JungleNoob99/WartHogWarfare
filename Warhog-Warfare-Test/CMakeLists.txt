cmake_minimum_required(VERSION 3.16)
project(WarhogWarfare LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add executable
add_executable(WarhogWarfare
    GameEngine/MainCombatSYS.cpp
    GameEngine/CivilWarTagGenerator.cpp
    GameEngine/NationsTags.cpp
    main.cpp
)

target_include_directories(WarhogWarfare PRIVATE GameEngine)