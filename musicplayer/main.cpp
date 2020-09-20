#include "widgets/addition.h"
#include "music.h"
#include <QApplication>

void initialize()
{
    if (!QFileInfo::exists(cacheFolder)) {
        QDir dir;
        dir.mkdir(cacheFolder);
    }
    QCoreApplication::setOrganizationName("Quan");
    QCoreApplication::setApplicationName("musicplayer");

    qRegisterMetaType<PlayTimesStruct>();
    qRegisterMetaTypeStreamOperators<PlayTimesStruct>("PlayTimesStruct");

    QObject::connect(picsQueue, &QueueObject::add, __addPic);
}


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QTranslator translator;
    bool res = translator.load(":/ZH_CN.qm");
    a.installTranslator(&translator);

    initialize();
    start();
    //"微软雅黑","微软雅黑 Light"

    return a.exec();
}
