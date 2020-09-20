#include "neteaseencode.h"

QString createSecretKey(int size)
{
    Q_UNUSED(size)
    QString res;
    QList<QChar> list = random::sample("1234567890qwertyuipasdfghjklzxcvbnm", 16);
    foreach (const QChar& ch, list)
        res.append(ch);
    return res;
}

const QString python_executable = "D:/Anaconda3/python.exe";

QHash<QString,QString> encrypted_request(const QHash<QString, QString> &dict)
{
    QString text;
    text.append('{');
    foreach (const QString& key, dict.keys()) {
        QString val = dict[key];
        text.append("\"");
        text.append(key);
        text.append("\": \"");

        text.append(val);
        text.append("\", ");
    }
    text.chop(2);//去除最后的逗号和空格
    text.append('}');
    //qDebug() << text;

    QProcess process;
    QStringList arguments({"temp.py", text});//注意不要修改或删除temp.py
    process.start(python_executable, arguments);
    process.waitForFinished();
    QString res = process.readAllStandardOutput();

    QHash<QString,QString> data;
    QStringList list = res.split("\r\n");
    if (list.size() < 2) {
        QMessageBox::warning(nullptr, __FILE__, __func__);
        return data;
    }
    QString encText = list[0];
    QString encSecKey = list[1];

    data["params"] = encText;
    data["encSecKey"] = encSecKey;
    return data;
}

QHash<QString,QString> encrypted_request(const QList<long long> &ids)
{
    QString text = "{\"csrf_token\": \"\", \"ids\": [";
    foreach (long long id, ids) {
        text.append(QString::number(id));
        text.append(", ");
    }
    text.chop(2);//去除最后的逗号和空格
    text.append("], \"br\": 999000}");
    //qDebug() << text;

    QProcess process;
    QStringList arguments({"temp.py", text});//注意不要修改或删除temp.py
    process.start(python_executable, arguments);
    process.waitForFinished();
    QString res = process.readAllStandardOutput();

    QHash<QString,QString> data;
    QStringList list = res.split("\r\n");
    if (list.size() < 2) {
        QMessageBox::warning(nullptr, __FILE__, __func__);
        return data;
    }
    QString encText = list[0];
    QString encSecKey = list[1];

    data["params"] = encText;
    data["encSecKey"] = encSecKey;
    return data;
}


QHash<QString,QString> encrypted_request2(const QHash<QString, QString> &dict)
{
    QFile file("temp2.txt");
    if (file.open(QIODevice::WriteOnly)) {
        QTextStream out(&file);
        out << dict["s"];
        file.close();
    }

    QProcess process;
    QStringList arguments({"temp2.py"});//注意不要修改或删除temp2.py
    process.start(python_executable, arguments);
    process.waitForFinished();
    QString res = process.readAllStandardOutput();

    QHash<QString,QString> data;
    QStringList list = res.split("\r\n");
    if (list.size() < 2) {
        QMessageBox::warning(nullptr, __FILE__, __func__);
        return data;
    }
    QString encText = list[0];
    QString encSecKey = list[1];

    data["params"] = encText;
    data["encSecKey"] = encSecKey;
    return data;
}


QHash<QString,QString> encrypted_request3(const QHash<QString, QString> &dict)
{
    QFile file("temp3.txt");
    if (file.open(QIODevice::WriteOnly)) {
        QTextStream out(&file);
        out << dict["s"];
        //qDebug() << dict["s"];
        file.close();
    }

    //QProcess process;
    QStringList arguments({"temp3.py"});//注意不要修改或删除temp3.py
    //process.start(python_executable, arguments);
    //process.waitForFinished();
    QProcess::execute("python", arguments);

    QHash<QString,QString> data;
    QString encText;
    QString encSecKey;
    if (file.open(QIODevice::ReadOnly)) {
        QString encText = file.readLine();//多了\r\n
        QString encSecKey = file.readLine();
        //qDebug() << encText;
        //qDebug() << encSecKey;

        data["params"] = encText;
        data["encSecKey"] = encSecKey;
        file.close();
    }

    return data;
}
