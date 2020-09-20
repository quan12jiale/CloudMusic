cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

project(musicplayer LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_PREFIX_PATH $ENV{QTDIR})
find_package(Qt5 COMPONENTS Core Gui Widgets Network Multimedia REQUIRED)

set(HEADERS 
    widgets/addition.h 
    widgets/desktoplyricbuttons.h 
    widgets/base.h 
    music.h 
    widgets/downloadframe.h 
    widgets/loginframes.h 
    widgets/native.h 
    widgets/recommendframe.h 
    widgets/singsframebase.h 
    os.h 
    apis/apirequestsbase.h 
    apis/neteaseapi.h 
    apis/neteaseencode.h 
    widgets/systemtray.h 
    widgets/player.h 
    widgets/neteasesingsframes.h 
    features/configneteasefeatures.h 
    features/configrecommendframefeatures.h 
    features/configmainfeatures.h 
    features/configdownloadframefeatures.h 
    widgets/changeskinwidget.h 
    widgets/skinwidget.h
)

set(SOURCES 
    main.cpp 
    widgets/addition.cpp 
    widgets/desktoplyricbuttons.cpp 
    widgets/base.cpp 
    music.cpp 
    widgets/downloadframe.cpp 
    widgets/loginframes.cpp 
    widgets/native.cpp 
    widgets/recommendframe.cpp 
    widgets/singsframebase.cpp 
    os.cpp 
    apis/apirequestsbase.cpp 
    apis/neteaseapi.cpp 
    apis/neteaseencode.cpp 
    widgets/systemtray.cpp 
    widgets/player.cpp 
    widgets/neteasesingsframes.cpp 
    features/configneteasefeatures.cpp 
    features/configrecommendframefeatures.cpp 
    features/configmainfeatures.cpp 
    features/configdownloadframefeatures.cpp 
    widgets/changeskinwidget.cpp 
    widgets/skinwidget.cpp
)

set(RESOURCES 
    res.qrc
)

add_executable(${PROJECT_NAME} ${HEADERS} ${SOURCES} ${RESOURCES})
target_link_libraries(${PROJECT_NAME} Qt5::Core Qt5::Gui Qt5::Widgets Qt5::Network Qt5::Multimedia)