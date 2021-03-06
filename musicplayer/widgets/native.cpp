﻿#include "native.h"
#include "music.h"

NativeMusic::NativeMusic(Window *parent)
    : ScrollArea (parent)
{
    this->config = nullptr;

    this->parent = parent;
    this->setObjectName("nativeMusic");

    this->mainLayout = new QVBoxLayout(this);

    this->setTopShow();
    this->musicTable();

    QFile file("QSS/nativeMusic.qss");
    if (file.open(QIODevice::ReadOnly)) {
        QTextStream in(&file);
        //this->setStyleSheet(in.readAll());
    }
}

void NativeMusic::setTopShow()
{
    this->showLabel = new QLabel(tr("本地音乐"));

    this->spaceLine = new QFrame(this);
    this->spaceLine->setObjectName("spaceLine");
    this->spaceLine->setFrameShape(QFrame::HLine);
    this->spaceLine->setFrameShadow(QFrame::Plain);
    this->spaceLine->setLineWidth(2);

    this->selectButton = new QPushButton(tr("选择目录"));
    this->selectButton->setObjectName("selectButton");

    this->topShowLayout = new QHBoxLayout();
    this->topShowLayout->addSpacing(20);
    this->topShowLayout->addWidget(this->showLabel);
    this->topShowLayout->addWidget(this->selectButton);
    this->topShowLayout->addStretch(1);

    this->mainLayout->addLayout(this->topShowLayout);
    this->mainLayout->addWidget(this->spaceLine);
}

void NativeMusic::musicTable()
{
    this->singsTable = new QTableWidget();
    this->singsTable->setObjectName("singsTable");
    this->singsTable->setMinimumWidth(this->width());
    this->singsTable->setColumnCount(3);
    this->singsTable->setHorizontalHeaderLabels(QStringList({tr("音乐标题"), tr("歌手"), tr("时长")}));

    this->singsTable->setColumnWidth(0, this->width()/3*1.25);
    this->singsTable->setColumnWidth(1, this->width()/3*1.25);
    this->singsTable->setColumnWidth(2, this->width()/3*0.5);
    this->singsTable->horizontalHeader()->setStretchLastSection(true);
    this->singsTable->verticalHeader()->setVisible(false);
    this->singsTable->setShowGrid(false);
    this->singsTable->setAlternatingRowColors(true);

    this->singsTable->setEditTriggers(QAbstractItemView::NoEditTriggers);
    this->singsTable->setSelectionBehavior(QAbstractItemView::SelectRows);

    this->mainLayout->addWidget(this->singsTable);
}

static void test()
{
    NativeMusic* music = new NativeMusic(nullptr);
    music->show();
}
